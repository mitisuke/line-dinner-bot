from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ["nyoBdCS2/+FW2Rs698IvE4W0+eT8anxRPzPDUFzj8IXcH0PsvrEja6xfBEptst2avfbmD2o7qm4GjgxEVdAgJzcu5vSIegFpAcJwTLlFdxqZIZWOAOhLAY1JGHYmoVB6DYWKx4bI5YuMI3D7i7XdwwdB04t89/1O/w1cDnyilFU="])
handler = WebhookHandler(os.environ["2962b0e0ad13d4d36c967f0718ee7fac"])

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    reply = "「はい」か「いいえ」でお願いします！" if msg not in ["はい", "いいえ"] else f"ご回答ありがとうございます（{msg}）"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

if __name__ == "__main__":
    app.run()