
# 連接雲端硬碟
from google.colab import drive
drive.mount('/content/drive')

# 必要套件
!pip install line-bot-sdk flask flask-ngrok

# 套件載入

from flask import Flask, request, abort, jsonify
import json

# 外部連結自動生成套件
from flask_ngrok import run_with_ngrok

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

# 引用無效簽章錯誤
from linebot.exceptions import (
    InvalidSignatureError
)

# 主程序建立
app = Flask(__name__,static_url_path = "/material" , static_folder = "./material/")
run_with_ngrok(app)

# 連結Line
line_bot_api = LineBotApi("line token")
handler = WebhookHandler("line secret")

# 初始介面建立
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print(body)

    # 記錄用戶log
    f = open("/content/drive/MyDrive/line bot/ai-event.log", "a")
    f.write(body)
    f.close()

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    
# 程式執行
app.run()

