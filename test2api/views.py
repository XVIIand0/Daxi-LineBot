from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse , HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import  LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError ,LineBotApiError
from linebot.models import MessageEvent ,TextSendMessage , ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,TextMessage, PostbackEvent
from .module.func import *
from urllib.parse import parse_qsl
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
	if request.method == 'POST':
		signature = request.META['HTTP_X_LINE_SIGNATURE']
		body = request.body.decode('utf-8')
		print(body)
		try:
			events = parser.parse(body, signature)
		except InvalidSignatureError:
			return HttpResponseForbidden()
		except LineBotApiError:
			return HttpResponseBadRequest()
		for event in events:
			if isinstance(event, MessageEvent):
				if isinstance(event.message, TextMessage):
					mtext = event.message.text
					if mtext == '@按鈕樣板':
					   sendButton(event)
					elif mtext == '@購買披薩':
						sendPizza(event)
					elif mtext == '@圖片地圖':
						sendImgmap(event)
					elif mtext == '@日期時間':
						sendDatetime(event)
					elif mtext =="@傳送大溪豆乾活動":
						sendText(event)
					elif mtext =="@傳送通識活動":
						sendImage(event)
					elif mtext =="@傳送石門水庫熱氣球活動":
						sendText2(event)
					elif mtext =="@傳送貼圖":
						sendStick(event)
					elif mtext =="@金師獎資訊":
						sendMulti(event)
					elif mtext =="@聯絡方式與地址":
						sendPosition(event)
					elif mtext =="@快速選單":
						sendQuickreply(event)
					elif mtext=="@大溪景點":
						sendCarousel(event)
					elif mtext == "@大溪名產":
						sendCarouselImg(event)
					else:
						output = "RRRR 快去買!!!"
						line_bot_api.reply_message(event.reply_token,TextSendMessage(text = output))
			if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
				backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
				if backdata.get('action') == 'buy':
					sendBack_buy(event, backdata)                       
		return HttpResponse()
	else:
		return HttpResponseBadRequest()
    
# def callback(request):
# 	if request.method =='POST':
# 		signature = request.META['HTTP_X_LINE_SIGNATURE']
# 		body = request.body.decode('utf-8')
		
# 		try:
# 			events = parser.parse(body,signature)
# 		except InvalidSignatureError:
# 			return HttpResponseForbidden()
# 		except LineBotApiError:
# 			return HttpResponseBadRequest()
# 		for event in events:		
# 			if isinstance(event , MessageEvent):
# 				mtext = event.message.text 
# 				if mtext =="@傳送文字":
# 					sendText(event)
# 				elif mtext =="@傳送圖片":
# 					sendImage(event)
# 				elif mtext =="@傳送貼圖":
# 					sendStick(event)
# 				elif mtext =="@多項傳送":
# 					sendMulti(event)
# 				elif mtext =="@傳送位置":
# 					sendPosition(event)
# 				elif mtext =="@快速選單":
# 					sendQuickreply(event)
# 				else:
# 					output = "RRRR 我聽不懂!!!"
# 					line_bot_api.reply_message(event.reply_token,TextSendMessage(text = output))
# 		return HttpResponse()
# 	else:
# 		return HttpResponseBadRequest()# Create your views here.
