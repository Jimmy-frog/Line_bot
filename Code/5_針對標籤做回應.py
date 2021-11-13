


# event.postback.data == 設定的標籤
# event.postback.data.find('標籤') 有 = 0, 沒有 = -1


@handler.add(PostbackEvent)
def handle_post_message(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)
    # 法一
    if (event.postback.data.find('Data1')== 0):
        with open("user_profile_business.txt", "a") as myfile:
            myfile.write(json.dumps(vars(user_profile),sort_keys=True))
            myfile.write('\n')
            line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(
                    text='請稍待，會有專人與您聯繫'
                )
            )
    # 法二
    elif (event.postback.data == 'Data2'):
        with open("user_profile_tutorial.txt", "a") as myfile:
            myfile.write(json.dumps(vars(user_profile),sort_keys=True))
            myfile.write('\n')
            line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(
                    text='請稍待，我們會派專家與您聯繫'
                )
            )
    else:
        pass