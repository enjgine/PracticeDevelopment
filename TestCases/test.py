import time

current_time = time.time() + 1
counter = 0
time.sleep(current_time-time.time())
while time.time() < current_time + 1:
	counter += 1
print(counter)