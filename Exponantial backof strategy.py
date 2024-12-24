
import time

attemed = 0
wait_time = 1
max_try = 5
while attemed <= max_try:
    print("")
    time.sleep(wait_time)
    print("Attemed:",attemed+1," watting time ",wait_time)
    attemed += 1
    wait_time *= 2


