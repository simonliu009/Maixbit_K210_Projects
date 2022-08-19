from fpioa_manager import fm
from machine import UART
from board import board_info
from fpioa_manager import fm
import time

# maixduino board_info PIN10/PIN11/PIN12/PIN13 or other hardware IO 12/11/10/3
fm.register(25, fm.fpioa.UART1_TX, force=True)
fm.register(24, fm.fpioa.UART1_RX, force=True)
#fm.register(board_info.PIN12, fm.fpioa.UART2_TX, force=True)
#fm.register(board_info.PIN13, fm.fpioa.UART2_RX, force=True)

uart_A = UART(UART.UART1, 9600, 8, 0, 0, timeout=1000, read_buf_len=4096)

# 向蜂鸟 灵TR-2 2.4G模块发送命令。
hexlist = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','01','12','00','80']
datalist= []
for i in range(len(hexlist)):
    datalist.append(int(hexlist[i], 16))
data = bytes(datalist)

hexlist2 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','02','12','00','81']
datalist2= []
for i in range(len(hexlist)):
    datalist2.append(int(hexlist2[i], 16))
data2 = bytes(datalist2)

hexlist3 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','03','12','00','82']
datalist3= []
for i in range(len(hexlist)):
    datalist3.append(int(hexlist3[i], 16))
data3 = bytes(datalist3)

hexlist4 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','04','12','00','83']
datalist4= []
for i in range(len(hexlist)):
    datalist4.append(int(hexlist4[i], 16))
data4 = bytes(datalist4)

hexlist5 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','05','12','00','84']
datalist5= []
for i in range(len(hexlist)):
    datalist5.append(int(hexlist5[i], 16))
data5 = bytes(datalist5)

hexlist6 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','06','12','00','85']
datalist6= []
for i in range(len(hexlist)):
    datalist6.append(int(hexlist6[i], 16))
data6 = bytes(datalist6)

hexlist7 = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','07','12','00','86']
datalist7= []
for i in range(len(hexlist)):
    datalist7.append(int(hexlist7[i], 16))
data7 = bytes(datalist7)

uart_A.write(data)
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

uart_A.deinit()
del uart_A

