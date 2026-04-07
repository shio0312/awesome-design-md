#!/usr/bin/env python3
"""
DESIGN.md自動更新スクリプト（非対話型）

GitHub Actionsから呼び出されるバージョン
auto_update=true のサイトを自動更新します
"""

import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("❌ エラー: pyyaml がインストールされていません")
    sys.exit(1)

import anthropic
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# 環境変数を読み込み（スクリプトと同じディレクトリの .env を参照）
load_dotenv(Path(__file__).parent / ".env", override=True)


class AutoUpdater:
    """自動更新クラス"""

    def __init__(self):
        """初期化"""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("❌ ANTHROPIC_API_KEYが設定されていません")
            sys.exit(1)

        self.client = anthropic.Anthropic(api_key=api_key)
        self.project_root = Path(__file__).parent
        self.design_md_dir = self.project_root / "design-md"
        self.sites_yaml_path = self.project_root / "sites.yaml"

    def load_sites(self) -> list[dict]:
        """sites.yamlからauto_update=trueのサイトを読み込み"""
        with open(self.sites_yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        all_sites = data.get("sites", [])
        # auto_updateがtrueのサイトのみ
        return [s for s in all_sites if s.get('auto_update', True)]

    def fetch_page_content(self, url: str) -> tuple[str, str]:
        """WebページのHTML/CSSを取得"""
        print(f"🌐 {url} にアクセス中...")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
                html_content = page.content()

                styles_script = """
                () => {
                    const elements = document.querySelectorAll('body, h1, h2, h3, h4, h5, h6, p, a, button, input, nav, header, footer, main');
                    const styles = [];
                    elements.forEach((el) => {
                        const computed = window.getComputedStyle(el);
                        styles.push({
                            tag: el.tagName,
                            className: el.className,
                            styles: {
                                color: computed.color,
                                backgroundColor: computed.backgroundColor,
                                fontFamily: computed.fontFamily,
                                fontSize: computed.fontSize,
                                fontWeight: computed.fontWeight,
                                lineHeight: computed.lineHeight,
                                letterSpacing: computed.letterSpacing,
                                borderRadius: computed.borderRadius,
                                boxShadow: computed.boxShadow,
                                padding: computed.padding,
                                margin: computed.margin
                            }
                        });
                    });
                    return JSON.stringify(styles);
                }
                """

                styles_json = page.evaluate(styles_script)
                print("✅ ページ取得完了")

                browser.close()
                return html_content, styles_json

            except Exception as e:
                print(f"❌ エラー: {e}")
                browser.close()
                return "", ""

    def generate_design_md(self, site: dict, html: str, styles: str) -> str:
        """Claude APIでDESIGN.mdを生成"""
        print(f"🤖 {site['name']} のDESIGN.mdを生成中...")

        sample_path = self.design_md_dir / "claude" / "DESIGN.md"
        sample_content = ""
        if sample_path.exists():
            with open(sample_path, "r", encoding="utf-8") as f:
                sample_content = f.read()[:3000]

        prompt = f"""あなたはWebデザインシステムの専門家です。以下のWebサイトを分析して、DESIGN.mdファイルを生成してください。

WebサイトURL: {site['url']}
サイト名: {site['name']}
説明: {site['description']}

DESIGN.mdは以下の9つのセクションを含めてください:

1. Visual Theme & Atmosphere
2. Color Palette & Roles
3. Typography Rules
4. Component Stylings
5. Layout Principles
6. Depth & Elevation
7. Do's and Don'ts
8. Responsive Behavior
9. Agent Prompt Guide

各セクションには具体的な数値（色コード、フォントサイズ、スペーシング等）を必ず含めてください。

参考サンプル:
{sample_content}

HTMLコンテンツ（抜粋）:
{html[:5000]}

計算済みスタイル情報:
{styles[:5000]}
"""

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=16000,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}]
            )

            content = message.content[0].text
            print("✅ DESIGN.md生成完了")
            return content

        except Exception as e:
            print(f"❌ Claude API エラー: {e}")
            return ""

    def update_site(self, site: dict) -> bool:
        """サイトのDESIGN.mdを更新"""
        print(f"\n{'='*60}")
        print(f"🔄 {site['name']} を更新")
        print(f"{'='*60}")

        # ページ内容を取得
        html, styles = self.fetch_page_content(site['url'])
        if not html:
            print(f"❌ {site['name']}: ページ取得失敗")
            return False

        # DESIGN.mdを生成
        design_md = self.generate_design_md(site, html, styles)
        if not design_md:
            print(f"❌ {site['name']}: 生成失敗")
            return False

        # ファイルに保存
        site_dir = self.design_md_dir / site['folder']
        site_dir.mkdir(parents=True, exist_ok=True)

        design_md_path = site_dir / "DESIGN.md"
        with open(design_md_path, "w", encoding="utf-8") as f:
            f.write(design_md)

        print(f"✅ {site['name']}: 更新完了")
        return True


def main():
    """メイン処理"""
    print("🤖 DESIGN.md 自動更新スクリプト")
    print("="*60)

    updater = AutoUpdater()

    # auto_update=true のサイトを読み込み
    sites = updater.load_sites()
    print(f"\n📋 更新対象: {len(sites)} サイト\n")

    # 各サイトを更新
    success_count = 0
    failed_sites = []

    for i, site in enumerate(sites, 1):
        print(f"\n[{i}/{len(sites)}] {site['name']}")

        if updater.update_site(site):
            success_count += 1
        else:
            failed_sites.append(site['name'])

    # 結果サマリー
    print(f"\n{'='*60}")
    print(f"📊 結果サマリー")
    print(f"{'='*60}")
    print(f"✅ 成功: {success_count}/{len(sites)}")

    if failed_sites:
        print(f"❌ 失敗: {len(failed_sites)}")
        print("失敗したサイト:")
        for name in failed_sites:
            print(f"  - {name}")

    # 失敗があった場合は終了コード1
    sys.exit(0 if not failed_sites else 1)


if __name__ == "__main__":
    main()
