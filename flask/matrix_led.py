
import random
import max7219.led as led
import time
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from random import randrange

rc = lambda x:int(x*random.random())
device = led.matrix(cascaded=1)






while 1:
    device.pixel(rc(8),rc(8),1)
    time.sleep(0.002)
    device.clear()



device.clear()
# 交错闪烁
[[device.pixel(i,x,((i+x)%2)) for i in range(8) ]for x in range (8)]
c = 1
while 1:
    device.invert(c)
    c=(c+1)%2
    time.sleep(0.001)


# 会 变化的闪烁
[[device.pixel(i,x,((i+x)%2)) for i in range(8) ]for x in range (8)]
c = 1
maxx=0.1
minn=1./120
t=maxx
mul = 0.8
import time
ti = int(time.time())
while 1:
    device.invert(c)
    c=(c+1)%2
    if int(time.time()) != ti:
        ti=int(time.time())
        t=t*mul
        print t
    if t > maxx or t < minn:
        mul=1/mul
        t=mul*mul*t
    time.sleep(t)






device._buffer=[0]*8;device.flush()



device._buffer=[rc(256) for i in range(8)];device.flush()

while 1:
    device._buffer=[rc(256) for i in range(8)];device.flush()
    time.sleep(0.0002)


while 1:
    device.clear()
    device.pixel(rc(8),rc(8),1)
    device.pixel(rc(8),rc(8),1)
    time.sleep(0.02)





# 单点来回闪烁
pos = 0
maxx=0.1
minn=0.0001
mul = 0.9
t=maxx
ti = int(time.time())
step = 1
while 1:
    device.pixel(pos/8,pos%8,1)
    pos += step
    if pos == 64 or pos == -1:
        step = -step
        pos = step *2+pos
    if int(time.time()) != ti:
        ti=int(time.time())
        t=t*mul
        print t
    if t > maxx or t < minn:
        mul=1/mul
        t=mul*mul*t
    time.sleep(t)
    device.clear()




def f(dic):
    device.pixel(dic['pos']/8,dic['pos']%8,1)
    dic['pos'] += dic['step']
    if dic['pos'] == 64 or dic['pos'] == -1:
        dic['step'] = -dic['step']
        dic['pos'] = dic['step'] *2+dic['pos']    


dic={
'pos' : 0,
'step' : 1,
'_f' : f,
}



def time_loop(_dic,maxx=0.1,minn=0.001,mul=0.9):
    '''
    t周期性变化的循环结构
    '''
    _t=maxx
    _ti = int(time.time())
    while 1:
        _dic['_f'](_dic)
        if int(time.time()) != _ti:
            _ti=int(time.time())
            _t=_t*mul
            print _t
        if _t > maxx or _t < minn:
            mul=1/mul
            _t=mul*mul*_t
        time.sleep(_t)
        device.clear()


time_loop(dic)





