import socket
import random
import time
import socket1a as sk

if __name__=='__main__':

   udp = sk.UDP_Send(sk.ADDR, sk.PORT)
   data=[1] # 送信データ用のリスト
   i=0 
   start=time.time()
   print("# 10秒間乱数をsendするテスト")
   while time.time()-start<10 :
      data[0] = random.randint(1,100000000)/10000000
      print("%5.1f %s" % (time.time()-start,data[0]))
      udp.send(data)
      time.sleep(0.10)
      i=i+1
