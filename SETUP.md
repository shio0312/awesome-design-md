# 自分用セットアップガイド

このリポジトリは **デザインmdジェネレーター** の個人管理用 fork です。
新しい端末で使い始めるときはこの手順に従ってください。

---

## 新しい端末でのセットアップ

### 1. リポジトリをクローン

ターミナルを開いて以下を貼り付けて実行：

```bash
git clone https://github.com/shio0312/awesome-design-md.git
cd awesome-design-md
bash setup.sh
```

### 2. API キーを入力

セットアップの途中で「`.env` ファイルに API キーを入力してください」と表示されたら：

1. Finder で `awesome-design-md` フォルダを開く
2. `Cmd + Shift + .` で隠しファイルを表示
3. `.env` をテキストエディタで開く
4. `your_api_key_here` の部分を実際のキーに書き換えて保存

> API キーの確認・発行: https://console.anthropic.com/

### 3. セットアップを完了

```bash
bash setup.sh
```

「セットアップ完了！」と表示されれば OK。

---

## 日常的な使い方

**基本的に何もしなくて OK。** 毎月1日 9:00 に自動更新されます。

| やること | 方法 |
|---------|------|
| デザインのトンマナを検討したい | Claude Code に「〇〇みたいなデザインで DESIGN.md 作って」と伝える |
| 月次通知が「失敗」だった | Claude Code に「〇〇の DESIGN.md 更新して」と伝える |
| 今すぐ特定サイトを更新したい | Claude Code に「〇〇の DESIGN.md 今すぐ更新して」と伝える |

---

## ファイル構成

```
awesome-design-md/
├── design-md/          # 生成された DESIGN.md ファイル群
├── sites.yaml          # 管理対象サイト一覧（auto_update: false = 自動更新除外）
├── suggest_design.py   # 新規 DESIGN.md 生成ツール
├── update_design.py    # 既存 DESIGN.md 手動更新ツール
├── update_design_auto.py # 自動更新ツール（launchd から呼ばれる）
├── run_auto_update.sh  # 自動更新ラッパー（通知付き）
├── setup.sh            # セットアップスクリプト
└── .env                # API キー（Git 管理外・各端末で個別設定）
```

---

## 参考サイトを新しく追加したいとき

Claude Code に以下のように伝えるだけでOKです：

> 「〇〇（URL）を参考サイトとして追加して」

Claude が以下を自動でやります：
1. `sites.yaml` に追記
2. `suggest_design.py` で DESIGN.md を生成
3. GitHub に push

---

## 自動更新から外しているサイト

以下は bot ブロックでタイムアウトするため手動更新対象：

- Claude (claude.ai)
- Figma (figma.com)
- Notion (notion.so)
- Stripe (stripe.com)

月次通知で案内が来たら Claude Code に更新を依頼してください。
