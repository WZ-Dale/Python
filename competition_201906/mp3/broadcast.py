import os
import time
a = 1.2222			# 外部传参
if a >= 15:		a = -1
elif a >= 10:	a = 10
elif a >= 9:	a = 9
elif a >= 8:	a = 8
elif a >= 7:	a = 7
elif a >= 6:	a = 6
elif a >= 5:	a = 5
elif a >= 4.5:	a = 4.5
elif a >= 4:	a = 4
elif a >= 3:	a = 3
elif a >= 3.8:	a = 3.8
elif a >= 3.6:	a = 3.6
elif a >= 3.4:	a = 3.4
elif a >= 3.2:	a = 3.2
elif a >= 3:	a = 3
elif a >= 2.8:	a = 2.8
elif a >= 2.6:	a = 2.6
elif a >= 2.4:	a = 2.4
elif a >= 2.2:	a = 2.2
elif a >= 2:	a = 2
elif a >= 1.9:	a = 1.9
elif a >= 1.8:	a = 1.8
elif a >= 1.7:	a = 1.7
elif a >= 1.6:	a = 1.6
elif a >= 1.5:	a = 1.5
elif a >= 1.4:	a = 1.4
elif a >= 1.3:	a = 1.3
elif a >= 1.2:	a = 1.2
elif a >= 1.1:	a = 1.1
elif a >= 1:	a = 1
elif a >= 0.9:	a = 0.9
elif a >= 0.8:	a = 0.8
elif a >= 0.7:	a = 0.7
elif a >= 0.6:	a = 0.6
elif a >= 0.5:	a = 0.5
elif a >= 0.4:	a = 0.4
elif a >= 0.3:	a = 0.3
elif a >= 0.2:	a = 0.2
elif a >= 0.1:	a = 0.1
elif a >= 0:	a = 0
mp3 = repr(a) + 'm.mp3'
if isinstance(a, int):
	sleep = 0.5
else:
	sleep = 0.7		
while a >= 0:
	os.system(mp3)
	time.sleep(sleep)
