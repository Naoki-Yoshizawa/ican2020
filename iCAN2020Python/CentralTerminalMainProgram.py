import time
import GmailSendUnit as GSU
import DIF_LineNotify as DILN

TO_ADR = 'naoki.4438.work@gmail.com'
SBJ = 'プログラムエラー'
BOD = 'プログラムエラー'
LINE = DILN.LINENotifyBot(access_token='VQOjC4EMK6WL0QsAWiw0Fyb5pu155yjpHMG5gov5RVz') #アクセストークンは自分のを入力

setrue = False
entrance = False
veranda = False
window = False

stop = False #プログラム試験用、本番では削除
window = True #プログラム試験用、本番では削除

while stop == False:
    SBJ = ''
    BOD = ''

    if entrance == True:
        SBJ = '玄関'
        BOD = '玄関,'
        setrue = True

    if veranda == True:
        SBJ = str(SBJ) + ' ベランダ'
        BOD = str(BOD) + 'ベランダ,'
        setrue = True

    if window == True:
        SBJ = str(SBJ) + ' 小窓'
        BOD = str(BOD) + '小窓'
        setrue = True

    if setrue == True:
        SBJ = str(SBJ) + 'のセンサーが開閉を検知しました。'
        BOD = str(BOD) + 'の侵入センサーが開閉を検知しました。直ちに状況を確認してください。'
        GSU.gms_unit_do(TO_ADR, SBJ, BOD) #gmail通知送信
        LINE.send(message = str(BOD)) #ライン通知送信

        setrue = False
        entrance = False
        veranda = False
        window = False

    time.sleep(5)
    print("実行中") #プログラム試験用、本番では削除
