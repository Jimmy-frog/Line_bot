# 套件載入
from linebot.models import(
    TextSendMessage, ImageSendMessage,StickerSendMessage,
    TemplateSendMessage,ButtonsTemplate,ConfirmTemplate,
    CarouselTemplate,CarouselColumn,PostbackTemplateAction,
    MessageTemplateAction,URITemplateAction,VideoSendMessage,
    LocationSendMessage,ImageCarouselTemplate,ImageCarouselColumn
)

"""
建立回應訊息

1. 文字
2. 貼圖
3. 圖片
4. 影片
5. 語音
6. 地理位置
7. tenplate

"""

# 文字回覆
emoji = [{
        "index": 0,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "001"
    }]
reply_message = TextSendMessage(text='$ 喵喵喵', emojis=emoji)

# 貼圖回覆
reply_sticker = StickerSendMessage(package_id=446, sticker_id=1988)

# 圖片回覆
reply_image = ImageSendMessage(original_content_url='https://www.mirrormedia.com.tw/assets/images/20200515182647-44d2dc790fce36e05cd131b09da09bd6-mobile.jpg', preview_image_url='https://storage.googleapis.com/ai-class-python/U9710185273c3f40f4ffc5b892901c95d/user_pic.png')

# 影像

#reply_video = VideoSendMessage(original_content_url='https://storage.googleapis.com/ai-class-python/test.mp4', preview_image_url='https://storage.googleapis.com/ai-class-python/U9710185273c3f40f4ffc5b892901c95d/user_pic.png')

# 地理位置
reply_loc =LocationSendMessage(title='my location', address='Tainan', latitude=22.994821, longitude=120.196452)

# Buttons Template

buttons_template = TemplateSendMessage(
    alt_text='Buttons Template',
    template=ButtonsTemplate(
        title = "test",
        text = "test",
        thumbnail_image_url = "https://www.mirrormedia.com.tw/assets/images/20200515182647-44d2dc790fce36e05cd131b09da09bd6-mobile.jpg",
        actions =[
            {
                "type": "postback",
                "label": "這可以貼標籤",
                "text": "這可以回應給用戶",
                "data": "Data2"
            },
            {
                "type": "uri",
                "label": "這是相機",
                "uri":"https://line.me/R/nv/camera/"
            },
            {
                "type": "uri",
                "label": "這是打開個人頁面",
                "uri":"https://line.me/R/nv/profile"
            },
            {
                "type": "message",
                "label": "單純回應訊息",
                "text":"good"
            }                 
        ]))

Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title = "got it",
                text = " 你要睡覺嗎 ",
                actions=[
                      {
                        "type": "postback",
                        "label": "好歐",
                        "text": "我會乖乖的",
                        "data": "Data1"
                      },
                      {
                        "type": "message",
                        "label": "我鼻要",
                        "text": "咬我啊 喵~~",
                      }
                    ]))

Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://www.mirrormedia.com.tw/assets/images/20200515182647-44d2dc790fce36e05cd131b09da09bd6-mobile.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    {
                      "type":"postback",
                      "label":'postback1',
                      "text":'postback text1',
                      "data":'action=buy&itemid=1'
                    },
                    {
                      "type":"message",
                      "label":'message1',
                      "text":'message text1'
                    },
                    {
                      "type":"uri",
                      "label":'uri1',
                      "uri":'http://example.com/1'
                    }
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://www.mirrormedia.com.tw/assets/images/20200515182647-44d2dc790fce36e05cd131b09da09bd6-mobile.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    {
                      "type":"postback",
                      "label":'postback1',
                      "text":'postback text1',
                      "data":'action=buy&itemid=1'
                    },
                    {
                      "type":"message",
                      "label":'message1',
                      "text":'message text1'
                    },
                    {
                      "type":"uri",
                      "label":'uri1',
                      "uri":'http://example.com/1'
                    }
                ]
            )
        ]
    )
    )
						
Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://www.mirrormedia.com.tw/assets/images/20200515182647-44d2dc790fce36e05cd131b09da09bd6-mobile.jpg',
                action=
                      {
                        "type":"postback",
                        "label":'postback1',
                        "text":'postback text1',
                        "data":'action=buy&itemid=1'
                      }
                    
            ),
            ImageCarouselColumn(
                image_url='https://www.mirrormedia.com.tw/assets/images/20200515182647-44d2dc790fce36e05cd131b09da09bd6-mobile.jpg',
                action=
                      {
                        "type":"postback",
                        "label":'postback2',
                        "text":'postback text2',
                        "data":'action=buy&itemid=2'
                      }
                    
                )
        ]
    )
    )
