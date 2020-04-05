import requests

class LINENotifyBot:
    API_URL = 'https://notify-api.line.me/api/notify'
    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(
            self, message,
            image=None, sticker_package_id=None, sticker_id=None,
            ):
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
            }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        r = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
            )

    def send_message_stamp():
        bot = DIF_LineNotify.LINENotifyBot(access_token='VQOjC4EMK6WL0QsAWiw0Fyb5pu155yjpHMG5gov5RVz') #アクセストークンは自分のを入力
        bot.send(
            message='Write Your Message', #ここは文章に関する記述
            sticker_package_id=1, #ここからはスタンプの送信についての記述
            sticker_id=13,
            )

    def send_message_stamp_image():
        bot = DIF_LineNotify.LINENotifyBot(access_token='VQOjC4EMK6WL0QsAWiw0Fyb5pu155yjpHMG5gov5RVz') #アクセストークンは自分のを入力
        bot.send(
            message='Write Your Message', #ここは文章に関する記述
            image='test.png',  # png or jpg これは画像の送信、画像が無いときはコメントアウトすること
            sticker_package_id=1, #ここからはスタンプの送信についての記述
            sticker_id=13,
            )
