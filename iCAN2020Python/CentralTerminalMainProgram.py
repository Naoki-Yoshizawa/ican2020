import GmailSendUnit as GSU
import LineNotifyUnit as LNU

TO_ADR = 'naoki.4438.work@gmail.com'
SBJ = '侵入センサー感知通知テスト'
BOD = '侵入センサーに感知がありました、直ちに確認してください(これは試験配信です)'

GSU.gms_unit_do(TO_ADR, SBJ, BOD)
