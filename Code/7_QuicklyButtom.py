
# 建立快速按鍵

# 以用戶身分發訊息
textQuickReplyButton = QuickReplyButton(
    action=MessageAction(
        label="發送文字消息", 
        text="text2"
    )
)

# 點擊後，彈跳出選擇時間之視窗
# DatetimePickerAction
# 可以傳隱藏資訊 -> 後續選擇只用
# mode 給用戶輸入天數
dateQuickReplyButton = QuickReplyButton(
    action=
{
        "type":"datetimepicker",
        "label":"時間選擇",
        "data":"data3",                       
        "mode":"date"
    }
)


# 將按鍵包起來

quickReplyList = QuickReply(
    items = [textQuickReplyButton, dateQuickReplyButton]
)

# 將quickReplyList放在TextSendMessage中， 在家到回應字典中
quick_reply_text_send_message = TextSendMessage(text='發送問題給用戶，請用戶回答', quick_reply=quickReplyList)
template_message_dict['@reply']=quick_reply_text_send_message