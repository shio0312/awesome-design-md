#!/bin/bash
# Refero Styles 定期同期ラッパースクリプト
# launchd から2ヶ月に1回（奇数月の1日 9:30）呼び出される

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_FILE="$SCRIPT_DIR/refero_sync.log"

echo "===== $(date '+%Y-%m-%d %H:%M:%S') =====" >> "$LOG_FILE"

cd "$SCRIPT_DIR"

# main を最新にしてから同期する（月次自動更新ジョブと同じリポジトリを共有するため）
git checkout main >> "$LOG_FILE" 2>&1
git pull origin main >> "$LOG_FILE" 2>&1

"$SCRIPT_DIR/venv/bin/python3" "$SCRIPT_DIR/sync_refero_styles.py" --all >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    osascript -e "display notification \"同期に失敗しました。refero_sync.log を確認してください\" with title \"Refero Styles 同期失敗\" sound name \"Basso\""
    echo "exit code: $EXIT_CODE" >> "$LOG_FILE"
    exit $EXIT_CODE
fi

# 変更があればコミットしてプッシュ
if [ -n "$(git status --porcelain)" ]; then
    git add -A >> "$LOG_FILE" 2>&1
    git commit -m "chore: Refero Styles 定期同期 ($(date '+%Y-%m-%d'))" >> "$LOG_FILE" 2>&1
    git push origin main >> "$LOG_FILE" 2>&1
    PUSH_CODE=$?
    if [ $PUSH_CODE -eq 0 ]; then
        osascript -e "display notification \"Refero Styles を同期してプッシュしました\" with title \"Refero Styles 同期完了\" sound name \"Glass\""
    else
        osascript -e "display notification \"コミットは完了しましたがプッシュに失敗しました。手動で git push してください\" with title \"Refero Styles プッシュ失敗\" sound name \"Basso\""
    fi
else
    osascript -e "display notification \"変更はありませんでした\" with title \"Refero Styles 同期完了\" sound name \"Glass\""
fi

echo "exit code: $EXIT_CODE" >> "$LOG_FILE"
