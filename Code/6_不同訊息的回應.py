

# 針對回應訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    if(event.message.text.find('@')!= -1):
        line_bot_api.reply_message(
        event.reply_token,
        template_message_dict.get(event.message.text)
        )
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="講人話")
        )

# 針對圖片訊息
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
  line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="好醜")
        )