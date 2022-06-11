from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('QJ5/pXzbooViFJMks7C/tIVG+Rt5DDBQMQLA/O7dmpkWrpZttC1R/ZR8UOH2Z05wosrXE95FppZCraEK3FqhYf2U1h9v7mfmYkHjnozzCRz2Lk+YOWup+5kX3PS0VEUIFEY4NsDY5m5smEKymfEV5AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7b13ada46090e324f5ac4cb7bfeb3c32')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎?'))


if __name__ == "__main__":
    app.run()