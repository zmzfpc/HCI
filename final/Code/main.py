import sys
from PyQt5.Qt import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
import serial
import Ui_mainwindow
from kinematic import inverse_kin , positive , transpos_kin,calcuInLine
import app
from threading import Thread


posx = 0
posy = 0
posz = 0 
flag  =0 

class Thread_2(QThread):  # 线程2
    def __init__(self):
        super().__init__()

    def run(self,data):
        serial_send_data(data)

class Thread_1(QThread):  # 线程1
    def __init__(self):
        super().__init__()

    def run(self,row):
        tri_move1(row[0],row[1],row[2],ui.lineEdit_ml4.text())
        global flag
        while flag==0:
            print(flag)

class Thread_3(QThread):  # 线程3
    def __init__(self):
        super().__init__()

    def run(self,row):
        tri_move1(row[0],row[1],row[2],ui.lineEdit_mp4.text())
        global flag
        while flag==0:
            print(flag)

def btn_reset_clicked():
    ui.textEdit_cons.append ('please replace in 10 seconds')

    serial_send_data(b'RF()\r\n')




def btn_sta_clicked():
    str1 = "SA({},{},{},{})\r\n".format(\
        ui.lineEdit_sa1.text(),ui.lineEdit_sa2.text(),\
        ui.lineEdit_sa3.text(),ui.lineEdit_sa4.text())
    byte1 = str1.encode("utf-8")
    serial_send_data(byte1)


 

def btn_mol_clicked():
    global posx,posy,posz
    startpos = [posx,posy,posz]
    print(startpos )
    endpos = [float(ui.lineEdit_ml1.text()),\
              float(ui.lineEdit_ml2.text()),\
              float(ui.lineEdit_ml3.text())]
    print (endpos)
    tgts0 = calcuInLine(startpos,endpos)
    tgts = []
    for row in tgts0:
        tpr1,tpr2,tpr3,yyy =inverse_kin(row[0],row[1],row[2],0)
        tgts.append([tpr1,tpr2,tpr3])
    print(tgts)
    for row in tgts:
        flag = 0
        th = Thread_1()
        th.run(row)
     #   tri_move1(row[0],row[1],row[2],ui.lineEdit_ml4.text())

        
        
def tri_move2(t1,t2,t3,sp):
    str1 = "ML(%+05.0f%+05.0f%+05.0f,%s)\r\n"%(t1,t2,t3,sp)
    byte1 = str1.encode("utf-8")
    th = Thread_2()
    th.run(byte1)
    #serial_send_data(byte1)
    
        
def tri_move1(t1,t2,t3,sp):
    str1 = "ML(%+05.0f%+05.0f%+05.0f,%s)\r\n"%(t1,t2,t3,sp)
    byte1 = str1.encode("utf-8")
    th = Thread_2()
    th.run(byte1)
    #serial_send_data(byte1)
    
def tri_move(t1,t2,t3,sp):
    str1 = "ML(%+05.0f%+05.0f%+05.0f,%s)\r\n"%(t1,t2,t3,sp)
    byte1 = str1.encode("utf-8")
    serial_send_data(byte1)

def btn_move_clicked():
    t1,t2,t3,sp=inverse_kin(ui.lineEdit_mo1.text(),ui.lineEdit_mo2.text(),\
    ui.lineEdit_mo3.text(),ui.lineEdit_mo4.text())
    tri_move(t1,t2,t3,sp)

def btn_pow_clicked():
    if ui.pushButton_pow.text() == "PowerOn":
        ui.textEdit_cons.append ('Power on')
        serial_send_data(b'PO()\r\n')
        ui.pushButton_pow.setText("ShutDown")
        #添加线程
        AipThread = Thread(target=app.create)
        AipThread.start()
    elif ui.pushButton_pow.text() == "ShutDown":
        ui.pushButton_pow.setText("PowerOn")
        ui.textEdit_cons.append ('Power off')
        serial_send_data(b'SD()\r\n')
        #删除线程
        AipThread.stop()



