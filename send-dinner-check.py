import os
from linebot import LineBotApi
from linebot.models import TextSendMessage

# LINEチャネルアクセストークン（環境変数から読み込む）
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

# LineBotAPIの初期化
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

# 送信するユーザーID一覧（友達になったユーザーの userId）
USER_IDS = [
    "Uxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # ←実際のuserIdに置き換えてください
    "Uyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
]

# 送信するメッセージ
message = TextSendMessage(text="今日の夕飯が必要ですか？（はい / いいえ）")

# 各ユーザーにメッセージを送信
for user_id in USER_IDS:
    try:
        line_bot_api.push_message(user_id, message)
        print(f"メッセージを送信しました: {user_id}")
    except Exception as e:
        print(f"送信失敗: {user_id} - {e}")