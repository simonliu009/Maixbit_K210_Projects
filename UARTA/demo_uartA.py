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


write_bytes = b'hello world\r\n'
data2 = b'0xAA 0x5A 0x00 0x00 0x00 0x01 0x00 0x00 0x00 0x04 0x00 0x64 0x00 0x00 0x01 0x12 0x00 0x80'
hexlist = ['AA','5A','00','00','00','01','00','00','00','04','00','64','00','00','01','12','00','80']
datalist= []
for i in range(len(hexlist)):
    datalist.append(int(hexlist[i], 16))
data = bytes(datalist)

for i in range(30):
    #uart_A.write(write_bytes)
    uart_A.write(data)

    print("write_bytes =%s , count %d"% (write_bytes,i+1))
    time.sleep(6)


uart_A.deinit()
del uart_A

