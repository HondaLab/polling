# recv側のプログラム(Robot)はこの例のように
# exceptでBlockingIOErrorを処理しなければならない。
# recv側のloop rate が send側のloop rateよりも大きくなるようにtime.sleep
# を調節する。これにより、センサー値のリアルタイム性が確保される。
# recv側のtime.sleepを外すと、rateは最大となるが、ビジーループとなり、
# CPUを最大消費するので注意が必要。

import socket1a as sk
import time
import socket

if __name__=='__main__':

   udp = sk.UDP_Recv(sk.ROBOT_ADDR, sk.MPU9150_PORT)
   # ここでは、socket1a内に登録してあるアドレスとポートを用いたが
   # 別のものを指定してももちろん機能する
   data=[1]
   start = time.time()
   print("# 10秒間Noblocking recieve のテスト")
   while time.time()-start<10 :
      try:
         data = udp.recv()
         print("%8.4f %12.8f" % ((time.time()-start),data[0]))
         time.sleep(0.05)
      except (BlockingIOError,  socket.error):
         # Noblockingなので、まだ届いてない場合の処理
         #print("%5.1f no recv" % (time.time()-start))
         time.sleep(0.05)
         continue
      except OSError:
         break