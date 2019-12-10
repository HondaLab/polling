#
import socket1a as sk
from matplotlib import pyplot as plt
import time
import numpy as np

print(sk.ADDR, sk.PORT)
udp=sk.UDP_Recv(sk.ADDR, sk.PORT)

x=[0.0 for i in range(100)]
y=[0.0 for i in range(100)]
y1=[0.0 for i in range(100)]
now=time.time()
start=now
plt.ylim(-2,2)
plt.grid()


lin, =  plt.plot(x,y,color='#ff0000')
lin1, =  plt.plot(x,y1,color='#0000ff')
while 1:
   try:
      data=udp.recv()
      print("\r %7.2f %7.2f %4d" % (data[0],data[1],data[2]), end='')
      x.pop(0)
      x.append(now-start)
      y.pop(0)
      y.append(data[0])
      y1.pop(0)
      y1.append(data[1])
      plt.xlim(min(x),max(x))
      lin.set_xdata(x)
      lin.set_ydata(y)
      lin1.set_xdata(x)
      lin1.set_ydata(y1)
      plt.pause(0.0001)
   except BlockingIOError:
      pass
   now=time.time()
