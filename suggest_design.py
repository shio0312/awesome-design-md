#!/usr/bin/env python3
"""
対話型DESIGN.md生成ツール

WebサイトのURLを入力すると、自動的にデザインシステムを解析して
DESIGN.mdファイルを生成します。
"""

import os
import sys
import re
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import anthropic
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# yamlはオプション（sites.yaml更新用）
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# 環境変数を読み込み
load_dotenv()


class DesignMDGenerator:
    """DESIGN.md生成クラス"""

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

    def get_site_name(self, url: str) -> str:
        """URLからサイト名を抽出"""
        parsed = urlparse(url)
        domain = parsed.netloc
        # www. を削除
        domain = re.sub(r'^www\.', '', domain)
        # .com, .io などを削除してシンプルなサイト名にするか、
        # あるいはドメイン全体を使うかを選択
        # ここではドメイン全体を使用
        return domain

    def fetch_page_content(self, url: str) -> tuple[str, str]:
        """
        PlaywrightでWebページのHTML/CSSを取得

        Returns:
            tuple[str, str]: (HTML content, computed styles)
        """
        print(f"\n🌐 {url} にアクセス中...")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            try:
                # ページを開く
                page.goto(url, wait_until="networkidle", timeout=30000)

                # HTMLを取得
                html_content = page.content()

                # 主要要素のスタイル情報を取得
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

    def generate_design_md(self, url: str, html: str, styles: str) -> str:
        """
        Claude APIを使ってDESIGN.mdを生成

        Args:
            url: WebサイトのURL
            html: HTMLコンテンツ
            styles: 計算済みスタイル情報（JSON文字列）

        Returns:
            str: 生成されたDESIGN.mdの内容
        """
        print("\n🤖 Claude APIでDESIGN.mdを生成中...")

        # 既存のDESIGN.mdサンプルを参照として読み込み
        sample_path = self.design_md_dir / "claude" / "DESIGN.md"
        sample_content = ""
        if sample_path.exists():
            with open(sample_path, "r", encoding="utf-8") as f:
                sample_content = f.read()[:3000]  # 最初の3000文字のみ

        prompt = f"""あなたはWebデザインシステムの専門家です。以下のWebサイトを分析して、DESIGN.mdファイルを生成してください。

WebサイトURL: {url}

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

    def save_design_md(self, site_name: str, content: str) -> Path:
        """
        生成したDESIGN.mdをファイルに保存

        Args:
            site_name: サイト名（ディレクトリ名）
            content: DESIGN.mdの内容

        Returns:
            Path: 保存したファイルのパス
        """
        # ディレクトリ作成
        site_dir = self.design_md_dir / site_name
        site_dir.mkdir(parents=True, exist_ok=True)

        # DESIGN.mdを保存
        design_md_path = site_dir / "DESIGN.md"
        with open(design_md_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ 保存完了: {design_md_path}")

        # README.mdも作成（シンプルな説明）
        readme_path = site_dir / "README.md"
        readme_content = f"""# {site_name}

自動生成されたDESIGN.mdファイル

## 使い方

このDESIGN.mdをプロジェクトのルートにコピーして、AIエージェントに以下のように指示してください:

```
このDESIGN.mdに従ってUIを構築してください
```
"""

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

        return design_md_path

    def add_to_sites_yaml(self, site_name: str, url: str) -> bool:
        """
        sites.yamlに新しいサイトを追加

        Args:
            site_name: サイト名（フォルダ名）
            url: サイトのURL

        Returns:
            bool: 成功したかどうか
        """
        if not HAS_YAML:
            print("⚠️  pyyamlがインストールされていないため、sites.yamlを更新できません")
            print("   pip install pyyaml を実行してください")
            return False

        # sites.yamlが存在しない場合は作成
        if not self.sites_yaml_path.exists():
            print("⚠️  sites.yaml が見つかりません。スキップします")
            return False

        # 既存のsites.yamlを読み込み
        with open(self.sites_yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        sites = data.get("sites", [])

        # 既に登録されているかチェック
        for site in sites:
            if site.get("folder") == site_name:
                print(f"ℹ️  {site_name} は既にsites.yamlに登録されています")
                return True

        # カテゴリを推測（ユーザーに聞くこともできるが、ここではデフォルト）
        category = input(f"\n📁 カテゴリを入力してください（例: Developer Tools & Platforms）>>> ").strip()
        if not category:
            category = "Other"

        description = input(f"📝 簡単な説明を入力してください >>> ").strip()
        if not description:
            description = "自動生成されたDESIGN.md"

        # 新しいサイトを追加
        new_site = {
            "name": site_name.replace("-", " ").replace(".", " ").title(),
            "folder": site_name,
            "url": url,
            "category": category,
            "description": description,
            "auto_update": True
        }

        sites.append(new_site)
        data["sites"] = sites

        # sites.yamlに保存
        with open(self.sites_yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(
                data,
                f,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,
                width=120
            )

        print(f"✅ sites.yaml に追加しました")
        return True

    def process_url(self, url: str) -> bool:
        """
        URLを処理してDESIGN.mdを生成

        Args:
            url: WebサイトのURL

        Returns:
            bool: 成功したかどうか
        """
        # URLの正規化
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        print(f"\n{'='*60}")
        print(f"🎨 DESIGN.md生成開始: {url}")
        print(f"{'='*60}")

        # サイト名を抽出
        site_name = self.get_site_name(url)
        print(f"📝 サイト名: {site_name}")

        # ページ内容を取得
        html, styles = self.fetch_page_content(url)
        if not html:
            print("❌ ページの取得に失敗しました")
            return False

        # DESIGN.mdを生成
        design_md = self.generate_design_md(url, html, styles)
        if not design_md:
            print("❌ DESIGN.mdの生成に失敗しました")
            return False

        # ファイルに保存
        saved_path = self.save_design_md(site_name, design_md)

        # sites.yamlに追加
        self.add_to_sites_yaml(site_name, url)

        print(f"\n{'='*60}")
        print(f"🎉 完了！")
        print(f"{'='*60}")
        print(f"ファイル: {saved_path}")

        return True


def main():
    """メイン処理"""
    print("=" * 60)
    print("🎨 DESIGN.md 自動生成ツール")
    print("=" * 60)
    print("\nWebサイトのURLを入力すると、自動的にDESIGN.mdを生成します")
    print("終了するには 'quit' または 'exit' を入力してください\n")

    generator = DesignMDGenerator()

    while True:
        try:
            # URL入力
            url = input("\n🌐 WebサイトのURL >>> ").strip()

            # 終了コマンド
            if url.lower() in ["quit", "exit", "q"]:
                print("\n👋 終了します")
                break

            # 空入力をスキップ
            if not url:
                continue

            # DESIGN.mdを生成
            success = generator.process_url(url)

            if success:
                print("\n✅ 次のURLを入力するか、'quit'で終了してください")
            else:
                print("\n❌ 処理に失敗しました。別のURLを試してください")

        except KeyboardInterrupt:
            print("\n\n👋 終了します")
            break
        except Exception as e:
            print(f"\n❌ エラーが発生しました: {e}")
            print("別のURLを試してください")


if __name__ == "__main__":
    main()
