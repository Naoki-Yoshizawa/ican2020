import DIF_LineNotify

bot = DIF_LineNotify.LINENotifyBot(access_token='VQOjC4EMK6WL0QsAWiw0Fyb5pu155yjpHMG5gov5RVz') #アクセストークンは自分のを入力

bot.send(
    message='Write Your Message', #ここは文章に関する記述
    #image='test.png',  # png or jpg これは画像の送信、画像が無いときはコメントアウトすること
    sticker_package_id=1, #ここからはスタンプの送信についての記述
    sticker_id=13,
    )
