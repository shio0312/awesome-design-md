#!/bin/bash
# DESIGN.md 自動更新ラッパースクリプト
# launchd から呼び出される

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_FILE="$SCRIPT_DIR/auto_update.log"

echo "===== $(date '+%Y-%m-%d %H:%M:%S') =====" >> "$LOG_FILE"

cd "$SCRIPT_DIR"
"$SCRIPT_DIR/venv/bin/python3" "$SCRIPT_DIR/update_design_auto.py" >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

# 結果を macOS 通知で知らせる
FAILED=$(grep "❌ 失敗:" "$LOG_FILE" | tail -1)
SUCCESS=$(grep "✅ 成功:" "$LOG_FILE" | tail -1)

if [ $EXIT_CODE -eq 0 ]; then
    osascript -e "display notification \"$SUCCESS\" with title \"DESIGN.md 更新完了\" sound name \"Glass\""
else
    FAILED_SITES=$(awk '/失敗したサイト:/{found=1; next} found && /^  - /{print $2} found && !/^  - /{found=0}' "$LOG_FILE" | tail -5 | tr '\n' '、')
    osascript -e "display notification \"更新できなかったサイト: ${FAILED_SITES}手動確認をお願いします\" with title \"DESIGN.md 一部更新失敗\" sound name \"Basso\""
fi

echo "exit code: $EXIT_CODE" >> "$LOG_FILE"
