#!/bin/bash
# 新しい端末でのセットアップスクリプト
# 実行方法: bash setup.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "===================================="
echo " DESIGN.md ジェネレーター セットアップ"
echo "===================================="

# Python 確認
PYTHON=$(which python3.14 || which python3 || echo "")
if [ -z "$PYTHON" ]; then
    echo "エラー: Python3 が見つかりません。Homebrew でインストールしてください。"
    echo "  /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    echo "  brew install python"
    exit 1
fi
echo "Python: $($PYTHON --version)"

# venv 作成
echo ""
echo "依存パッケージをインストール中..."
cd "$SCRIPT_DIR"
$PYTHON -m venv venv
venv/bin/pip install -r requirements.txt -q
venv/bin/playwright install chromium
echo "インストール完了"

# .env セットアップ
echo ""
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
    echo "【重要】.env ファイルに Anthropic API キーを入力してください:"
    echo "  場所: $SCRIPT_DIR/.env"
    echo "  取得: https://console.anthropic.com/"
    echo ""
    echo "入力後、もう一度このスクリプトを実行してください。"
    exit 0
fi

# APIキー確認
if grep -q "your_api_key_here" "$SCRIPT_DIR/.env"; then
    echo "【重要】.env の API キーがまだ未入力です。"
    echo "  場所: $SCRIPT_DIR/.env"
    exit 1
fi

# launchd 設定（Mac のみ）
echo ""
echo "月次自動更新を設定中..."
PLIST_SRC="$SCRIPT_DIR/com.maedashiori.design-md-update.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/com.maedashiori.design-md-update.plist"

# plist のスクリプトパスをこの端末のパスに書き換え
sed "s|/Users/maedashiori/awesome-design-md|$SCRIPT_DIR|g" "$PLIST_SRC" > "$PLIST_DEST"
launchctl unload "$PLIST_DEST" 2>/dev/null || true
launchctl load "$PLIST_DEST"
echo "設定完了（毎月1日 9:00 に自動更新）"

echo ""
echo "===================================="
echo " セットアップ完了！"
echo "===================================="
