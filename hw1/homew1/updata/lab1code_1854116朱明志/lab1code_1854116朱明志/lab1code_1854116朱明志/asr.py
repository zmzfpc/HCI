import pyaudio
#from recorder import Recorder
from PyQt5.QtCore import QThread, pyqtSignal
from aip import AipSpeech

APP_ID = '24156401'
API_KEY = 'E0IoR5KgwaxNfBdLWsimRi34'
SECRET_KEY = 'ZfmpKut46SnGap4VgvXozy5u5TdnAnQB'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def baidu_asr(wave, format, rate):
        return client.asr(wave, format, rate, {'dev_pid': 1537, })

class AsrThread(QThread):
    do_nothing = lambda *_, **__: None

    # A signal needs to be defined on class level
    ok_signal = pyqtSignal(str)
    err_signal = pyqtSignal(dict)

    

    def __init__(self, on_success, on_error=print):
        super(AsrThread, self).__init__()
        # self.recorder = "1.m4a"

        self.ok_signal.connect(
            on_success if on_success else AsrThread.do_nothing)
        self.err_signal.connect(on_error if on_error else AsrThread.do_nothing)

        self.run = self.do_asr

    def do_asr(self):
        wav = "1_new_1.wav"
        with open(wav, 'rb') as speech_file:
            speech_data = speech_file.read()
        res = baidu_asr(speech_data, 'wav', 16000)
        print(res)
        if res['err_msg'] == 'success.':
            self.ok_signal.emit(' '.join(res['result']))
        else:
            self.err_signal.emit(
                {'err_no': res['err_no'], 'err_msg': res['err_msg']})


if __name__ == '__main__':
    thread = AsrThread(print, None)
    thread.start()
