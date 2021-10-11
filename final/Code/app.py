import sys
import difflib
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, pyqtSlot
from app_ui import Ui_Dialog
from asr import AsrThread
import main


def play_music():
    print(1)


def open_file():
    print(1)


def search(keyword):
    print(1)




def open_browser():
    print(1)
    
def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


class myWindow(QtWidgets.QDialog):
    def __init__(self):
        super(myWindow, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.asr_thread = AsrThread(self.do_sth, self.on_err)

        '''自动触发识别'''
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.start_asr)
        self.timer.start()
        self.start_asr()

    @pyqtSlot()
    def on_voiceFig_clicked(self):
        '''手动触发识别'''
        self.asr_thread.terminate()
        self.asr_thread = AsrThread(self.do_sth, self.on_err)
        self.start_asr()

    @pyqtSlot()
    def start_asr(self):
        self.timer.stop()
        self.ui.movie.start()
        self.ui.label_6.setText('小思在听你说哦！')
        self.asr_thread.start()

    def do_sth(self, text):
        self.ui.movie.stop()
        self.ui.movie.jumpToFrame(0)
        self.ui.label_6.setText(text or '小思没听清能再说一遍嘛？')
        print(text)
        # try:
        #     if '音乐' in text or '来点' in text:
        #         play_music()
        #     elif '文本' in text or '记事本' in text:
        #         open_file()
        #     elif '浏览器' in text:
        #         open_browser()
        #     elif '搜索' in text:
        #         keyword = text[text.index('搜索') + 2:]
        #         search(keyword)
        #     else:
        #         self.ui.label_6.setText('小思没听清能再说一遍嘛？')
        # except:
        #     self.ui.label_6.setText('小思没听清能再说一遍嘛？')
        try:
            if '前' in text:
                main.front_clicked()
            elif '后' in text:
                main.behind_clicked()
            elif '上' in text:
                main.up_clicked()
            elif '下' in text:
                main.down_clicked()
            elif '左' in text:
                main.left_clicked()
            elif '右' in text:
                main.right_clicked()
        except:
            self.ui.label_6.setText('小思没听清能再说一遍嘛？')
        self.timer.setInterval(5000)
        self.timer.start()

    def on_err(self, err):
        self.timer.start()
        self.ui.movie.stop()
        self.ui.movie.jumpToFrame(0)
        self.ui.label_6.setText('小思没听清能再说一遍嘛？')
        print(err)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    instance = myWindow()
    instance.show()
    sys.exit(app.exec())

# def create():
#     app = QtWidgets.QApplication(sys.argv)
#     instance = myWindow()
#     instance.show()
#     sys.exit(app.exec())