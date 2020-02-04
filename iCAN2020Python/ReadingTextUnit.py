import subprocess
import winsound

def jtalk(t):
    # depend on your install folder
    OPENJTALK_BINPATH = 'c:/open_jtalk/bin'
    OPENJTALK_DICPATH = 'c:/open_jtalk/bin/dic'
    OPENJTALK_VOICEPATH = 'c:/open_jtalk/bin/nitech_jp_atr503_m001.htsvoice'
    open_jtalk=[OPENJTALK_BINPATH + '/open_jtalk.exe']
    mech=['-x',OPENJTALK_DICPATH]
    htsvoice=['-m',OPENJTALK_VOICEPATH]
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)

    # convert text encoding from utf-8 to shitf-jis
    c.stdin.write(t.encode('shift-jis'))
    c.stdin.close()
    c.wait()

    # play wav audio file with winsound module
    winsound.PlaySound('open_jtalk.wav', winsound.SND_FILENAME)

if __name__ == '__main__':
    print("独立挙動モード")
    jtalk(u'ユニットとしては動いてません、独立挙動モードです')
