import psutil
import time
import os

def log_date_time():
    current_time = time.strftime("%x") + " " + time.strftime("%H:%M:%S")
    return current_time

def cpu_cores():
    cores_count = psutil.cpu_count()
    return cores_count

def RAM_usage():
    system_RAM = psutil.virtual_memory()
    print("RAM info: ", system_RAM)
    system_RAM_usage = psutil.Process(os.getpid())
    RAM = system_RAM_usage.memory_percent()
    return RAM

def Disk_usage():
    system_disk = psutil.disk_partitions()
    print("Disk info: ", system_disk)
    system_disk_usage = psutil.disk_usage("/")
    return system_disk_usage

def CPU_usage():
    for proc in psutil.process_iter(attrs=['name', 'username', 'pid']):
        system_CPU = psutil.cpu_percent(interval = 1, percpu = True)
        print("CPU info: ", proc.info, system_CPU)
        system_CPU_usage = psutil.Process(proc.pid)
        CPU_process = system_CPU_usage.cpu_percent(interval = 1)
        return CPU_process

while True:
    print("Date and Time: ", log_date_time())
    print("Number of CPU Cores: ", cpu_cores())
    print("RAM Usage: ", RAM_usage())
    print("Disk Usage: ", Disk_usage())
    print("CPU Usage: ", CPU_usage())
    time.sleep(5)
    
