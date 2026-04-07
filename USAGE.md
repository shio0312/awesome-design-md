# DESIGN.md 自動生成ツール - 使い方

## 概要

このツールは、WebサイトのURLを入力するだけで、自動的にDESIGN.mdファイルを生成する対話型スクリプトです。

## セットアップ

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. Playwright ブラウザのインストール

```bash
playwright install chromium
```

### 3. Anthropic API キーの設定

1. [Anthropic Console](https://console.anthropic.com/) でAPIキーを取得
2. `.env` ファイルを作成:

```bash
cp .env.example .env
```

3. `.env` ファイルを編集してAPIキーを設定:

```
ANTHROPIC_API_KEY=sk-ant-your-actual-api-key-here
```

## 使い方

### 基本的な使い方

スクリプトを実行します:

```bash
python suggest_design.py
```

対話形式でURLを入力します:

```
🎨 DESIGN.md 自動生成ツール
============================================================

Webサイトのurlを入力すると、自動的にDESIGN.mdを生成します
終了するには 'quit' または 'exit' を入力してください

🌐 WebサイトのURL >>> https://example.com
```

### 処理の流れ

1. **URL入力**: WebサイトのURLを入力
2. **ページ取得**: Playwrightでページにアクセスし、HTML/CSSを解析
3. **DESIGN.md生成**: Claude APIでデザインシステムを分析・文書化
4. **ファイル保存**: `design-md/[site-name]/DESIGN.md` に保存

### 複数サイトの処理

スクリプトは対話型なので、連続して複数のサイトを処理できます:

```
🌐 WebサイトのURL >>> stripe.com
✅ 完了！

🌐 WebサイトのURL >>> vercel.com
✅ 完了！

🌐 WebサイトのURL >>> quit
👋 終了します
```

## 出力例

入力: `https://stripe.com`

出力ディレクトリ構造:
```
design-md/
└── stripe.com/
    ├── DESIGN.md
    └── README.md
```

### DESIGN.mdの内容

以下のセクションが自動生成されます:

1. **Visual Theme & Atmosphere** - デザイン哲学と全体的な雰囲気
2. **Color Palette & Roles** - カラーパレットと役割
3. **Typography Rules** - タイポグラフィルール
4. **Component Stylings** - コンポーネントのスタイル
5. **Layout Principles** - レイアウト原則
6. **Depth & Elevation** - 奥行きと立体感
7. **Do's and Don'ts** - 推奨事項と禁止事項
8. **Responsive Behavior** - レスポンシブ対応
9. **Agent Prompt Guide** - AIエージェント向けガイド

## トラブルシューティング

### `ANTHROPIC_API_KEY`エラー

```
エラー: ANTHROPIC_API_KEYが設定されていません
```

**解決方法**: `.env`ファイルが正しく作成され、有効なAPIキーが設定されているか確認してください。

### ページ取得エラー

```
❌ エラー: Timeout 30000ms exceeded
```

**原因**:
- ネットワーク接続の問題
- サイトが重すぎて読み込みに時間がかかる
- サイトがBot検出している

**解決方法**:
- 安定したネットワーク環境で実行
- より軽量なページで試す
- 別のサイトで試す

### Claude API エラー

```
❌ Claude API エラー: rate_limit_error
```

**解決方法**: APIレート制限に達しています。少し時間をおいてから再実行してください。

## 既存DESIGN.mdの更新

サイトのデザインが変更された場合、DESIGN.mdを更新できます。

### 手動更新

```bash
python update_design.py
```

対話形式で更新するサイトを選択できます:

```
📋 登録されているサイト一覧:

【AI & Machine Learning】
   1. [✓] Claude              (claude)
   2. [✓] Cohere              (cohere)
   ...

【Developer Tools & Platforms】
   3. [✓] Cursor              (cursor)
   4. [✓] Linear              (linear.app)
   ...

オプション:
  数字    : 指定したサイトを更新
  all     : 全サイトを更新
  auto    : auto_update=true のサイトのみ更新
  quit    : 終了

選択 >>> 1
```

### 自動更新（GitHub Actions）

このリポジトリには週次で自動的にDESIGN.mdをチェック・更新するGitHub Actionsワークフローが含まれています。

#### セットアップ

1. GitHubリポジトリの Settings > Secrets and variables > Actions に移動
2. `ANTHROPIC_API_KEY` という名前でAPIキーを登録

#### 動作

- 毎週日曜日の午前2時（UTC）に自動実行
- `sites.yaml`の`auto_update: true`のサイトを更新
- 変更があれば自動的にPRを作成
- 手動実行も可能（Actions タブから "Auto Update DESIGN.md" ワークフローを実行）

#### 設定ファイル

`sites.yaml` でサイト情報を管理:

```yaml
sites:
  - name: Claude
    folder: claude
    url: https://claude.ai
    category: AI & Machine Learning
    description: Anthropic's AI assistant. Warm terracotta accent, clean editorial layout
    auto_update: true  # 自動更新対象
```

フィールド:
- `name`: サイト名（表示用）
- `folder`: design-md/以下のフォルダ名
- `url`: サイトのURL
- `category`: カテゴリ
- `description`: 簡単な説明
- `auto_update`: 自動更新対象かどうか（true/false）

#### sites.yamlの初期生成

README.mdから既存サイト情報を抽出してsites.yamlを生成できます:

```bash
pip install pyyaml
python generate_sites_yaml.py
```

## 高度な使い方

### カスタムサイト名

デフォルトではドメイン名がサイト名として使用されますが、スクリプトを編集して変更できます:

```python
# suggest_design.py の get_site_name() メソッドを編集
def get_site_name(self, url: str) -> str:
    # カスタムロジックをここに追加
    return "custom-name"
```

### プロンプトのカスタマイズ

`generate_design_md()` メソッド内のプロンプトを編集することで、生成内容をカスタマイズできます。

## 制限事項

- 動的にレンダリングされるSPA（Single Page Application）では、一部のスタイル情報が取得できない場合があります
- 認証が必要なページには対応していません
- 生成されたDESIGN.mdは手動でのレビュー・調整を推奨します

## ライセンス

MIT License
