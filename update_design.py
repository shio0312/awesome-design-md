#!/usr/bin/env python3
"""
既存DESIGN.md更新ツール

sites.yamlに登録されているサイトのDESIGN.mdを再生成します。
サイトのデザインが更新された際に使用してください。
"""

import os
import sys
from pathlib import Path
from typing import Optional
import json

try:
    import yaml
except ImportError:
    print("❌ エラー: pyyaml がインストールされていません")
    print("以下のコマンドでインストールしてください:")
    print("  pip install pyyaml")
    sys.exit(1)

import anthropic
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# 環境変数を読み込み
load_dotenv()


class DesignMDUpdater:
    """DESIGN.md更新クラス"""

    def __init__(self):
        """初期化"""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("エラー: ANTHROPIC_API_KEYが設定されていません")
            print(".envファイルにAPIキーを設定してください")
            sys.exit(1)

        self.client = anthropic.Anthropic(api_key=api_key)
        self.project_root = Path(__file__).parent
        self.design_md_dir = self.project_root / "design-md"
        self.sites_yaml_path = self.project_root / "sites.yaml"

    def load_sites(self) -> list[dict]:
        """sites.yamlからサイト情報を読み込み"""
        if not self.sites_yaml_path.exists():
            print(f"❌ {self.sites_yaml_path} が見つかりません")
            sys.exit(1)

        with open(self.sites_yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return data.get("sites", [])

    def fetch_page_content(self, url: str) -> tuple[str, str]:
        """
        PlaywrightでWebページのHTML/CSSを取得
        """
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

                    elements.forEach((el, idx) => {
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
                print("✅ ページの取得完了")

                browser.close()
                return html_content, styles_json

            except Exception as e:
                print(f"❌ エラー: {e}")
                browser.close()
                return "", ""

    def generate_design_md(self, site: dict, html: str, styles: str) -> str:
        """Claude APIを使ってDESIGN.mdを生成"""
        print(f"\n🤖 Claude APIで {site['name']} のDESIGN.mdを生成中...")

        # 既存のDESIGN.mdサンプルを参照
        sample_path = self.design_md_dir / "claude" / "DESIGN.md"
        sample_content = ""
        if sample_path.exists():
            with open(sample_path, "r", encoding="utf-8") as f:
                sample_content = f.read()[:3000]

        prompt = f"""あなたはWebデザインシステムの専門家です。以下のWebサイトを分析して、DESIGN.mdファイルを生成してください。

WebサイトURL: {site['url']}
サイト名: {site['name']}
説明: {site['description']}

提供情報:
1. HTMLコンテンツ（一部抜粋）
2. 計算済みCSSスタイル情報

DESIGN.mdは以下の形式に従ってください:

## 必須セクション:

### 1. Visual Theme & Atmosphere
- サイト全体の雰囲気、デザイン哲学を詳細に記述
- 主要な視覚的特徴（フォント、カラー、スペーシング等）
- 競合他社との差別化ポイント

### 2. Color Palette & Roles
- Primary, Secondary, Accent カラー
- Surface & Background カラー
- Neutrals & Text カラー
- 各カラーの16進数コードと役割を明記

### 3. Typography Rules
- フォントファミリー（Web font名）
- 見出し・本文・コード用のタイポグラフィ階層
- フォントサイズ、ウェイト、行間、字間の具体的な数値

### 4. Component Stylings
- Button（Primary, Secondary, Ghost等）のスタイル
- Input、Card、Navigation等の主要コンポーネント
- ホバー、フォーカス、アクティブ等の状態

### 5. Layout Principles
- スペーシングシステム（4px, 8px, 16px等）
- グリッドシステム
- コンテナ幅、余白の考え方

### 6. Depth & Elevation
- シャドウシステム
- レイヤリングの考え方

### 7. Do's and Don'ts
- デザインガイドライン
- アンチパターン

### 8. Responsive Behavior
- ブレークポイント
- モバイル対応戦略

### 9. Agent Prompt Guide
- AI エージェント向けのクイックリファレンス
- 推奨プロンプト例

## 参考サンプル（Claude DESIGN.mdの冒頭部分）:
{sample_content}

---

HTMLコンテンツ（抜粋）:
{html[:5000]}

---

計算済みスタイル情報:
{styles[:5000]}

---

上記の情報を元に、このWebサイトのDESIGN.mdを詳細に生成してください。
具体的な数値（色コード、フォントサイズ、スペーシング等）を必ず含めてください。
"""

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=16000,
                temperature=0.3,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )

            design_md_content = message.content[0].text
            print("✅ DESIGN.md生成完了")
            return design_md_content

        except Exception as e:
            print(f"❌ Claude API エラー: {e}")
            return ""

    def update_site(self, site: dict) -> bool:
        """サイトのDESIGN.mdを更新"""
        print(f"\n{'='*60}")
        print(f"🔄 {site['name']} のDESIGN.mdを更新")
        print(f"{'='*60}")

        # 既存のDESIGN.mdパス
        site_dir = self.design_md_dir / site['folder']
        design_md_path = site_dir / "DESIGN.md"

        # 既存ファイルのバックアップ
        backup_path = None
        if design_md_path.exists():
            backup_path = site_dir / "DESIGN.md.backup"
            import shutil
            shutil.copy(design_md_path, backup_path)
            print(f"📦 既存ファイルをバックアップ: {backup_path.name}")

        # ページ内容を取得
        html, styles = self.fetch_page_content(site['url'])
        if not html:
            print("❌ ページの取得に失敗しました")
            return False

        # DESIGN.mdを生成
        design_md = self.generate_design_md(site, html, styles)
        if not design_md:
            print("❌ DESIGN.mdの生成に失敗しました")
            return False

        # ファイルに保存
        site_dir.mkdir(parents=True, exist_ok=True)
        with open(design_md_path, "w", encoding="utf-8") as f:
            f.write(design_md)

        print(f"✅ 更新完了: {design_md_path}")

        # 差分を表示（簡易版）
        if backup_path and backup_path.exists():
            old_size = backup_path.stat().st_size
            new_size = design_md_path.stat().st_size
            print(f"\n📊 ファイルサイズ: {old_size} → {new_size} bytes")

        return True

    def show_sites_menu(self, sites: list[dict]) -> None:
        """サイト一覧をカテゴリ別に表示"""
        # カテゴリごとにグループ化
        categories = {}
        for site in sites:
            category = site.get('category', 'Other')
            if category not in categories:
                categories[category] = []
            categories[category].append(site)

        print("\n📋 登録されているサイト一覧:\n")

        idx = 1
        site_index_map = {}

        for category, category_sites in categories.items():
            print(f"【{category}】")
            for site in category_sites:
                auto_update = "✓" if site.get('auto_update', True) else " "
                print(f"  {idx:2d}. [{auto_update}] {site['name']:<20} ({site['folder']})")
                site_index_map[idx] = site
                idx += 1
            print()

        return site_index_map


def main():
    """メイン処理"""
    print("=" * 60)
    print("🔄 DESIGN.md 更新ツール")
    print("=" * 60)
    print("\n既存サイトのDESIGN.mdを再生成します")
    print("サイトのデザインが更新された際にご使用ください\n")

    updater = DesignMDUpdater()

    # サイト一覧を読み込み
    sites = updater.load_sites()
    if not sites:
        print("❌ sites.yaml にサイトが登録されていません")
        return

    while True:
        # サイト一覧を表示
        site_index_map = updater.show_sites_menu(sites)

        print("オプション:")
        print("  数字    : 指定したサイトを更新")
        print("  all     : 全サイトを更新")
        print("  auto    : auto_update=true のサイトのみ更新")
        print("  quit    : 終了")

        try:
            choice = input("\n選択 >>> ").strip().lower()

            if choice in ["quit", "exit", "q"]:
                print("\n👋 終了します")
                break

            elif choice == "all":
                print(f"\n🚀 全 {len(sites)} サイトを更新します...")
                confirm = input("本当に実行しますか？ (yes/no) >>> ").strip().lower()
                if confirm == "yes":
                    success_count = 0
                    for site in sites:
                        if updater.update_site(site):
                            success_count += 1
                    print(f"\n✅ 完了: {success_count}/{len(sites)} サイトを更新しました")

            elif choice == "auto":
                auto_sites = [s for s in sites if s.get('auto_update', True)]
                print(f"\n🚀 auto_update=true の {len(auto_sites)} サイトを更新します...")
                confirm = input("本当に実行しますか？ (yes/no) >>> ").strip().lower()
                if confirm == "yes":
                    success_count = 0
                    for site in auto_sites:
                        if updater.update_site(site):
                            success_count += 1
                    print(f"\n✅ 完了: {success_count}/{len(auto_sites)} サイトを更新しました")

            elif choice.isdigit():
                idx = int(choice)
                if idx in site_index_map:
                    site = site_index_map[idx]
                    updater.update_site(site)
                else:
                    print("❌ 無効な番号です")

            else:
                print("❌ 無効な入力です")

        except KeyboardInterrupt:
            print("\n\n👋 終了します")
            break
        except Exception as e:
            print(f"\n❌ エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
