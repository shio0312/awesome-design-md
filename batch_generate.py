#!/usr/bin/env python3
"""日本のデザインシステム バッチ生成スクリプト（非対話型）"""

import os
import sys
from pathlib import Path
import yaml
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env", override=True)

sys.path.insert(0, str(Path(__file__).parent))
from suggest_design import DesignMDGenerator

SITES = [
    {
        "name": "Wantedly",
        "folder": "wantedly",
        "url": "https://www.wantedly.com",
        "category": "Japanese Design Systems",
        "description": "日本のビジネス SNS。Wantedly UI Components をベースにしたデザインシステム",
        "auto_update": True,
    },
    {
        "name": "SPEEDA",
        "folder": "speeda",
        "url": "https://speeda.com",
        "category": "Japanese Design Systems",
        "description": "経済情報プラットフォーム。Falcon デザインシステムを採用",
        "auto_update": True,
    },
    {
        "name": "Sansan One Design",
        "folder": "sansan-one-design",
        "url": "https://ui.one-design-system.sansan.com",
        "category": "Japanese Design Systems",
        "description": "Sansan の One Design System。清潔感のある業務系 UI",
        "auto_update": True,
    },
    {
        "name": "Goodpatch Sparkle",
        "folder": "goodpatch-sparkle",
        "url": "https://sparkle-design.goodpatch.com/sparkle-design",
        "category": "Japanese Design Systems",
        "description": "Goodpatch の Sparkle デザインシステム。デザイン会社らしい洗練された UI",
        "auto_update": True,
    },
    {
        "name": "Serendie",
        "folder": "serendie",
        "url": "https://serendie.design",
        "category": "Japanese Design Systems",
        "description": "Sony のデザインシステム Serendie。グローバル品質の日本発デザイン",
        "auto_update": True,
    },
    {
        "name": "Raksul Kamii",
        "folder": "raksul-kamii",
        "url": "https://zeroheight.com/731d8c745/p/018df4-kamii--raksul-design-system",
        "category": "Japanese Design Systems",
        "description": "ラクスルのデザインシステム Kamii。印刷・物流サービスの業務系 UI",
        "auto_update": False,  # zeroheight はアクセス制限の可能性あり
    },
    {
        "name": "Pepabo Design",
        "folder": "pepabo",
        "url": "https://design.pepabo.com",
        "category": "Japanese Design Systems",
        "description": "GMO ペパボのデザインガイドライン。親しみやすくフレンドリーな UI",
        "auto_update": True,
    },
    {
        "name": "Ubie Vitals",
        "folder": "ubie-vitals",
        "url": "https://vitals.ubie.life",
        "category": "Japanese Design Systems",
        "description": "Ubie のデザインシステム Vitals。医療系サービスの信頼感ある UI",
        "auto_update": True,
    },
    {
        "name": "Digital Agency Design",
        "folder": "digital-agency",
        "url": "https://design.digital.go.jp/dads/",
        "category": "Japanese Design Systems",
        "description": "デジタル庁のデザインシステム DADS。行政向けのアクセシブルな UI",
        "auto_update": True,
    },
    {
        "name": "SmartHR Design",
        "folder": "smarthr",
        "url": "https://smarthr.design",
        "category": "Japanese Design Systems",
        "description": "SmartHR のデザインシステム。HR SaaS らしいシンプルで機能的な UI",
        "auto_update": True,
    },
    {
        "name": "Ameba Spindle",
        "folder": "ameba-spindle",
        "url": "https://spindle.ameba.design",
        "category": "Japanese Design Systems",
        "description": "CyberAgent Ameba の Spindle デザインシステム。ブログ・メディア系の親しみやすい UI",
        "auto_update": True,
    },
]


def add_to_sites_yaml(sites_yaml_path: Path, site: dict):
    with open(sites_yaml_path, "r", encoding="utf-8") as f:
        content = f.read()

    data = yaml.safe_load(content) or {"sites": []}
    existing_folders = {s.get("folder") for s in data.get("sites", [])}

    if site["folder"] in existing_folders:
        print(f"  スキップ（既登録）: {site['name']}")
        return

    data["sites"].append(site)

    with open(sites_yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=120)
    print(f"  sites.yaml に追加: {site['name']}")


def main():
    generator = DesignMDGenerator()
    sites_yaml_path = Path(__file__).parent / "sites.yaml"

    success, failed = [], []

    for site in SITES:
        print(f"\n{'='*60}")
        print(f"処理中: {site['name']} ({site['url']})")
        print(f"{'='*60}")

        # sites.yaml に追記
        add_to_sites_yaml(sites_yaml_path, site)

        # DESIGN.md 生成
        html, styles = generator.fetch_page_content(site["url"])
        if not html:
            print(f"❌ ページ取得失敗: {site['name']}")
            failed.append(site["name"])
            continue

        design_md = generator.generate_design_md(site["url"], html, styles)
        if not design_md:
            print(f"❌ 生成失敗: {site['name']}")
            failed.append(site["name"])
            continue

        generator.save_design_md(site["folder"], design_md)
        success.append(site["name"])

    print(f"\n{'='*60}")
    print(f"完了: {len(success)}/{len(SITES)} サイト")
    if failed:
        print(f"失敗: {failed}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
