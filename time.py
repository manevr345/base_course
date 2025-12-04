import time
timer = time.time()
print(timer)
for i in range(10):
    print(i)
    time.sleep(1)
print(f'{time.time() - timer} seconds')