def serial_send_data(data):
    if not serial0.isOpen():
        serial0.open()
    if serial0.isOpen():
        #print ('串口已打开')
        #ui.textEdit_cons.append ('串口已打开')
        # data = b'ML(-1800-1800+1800,018)\r\n'    #发送的数据
        serial0.write(data)      #串口写数据
        #print ('You Send Data:',data)
        ui.textEdit_cons.append ('You Send Data:{}'.format(data.decode('utf8')))
        while True:
            data = serial0.read(40)    #串口读40位数据
            if data != b'':
                break
        ui.textEdit_cons.append('receive data is :{}'.format(data.decode('utf8')) )
        #print ('receive data is :',data)
        data = data.decode('utf8')
        global posx,posy,posz 
        posx,posy,posz = transpos_kin (data)
        str1 = "Position x={:.1f};y={:.1f};z={:.1f}".format(posx,posy,posz)
        global flag
        flag = 1
        #print(flag)
        ui.label_pos.setText(str1)
    else:
        ui.textEdit_cons.append ('串口未打开')
        # ('串口未打开')
    
    
    
    #关闭串口
    serial0.close()
    
    if serial0.isOpen():
        ui.textEdit_cons.append ('串口未关闭')
        #print ('串口未关闭')
    else:
        pass
        #ui.textEdit_cons.append ('串口已关闭')
        #print ('串口已关闭')

#以下函数加入输出测试
def up_clicked():
    print('up')
    t1,t2,t3,sp=inverse_kin(posx,posy,posz+6,ui.lineEdit_mo4.text())
    tri_move(t1,t2,t3,sp)
def down_clicked():
    print('down')
    t1,t2,t3,sp=inverse_kin(posx,posy,posz-6,ui.lineEdit_mo4.text())
    tri_move(t1,t2,t3,sp)
def left_clicked():
    print('left')
    t1,t2,t3,sp=inverse_kin(posx,posy-6,posz,ui.lineEdit_mo4.text())
    tri_move(t1,t2,t3,sp)
def right_clicked():
    print('right')
    t1,t2,t3,sp=inverse_kin(posx,posy+6,posz,ui.lineEdit_mo4.text())
    tri_move(t1,t2,t3,sp)
def behind_clicked():
    print('behind')
    t1,t2,t3,sp=inverse_kin(posx-6,posy,posz,ui.lineEdit_mo4.text())
    tri_move(t1,t2,t3,sp)
def front_clicked():
    print('front')
    t1,t2,t3,sp=inverse_kin(posx+6,posy,posz,ui.lineEdit_mo4.text())
    tri_move(t1,t2,t3,sp)


def btn_mop_clicked():
    global posx,posy,posz
    startpos = [posx,posy,posz]
    #print(startpos )
    endpos = [float(ui.lineEdit_mp1.text()),\
              float(ui.lineEdit_mp2.text()),\
              float(ui.lineEdit_mp3.text())]
    tgts = []
    midpos = [(startpos[0]+endpos[0])/2,(startpos[1]+endpos[1])/2,posz+50]
    
    
    tgt = [startpos,midpos,endpos]
    tgts = []
    for row in tgt:
        tpr1 ,tpr2,tpr3 ,yyy= inverse_kin(row[0],row[1],row[2],0)
        tgts.append([tpr1,tpr2,tpr3])
    
    #print("gggg = {}".format(tgts))
    for row in tgts:
        flag = 0
        tri_move2(row[0],row[1],row[2],ui.lineEdit_mp4.text())

        #th = Thread_3()
        #th.run(row)
        

if __name__ == '__main__':
    serial0 = serial.Serial('/dev/ttyACM0', 115200, timeout=0.5)
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    ui.pushButton_sta.clicked.connect(btn_sta_clicked)
    ui.pushButton_reset.clicked.connect(btn_reset_clicked)
    ui.pushButton_pow.clicked.connect(btn_pow_clicked)
    ui.pushButton_move.clicked.connect(btn_move_clicked) 
    ui.pushButton_move_2.clicked.connect(btn_mol_clicked)
    ui.pushButton_move_3.clicked.connect(btn_mop_clicked)
    ui.pushButton_up.clicked.connect(up_clicked) 
    ui.pushButton_down.clicked.connect(down_clicked)
    ui.pushButton_left.clicked.connect(left_clicked) 
    ui.pushButton_right.clicked.connect(right_clicked)
    ui.pushButton_behind.clicked.connect(behind_clicked) 
    ui.pushButton_front.clicked.connect(front_clicked)
    MainWindow.show()





    sys.exit(app.exec_())




