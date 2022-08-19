# 使用BOOT按键控制向”灵TR-2“发送串口命令
from fpioa_manager import fm
from machine import UART
from board import board_info
import time
from Maix import GPIO
import utime

# 手里的版本  Boot按键就是HS0
fm.register(board_info.BOOT_KEY, fm.fpioa.GPIOHS0, force=True)



# maixduino board_info PIN10/PIN11/PIN12/PIN13 or other hardware IO 12/11/10/3
fm.register(25, fm.fpioa.UART1_TX, force=True)
fm.register(24, fm.fpioa.UART1_RX, force=True)
#fm.register(board_info.PIN12, fm.fpioa.UART2_TX, force=True)
#fm.register(board_info.PIN13, fm.fpioa.UART2_RX, force=True)

uart_A = UART(UART.UART1, 9600, 8, 0, 0, timeout=1000, read_buf_len=4096)

cnt = 0



# 向蜂鸟 灵TR-2 2.4G模块发送命令。
hexlist1 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','01','12','00','80']
datalist1= []
for i in range(len(hexlist1)):
    datalist1.append(int(hexlist1[i], 16))
data1 = bytes(datalist1)

hexlist2 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','02','12','00','81']
datalist2= []
for i in range(len(hexlist1)):
    datalist2.append(int(hexlist2[i], 16))
data2 = bytes(datalist2)

hexlist3 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','03','12','00','82']
datalist3= []
for i in range(len(hexlist1)):
    datalist3.append(int(hexlist3[i], 16))
data3 = bytes(datalist3)

hexlist4 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','04','12','00','83']
datalist4= []
for i in range(len(hexlist1)):
    datalist4.append(int(hexlist4[i], 16))
data4 = bytes(datalist4)

hexlist5 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','05','12','00','84']
datalist5= []
for i in range(len(hexlist1)):
    datalist5.append(int(hexlist5[i], 16))
data5 = bytes(datalist5)

hexlist6 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','06','12','00','85']
datalist6= []
for i in range(len(hexlist1)):
    datalist6.append(int(hexlist6[i], 16))
data6 = bytes(datalist6)

hexlist7 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','07','12','00','86']
datalist7= []
for i in range(len(hexlist1)):
    datalist7.append(int(hexlist7[i], 16))
data7 = bytes(datalist7)

last_push_time = 0

def bootkey_irq(pin_num):
    #print("key", pin_num)
    global cnt,last_push_time

    t = utime.time()
    print("Time=",t)
    if (t-last_push_time > 2):
        cnt += 1
        last_push_time = t
        print("cnt = %d"%cnt)
    if (cnt%7==0):
        uart_A.write(data1)
    elif (cnt%7==1):
        uart_A.write(data2)
    elif (cnt%7==2):
        uart_A.write(data3)
    elif (cnt%7==3):
        uart_A.write(data4)
    elif (cnt%7==4):
        uart_A.write(data5)
    elif (cnt%7==5):
        uart_A.write(data6)
    elif (cnt%7==6):
        uart_A.write(data7)



key=GPIO(GPIO.GPIOHS0, GPIO.IN, GPIO.PULL_NONE)
key.irq(bootkey_irq, GPIO.IRQ_FALLING, GPIO.WAKEUP_NOT_SUPPORT, 7)

#
#time.sleep(6)
#uart_A.write(data3)
#time.sleep(7)
#uart_A.write(data4)
#time.sleep(7)
#uart_A.write(data5)
#time.sleep(7)
#uart_A.write(data6)
#time.sleep(7)
#uart_A.write(data7)
#time.sleep(7)
while(1):
    time.sleep(1)

uart_A.deinit()
del uart_A

