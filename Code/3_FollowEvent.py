

# 告知handler，如果收到FollowEvent，則做下面的方法處理
@handler.add(FollowEvent)
def reply_text_and_get_user_profile(event):
    
    # 取出消息內User的資料
    user_profile = line_bot_api.get_profile(event.source.user_id)
      
     # 將用戶資訊存在檔案內
    with open("/content/drive/MyDrive/line bot/users.txt", "a") as myfile:
        myfile.write(json.dumps(vars(user_profile),sort_keys=True))
        myfile.write('\n')
    
    # 回覆文字消息與圖片消息
    line_bot_api.reply_message(
        event.reply_token,
        [
          # 這裡面可以放各項reply_message
          # 最多只能放四個
          TextSendMessage(text='下面為各項回應訊息範例')
        ]
    )
