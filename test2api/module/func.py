from linebot.models import MessageEvent ,TextSendMessage , ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction, URITemplateAction, PostbackTemplateAction,ImagemapSendMessage,BaseSize,MessageImagemapAction,ImagemapArea,URIImagemapAction,CarouselColumn,CarouselTemplate,ImageCarouselColumn,ImageCarouselTemplate
from linebot import  LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError ,LineBotApiError
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse , HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


def sendText(event):
	try:
		message = TextSendMessage(
			text = "因為今年疫情緣故，豆干節詳細舉辦日期尚未得知，以下為去年活動懶人包供參考：\n 網址：https://jfsblog.com/blog/post/daxi-bean-curd-festival"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))
def sendText2(event):
	try:
		message = TextSendMessage(
			text = "因為今年疫情緣故，活動延期，詳細舉辦日期尚未得知，以下為去年活動懶人包供參考：\n 網址：https://jfsblog.com/blog/post/taoyuan-balloon-festival"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))

def sendImage(event):
	try:
		message = ImageSendMessage(
			original_content_url="https://i.imgur.com/FutqcMi.jpg",
			preview_image_url="https://i.imgur.com/FutqcMi.jpg"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendImage2(event):
	try:
		message = ImageSendMessage(
			original_content_url="https://i.imgur.com/dazZhFz.jpg",
			preview_image_url="https://i.imgur.com/dazZhFz.jpg"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendStick(event):
	try:
		message = StickerSendMessage(
			package_id='1',
			sticker_id='2'
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendMulti(event):
	try:
		message = [
				TextSendMessage(text="【金師獎】中原資管105級謝師宴 🎉 \n:::::::::::::::::::::::::::::::::::::::::::::::\n活動時間：109/6/17(三) 晚上17:30 報到進場 ； 18:00 開始\n活動地點：南方莊園渡假飯店 (桃園市中壢區樹籽路8號) 中原過去交通約20-25分鐘，備免費停車場\n價格：750-850 / 人（將於統計人數後公告確定金額於各班群組）\n繳費方式與時間待金額確定會一併公告，請同學務必注意！！\n用餐內容：自助Buffet\n🎁當天有抽獎活動哦！獎品豐富!\n之後會再讓大家安排座位跟自己的好朋友同一桌!!\n快來參加謝師宴、吃大餐、抽好禮\n\n報名截止時間：6/3(三)11:59分"),
				TextSendMessage(text="※ 本次謝師宴主題為【金師獎】\n※ 服裝方面，請著「正式服裝」出席\n⚠️ 請勿穿著拖鞋入場\n❗️ 此表單填寫完畢即視為確定出席\n \n※ 待統計完人數確定每人繳付金額後，無論晚到還是缺席都需要負擔「完整出席餐費」！\n\n甲班負責人聯絡電話：蔡宜真 0926-108-965\n乙班負責人聯絡電話：涂益誠 0934-258-528\n\n有任何疑問都歡迎直接聯繫負責人\n感謝配合 !! ")
		]
		
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))
def sendPosition(event):
	try:
		message = [
			LocationSendMessage(title='桃園市大溪區',address='335桃園市大溪區',latitude='24.8709613',longitude='121.2306069'),
			TextSendMessage(text="大溪區爲中華民國桃園市的一個市轄區，境內有大漢溪，因而得名。大溪區原為復興區的木材輸出門戶，以大漢溪爲河運管道。雖然現在河運已經不再，但當地昔日的渡船頭仍然保存，大溪爲北橫公路的入口端，因擁有豐富的觀光資源，桃園市政府持續推展生態休閒遊憩東都心之重點發展區。")
		]
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))
def sendQuickreply(event):
	try:
		message = TextSendMessage(
			text = "選擇你最愛的程式語言吧",
			quick_reply=QuickReply(
				items=[
					QuickReplyButton(
						action=MessageAction(label="Python",text="Python")
					),
					QuickReplyButton(
						action=MessageAction(label="Java",text="Java")
					),
					QuickReplyButton(
						action=MessageAction(label="C#",text="C#")
					),
					QuickReplyButton(
						action=MessageAction(label="Basic",text="Basic")
					),
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))
def sendButton(event):  #按鈕樣版
    # try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ButtonsTemplate(
                thumbnail_image_url='https://lh3.googleusercontent.com/proxy/mAPV6VIFrXqWaX4uzwu-qfk2QSg4g7LkE2hhEU7SGW_tbJJ-k1gTb9B4YYcYGQk9yNLOwn560yrLiTMLhBRoKQm_voje3g',  #顯示的圖片
                title='大溪近期經典活動',  #主標題
                text='請點選選項以獲取更多資訊：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='2020大溪豆干節(延期)',
                        text='@傳送大溪豆乾活動'
                    ),
                    MessageTemplateAction(  #開啟網頁
                        label='2020石門水庫熱氣球嘉年華(延期)',
                        text='@傳送石門水庫熱氣球活動'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    # except:
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPizza(event):
    try:
        message = TextSendMessage(
            text = '感謝您購買披薩。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_buy(event, backdata):  #處理Postback
    try:
        text1 = '感謝您購買披薩，'
        text1 += '我們將盡快為您製作。'
        message = TextSendMessage(  #傳送文字
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImgmap(event):
	#try:
		image_url = 'https://i.imgur.com/Yz2yzve.jpg'
		imgwidth = 1040
		imgheight = 300
		message = ImagemapSendMessage(
			base_url=image_url,
			alt_text= "圖片地圖範例",
			base_size=BaseSize(height=imgheight, width=imgwidth),
			actions=[
				MessageImagemapAction(
					text="你點選了紅色區域!",
					area=ImagemapArea(
						x=0,
						y=0,
						width=imgwidth*0.25,
						height=imgheight
					)
				),
				URIImagemapAction(
					link_url='https://www1.cycu.edu.tw/',
					area=ImagemapArea(
						x=imgwidth*0.75,
						y=0,
						width=imgwidth*0.25,
						height=imgheight
					)
				),
			]
		)
		line_bot_api.reply_message(event.reply_token, message)
	#except:
	#	line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendCarousel(event):
	try:
		message = TemplateSendMessage(
			alt_text='轉盤樣板',
			template=CarouselTemplate(
				columns=[
					CarouselColumn(
						thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipNnQOa2A8RTG1GJn8iYAwAVrZt0lcQofOFoUGdc=w928-h520-n-k-no',
						title='大溪老街',
						text='請點選欲了解的項目：',
						actions=[
							URITemplateAction(
								label='維基百科',
								uri='https://zh.wikipedia.org/zh-tw/%E5%A4%A7%E6%BA%AA%E8%80%81%E8%A1%97'
							),
							URITemplateAction(
								label='搜尋結果',
								uri='https://www.google.com/search?q=大溪老街&stick=H4sIAAAAAAAAAONgFuLUz9U3MC5Jyi5S4gYxDQ0LTS1KDLUUs5Ot9HPykxNLMvPz4AyrxJKSosRkELMYAM4Ux8U9AAAA&ved=0CBMQ4mhqFwoTCOD8lv2DmuoCFQAA'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://lh5.googleusercontent.com/proxy/DmoAcQkorYFiFBWYpjcZ0ojdflqMarZY22xByDVYAlq0x4YzDY7kFZuBObFN509dUKEzLNQCWkB_vuLoXXJSZnI9PwJbN8lOnN64WvO4-BvtUYiAwIheY1getH0iX-2TZa6G_qowRkch56Ysf6rJaqL3YJyx9358IhyXWTJA912A=w928-h520-n-k-no',
						title='石門水壩',
						text='請點選欲了解的項目：',
						actions=[
							URITemplateAction(
								label='維基百科',
								uri='https://zh.wikipedia.org/zh-tw/%E7%9F%B3%E9%96%80%E6%B0%B4%E5%BA%AB_(%E8%87%BA%E7%81%A3)'
							),
							URITemplateAction(
								label='搜尋結果',
								uri='https://www.google.com/search?sxsrf=ALeKk00xMaGNpe6vQ5UveW8naztqMuG45Q%3A1592988817966&ei=kRTzXuSxOuLEmAXt7b6ICg&q=%E7%9F%B3%E9%96%80%E6%B0%B4%E5%A3%A9&oq=%E7%9F%B3%E9%96%80%E6%B0%B4%E5%A3%A9&gs_lcp=ChNtb2JpbGUtZ3dzLXdpei1zZXJwEAwyBAgjECcyBQgAEM0CMgUIABDNAlAAWABgnxJoAHAAeACAAcYBiAHGAZIBAzAuMZgBAA&sclient=mobile-gws-wiz-serp'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipM9Qi7wsPxWLoP_Xb4kgGdNH5edl98RKB3rCvXt=w928-h520-n-k-no',
						title='慈湖陵寢',
						text='請點選欲了解的項目：',
						actions=[
							URITemplateAction(
								label='維基百科',
								uri='https://zh.wikipedia.org/zh-tw/%E6%85%88%E6%B9%96%E9%99%B5%E5%AF%A2'
							),
							URITemplateAction(
								label='搜尋結果',
								uri='https://www.google.com/search?sxsrf=ALeKk00yTMqLvInr27tczdLueA-_u1-Onw%3A1592988977360&ei=MRXzXofHFY2Lr7wPlImx0AM&q=%E6%85%88%E6%B9%96%E9%99%B5%E5%AF%9D&oq=%E6%85%88%E6%B9%96&gs_lcp=ChNtb2JpbGUtZ3dzLXdpei1zZXJwEAEYATICCAAyAggAMgQIABBDMgIIADICCAAyAggAMgQIABBDMgIIADoECAAQRzoECCMQJzoHCAAQsQMQQzoFCAAQsQM6BwgjEOoCECdQoQNYoBlgkCJoAXABeACAAbcBiAHGApIBAzIuMZgBAKABAbABDw&sclient=mobile-gws-wiz-serp'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipMhtBz-0MeLy0NTknkuix014hdNaCpQALVS0OR4=w408-h306-k-no',
						title='大溪花海',
						text='請點選欲了解的項目：',
						actions=[
							URITemplateAction(
								label='官方網站',
								uri='http://www.tasheeblmn.com.tw/'
							),
							URITemplateAction(
								label='搜尋結果',
								uri='https://www.google.com/search?q=%E5%A4%A7%E6%BA%AA%E8%8A%B1%E6%B5%B7&rlz=1C5CHFA_enTW898TW898&oq=%E5%A4%A7%E6%BA%AA%E8%8A%B1%E6%B5%B7&aqs=chrome.0.69i59j0l5j69i61l2.2788j0j4&sourceid=chrome&ie=UTF-8'
							)
						]
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendCarouselImg(event):
	#try:
		message = TemplateSendMessage(
			alt_text='圖片轉盤樣板',
			template=ImageCarouselTemplate(
				columns=[
					ImageCarouselColumn(
						image_url='https://www.alberthsieh.com/wp-content/uploads/flickr/24794130670_d49b2fee3b_b.jpg',
						action=MessageTemplateAction(
							label='大溪豆乾',
							text="想吃！"
						)
					),
					ImageCarouselColumn(
						image_url='https://www.alberthsieh.com/wp-content/uploads/flickr/24462870313_336a20c273_b.jpg',
						action=MessageTemplateAction(
							label='月光餅（地瓜餅）',
							text="想吃！"
						)
					),
					ImageCarouselColumn(
						image_url='https://www.alberthsieh.com/wp-content/uploads/flickr/25063404956_2e3254b4c8_b.jpg',
						action=MessageTemplateAction(
							label='麥芽花生糖',
							text="想吃！"
						)
					),
					ImageCarouselColumn(
						image_url='https://www.alberthsieh.com/wp-content/uploads/flickr/24971569902_218b62be31_b.jpg',
						action=MessageTemplateAction(
							label='原味黃金乳酪球',
							text="想吃！"
						)
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,message)
	#except:
	#	line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
