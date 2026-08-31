#!/usr/bin/env python3
"""
Refero Styles 同期ツール

https://styles.refero.design/ で公開されているデザインシステム
（DESIGN.md 相当のデータ）をこのリポジトリに取り込んで管理します。

Refero Styles は実在サイトのデザインを構造化データとして公開しており、
公開 API から取得した designSystem JSON を決定的に DESIGN.md へ変換します
（Claude API キーは不要）。

使い方:
    python sync_refero_styles.py --list             # カタログ一覧を表示
    python sync_refero_styles.py <id|url> ...       # 指定スタイルを同期
    python sync_refero_styles.py --all              # 全スタイルを同期
    python sync_refero_styles.py --update           # 登録済みスタイルを再同期
    python sync_refero_styles.py --list --pages 5   # 取得ページ数を指定

同期したスタイルは sites.yaml に source: refero-styles / refero_id 付きで
登録され、auto_update: false になります（更新は本ツールの --update で行い、
Claude API による再生成対象にはしません）。
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("❌ エラー: pyyaml がインストールされていません")
    print("  pip install pyyaml")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("❌ エラー: requests がインストールされていません")
    print("  pip install requests")
    sys.exit(1)

API_BASE_URL = "https://styles.refero.design/api"
SITE_BASE_URL = "https://styles.refero.design"
REQUEST_TIMEOUT = 30
DEFAULT_MAX_PAGES = 10
CATEGORY = "Refero Styles"

README_START_MARKER = "<!-- refero-styles:start -->"
README_END_MARKER = "<!-- refero-styles:end -->"

PROJECT_ROOT = Path(__file__).parent
DESIGN_MD_DIR = PROJECT_ROOT / "design-md"
SITES_YAML_PATH = PROJECT_ROOT / "sites.yaml"
README_PATH = PROJECT_ROOT / "README.md"

UUID_RE = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.IGNORECASE
)


# ---------------------------------------------------------------------------
# Refero Styles API
# ---------------------------------------------------------------------------

def _get(path: str, params: dict | None = None) -> dict:
    """Refero Styles API に GET リクエスト"""
    response = requests.get(
        f"{API_BASE_URL}{path}",
        params=params,
        timeout=REQUEST_TIMEOUT,
        headers={
            "Accept": "application/json",
            "User-Agent": "awesome-design-md-sync/1.0",
        },
    )
    response.raise_for_status()
    return response.json()


def list_styles(page: int = 1) -> dict:
    """スタイル一覧を1ページ分取得"""
    return _get("/styles", params={"page": page})


def fetch_all_summaries(max_pages: int = DEFAULT_MAX_PAGES) -> list[dict]:
    """スタイル一覧を全ページ分取得"""
    summaries: list[dict] = []
    for page in range(1, max_pages + 1):
        result = list_styles(page)
        styles = result.get("styles") or []
        summaries.extend(styles)
        if not result.get("nextPage") or not styles:
            break
    return summaries


def get_style(style_id: str) -> dict:
    """スタイル詳細（designSystem 含む）を取得"""
    data = _get(f"/styles/{style_id}")
    if isinstance(data, dict) and data.get("style"):
        style = data["style"]
        if data.get("similar"):
            style["similar"] = data["similar"]
        return style
    return data


# ---------------------------------------------------------------------------
# DESIGN.md 生成（styles.refero.design の designSystem JSON から決定的に変換）
# ---------------------------------------------------------------------------

def _color_line(color: dict) -> str:
    role = f" — {color['role']}" if color.get("role") else ""
    group = f" [{color['group']}]" if color.get("group") else ""
    return f"- **{color.get('name', 'Unnamed')}**: `{color.get('hex', '?')}`{role}{group}"


def generate_design_md(style: dict) -> str:
    """StyleDetail から DESIGN.md を生成"""
    ds = (style.get("fullResult") or {}).get("designSystem") or {}
    lines: list[str] = []

    site_name = style.get("siteName", "Unknown")
    lines.append(f"# {site_name} — Design System")
    lines.append("")
    lines.append(f"> **North Star**: {style.get('northStar') or ds.get('northStar') or 'N/A'}")
    lines.append(f"> **Theme**: {ds.get('theme') or style.get('colorScheme') or 'N/A'}")
    lines.append(f"> **Source**: {style.get('url', 'N/A')}")
    lines.append(f"> **Refero Style**: {SITE_BASE_URL}/style/{style.get('id', '')}")
    lines.append(f"> **Synced**: {date.today().isoformat()}")
    lines.append("")

    if ds.get("description"):
        lines += ["## Overview", "", ds["description"], ""]

    colors = ds.get("colors") or [
        {"name": c.get("name"), "hex": c.get("hex")} for c in (style.get("colors") or [])
    ]
    if colors:
        lines += ["## Color Palette", ""]
        lines += [_color_line(c) for c in colors]
        lines.append("")

    if ds.get("typography"):
        lines += ["## Typography", ""]
        for font in ds["typography"]:
            weights = f" (weights: {', '.join(str(w) for w in font['weights'])})" if font.get("weights") else ""
            fallback = f" — fallback: {font['fallback']}" if font.get("fallback") else ""
            lines.append(f"- **{font.get('family', 'Unknown')}**{weights}{fallback}")
        lines.append("")
    elif style.get("fonts"):
        lines += ["## Typography", ""]
        lines += [f"- **{font}**" for font in style["fonts"]]
        lines.append("")

    if ds.get("typeScale"):
        lines += [
            "## Type Scale",
            "",
            "| Role | Size | Weight | Line Height |",
            "|------|------|--------|-------------|",
        ]
        for step in ds["typeScale"]:
            lines.append(
                f"| {step.get('role', '—')} | {step.get('size', '—')} "
                f"| {step.get('weight', '—')} | {step.get('lineHeight', '—')} |"
            )
        lines.append("")

    spacing = ds.get("spacing") or {}
    if spacing:
        lines += ["## Spacing & Layout", ""]
        for key, label in [
            ("pageMaxWidth", "Max Width"),
            ("cardPadding", "Card Padding"),
            ("elementGap", "Element Gap"),
            ("sectionGap", "Section Gap"),
            ("radius", "Border Radius"),
        ]:
            if spacing.get(key):
                lines.append(f"- **{label}**: {spacing[key]}")
        lines.append("")

    if ds.get("layout"):
        lines += ["## Layout", "", ds["layout"], ""]

    if ds.get("surfaces"):
        lines += ["## Surfaces / Elevation", ""]
        for surface in ds["surfaces"]:
            color = f" (`{surface['color']}`)" if surface.get("color") else ""
            desc = f" — {surface['description']}" if surface.get("description") else ""
            lines.append(f"- **{surface.get('name', 'Surface')}**{color}{desc}")
        if ds.get("elevation"):
            lines += ["", "**Shadow tokens:**"]
            for el in ds["elevation"]:
                if el.get("shadow"):
                    name = f"{el['name']}: " if el.get("name") else ""
                    lines.append(f"- {name}`{el['shadow']}`")
        lines.append("")

    if ds.get("imagery"):
        lines += ["## Imagery", "", ds["imagery"], ""]

    if ds.get("dos") or ds.get("donts"):
        lines += ["## Design Principles", ""]
        if ds.get("dos"):
            lines += ["### Do", ""]
            lines += [f"- {item}" for item in ds["dos"]]
            lines.append("")
        if ds.get("donts"):
            lines += ["### Don't", ""]
            lines += [f"- {item}" for item in ds["donts"]]
            lines.append("")

    if ds.get("components"):
        lines += ["## Components", ""]
        for comp in ds["components"]:
            lines += [f"### {comp.get('name', 'Component')}", ""]
            if comp.get("description"):
                lines += [comp["description"], ""]
            if comp.get("html"):
                lines += ["```html", comp["html"], "```", ""]
            if comp.get("css"):
                lines += ["```css", comp["css"], "```", ""]

    if ds.get("similar"):
        lines += ["## Similar Design Systems", ""]
        lines += [f"- {s}" for s in ds["similar"]]
        lines.append("")

    for section in ds.get("customSections") or []:
        lines += [f"## {section.get('title', 'Notes')}", "", section.get("content", ""), ""]

    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# sites.yaml / README.md 管理
# ---------------------------------------------------------------------------

def slugify(name: str) -> str:
    """サイト名からフォルダ名を生成"""
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "unnamed"


def load_sites() -> list[dict]:
    if not SITES_YAML_PATH.exists():
        return []
    with open(SITES_YAML_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("sites", [])


def save_sites(sites: list[dict]) -> None:
    with open(SITES_YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(
            {"sites": sites},
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=120,
        )


def resolve_folder(style: dict, sites: list[dict]) -> str:
    """スタイルの保存先フォルダを決定（既存の非Referoフォルダと衝突したら -refero を付与）"""
    for site in sites:
        if site.get("refero_id") == style.get("id"):
            return site["folder"]

    slug = slugify(style.get("siteName", "unnamed"))
    taken = {s.get("folder") for s in sites}
    if slug in taken or (DESIGN_MD_DIR / slug).exists():
        slug = f"{slug}-refero"
    # それでも衝突する場合は ID 先頭8文字で一意化
    if slug in taken:
        slug = f"{slug}-{style.get('id', '')[:8]}"
    return slug


def describe(style: dict) -> str:
    """sites.yaml / README 用の1行説明"""
    north_star = (style.get("northStar") or "").strip().replace("\n", " ")
    if len(north_star) > 120:
        north_star = north_star[:117].rstrip() + "..."
    return north_star or "Design system synced from Refero Styles"


def register_site(style: dict, folder: str, sites: list[dict]) -> None:
    """sites.yaml にスタイルを登録（既存なら更新）"""
    entry = {
        "name": style.get("siteName", folder),
        "folder": folder,
        "url": style.get("url", ""),
        "category": CATEGORY,
        "description": describe(style),
        "auto_update": False,
        "source": "refero-styles",
        "refero_id": style.get("id", ""),
    }
    for i, site in enumerate(sites):
        if site.get("refero_id") == entry["refero_id"]:
            sites[i] = entry
            return
    sites.append(entry)


def update_readme(sites: list[dict]) -> None:
    """README の Refero Styles セクションと DESIGN.md カウントバッジを更新"""
    if not README_PATH.exists():
        return
    content = README_PATH.read_text(encoding="utf-8")

    refero_sites = sorted(
        (s for s in sites if s.get("source") == "refero-styles"),
        key=lambda s: s["name"].lower(),
    )
    items = "\n".join(
        f"- [**{s['name']}**](design-md/{s['folder']}/) - {s['description']}"
        for s in refero_sites
    )
    section_body = (
        f"{README_START_MARKER}\n"
        f"### Refero Styles\n\n"
        f"Design systems synced from [Refero Styles]({SITE_BASE_URL}) "
        f"via `sync_refero_styles.py`.\n\n"
        f"{items}\n"
        f"{README_END_MARKER}"
    )

    if README_START_MARKER in content and README_END_MARKER in content:
        content = re.sub(
            re.escape(README_START_MARKER) + r".*?" + re.escape(README_END_MARKER),
            section_body,
            content,
            flags=re.DOTALL,
        )
    elif "## Contributing" in content:
        content = content.replace("## Contributing", f"{section_body}\n\n## Contributing", 1)
    else:
        content = content.rstrip() + f"\n\n{section_body}\n"

    # DESIGN.md カウントバッジを実ファイル数で更新
    count = len(list(DESIGN_MD_DIR.glob("*/DESIGN.md")))
    content = re.sub(
        r"DESIGN\.md%20count-\d+-",
        f"DESIGN.md%20count-{count}-",
        content,
    )

    README_PATH.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# 同期処理
# ---------------------------------------------------------------------------

def parse_style_id(token: str) -> str:
    """UUID または styles.refero.design のスタイルURLから ID を抽出"""
    match = UUID_RE.search(token)
    if not match:
        raise ValueError(f"スタイルIDが読み取れません: {token}")
    return match.group(0).lower()


def sync_style(style_id: str, sites: list[dict]) -> bool:
    """1スタイルを取得して DESIGN.md 保存 + sites.yaml 登録"""
    try:
        style = get_style(style_id)
    except requests.RequestException as e:
        print(f"❌ {style_id}: 取得失敗 ({e})")
        return False

    folder = resolve_folder(style, sites)
    site_dir = DESIGN_MD_DIR / folder
    site_dir.mkdir(parents=True, exist_ok=True)
    (site_dir / "DESIGN.md").write_text(generate_design_md(style), encoding="utf-8")
    register_site(style, folder, sites)

    print(f"✅ {style.get('siteName', style_id)} → design-md/{folder}/DESIGN.md")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="styles.refero.design のデザインシステムを同期する"
    )
    parser.add_argument("styles", nargs="*", help="スタイルID または スタイルURL")
    parser.add_argument("--list", action="store_true", help="カタログ一覧を表示")
    parser.add_argument("--all", action="store_true", help="全スタイルを同期")
    parser.add_argument("--update", action="store_true", help="登録済みスタイルを再同期")
    parser.add_argument(
        "--pages", type=int, default=DEFAULT_MAX_PAGES,
        help=f"一覧取得の最大ページ数 (default: {DEFAULT_MAX_PAGES})",
    )
    args = parser.parse_args()

    if not (args.list or args.all or args.update or args.styles):
        parser.print_help()
        return

    if args.list:
        print("📋 Refero Styles カタログ:\n")
        try:
            summaries = fetch_all_summaries(args.pages)
        except requests.RequestException as e:
            print(f"❌ カタログの取得に失敗しました: {e}")
            sys.exit(1)
        registered = {s.get("refero_id") for s in load_sites()}
        for s in summaries:
            mark = "✓" if s.get("id") in registered else " "
            print(f"  [{mark}] {s.get('siteName', '?'):<28} {s.get('id', '')}  {s.get('url', '')}")
        print(f"\n合計: {len(summaries)} スタイル（✓ = 同期済み）")
        return

    sites = load_sites()
    targets: list[str] = []

    if args.all:
        try:
            targets += [s["id"] for s in fetch_all_summaries(args.pages) if s.get("id")]
        except requests.RequestException as e:
            print(f"❌ カタログの取得に失敗しました: {e}")
            sys.exit(1)
    if args.update:
        targets += [s["refero_id"] for s in sites if s.get("source") == "refero-styles" and s.get("refero_id")]
    for token in args.styles:
        try:
            targets.append(parse_style_id(token))
        except ValueError as e:
            print(f"❌ {e}")
            sys.exit(1)

    # 重複除去（順序維持）
    targets = list(dict.fromkeys(targets))
    if not targets:
        print("同期対象がありません（--update は同期済みスタイルがある場合のみ動作します）")
        return

    print(f"🔄 {len(targets)} スタイルを同期します\n")
    success = 0
    for style_id in targets:
        if sync_style(style_id, sites):
            success += 1

    save_sites(sites)
    update_readme(sites)

    print(f"\n📊 完了: {success}/{len(targets)} スタイルを同期")
    print("📝 sites.yaml と README.md を更新しました")
    if success < len(targets):
        sys.exit(1)


if __name__ == "__main__":
    main()
