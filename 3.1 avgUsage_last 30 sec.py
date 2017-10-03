import psutil
import time
import numpy

def avg_usage():
    avg_usage = psutil.cpu_times()
    
    return avg_usage
while True:
    time.sleep(30)
    print("CPU Times: ", avg_usage())
    cpu_times = psutil.cpu_times()
    print("Average Usage: ", numpy.mean(cpu_times))



    

