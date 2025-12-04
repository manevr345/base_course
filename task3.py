import time
M = int(input())
N = int(input())
timer1 = time.time()
for i in range(M):
    print(i)
    time.sleep(1)
    for s in range(round(float(f'{N}.{M}'))):
        print(s)
        time.sleep(1)
timer2 = time.time()
print(f'time ={timer2}-{timer1}')    