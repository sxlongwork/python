import psutil
import datetime

# CPU management info
# User time
# System time
# Wait io
# Idle
# cpuinfo = psutil.cpu_times()
# percpu = psutil.cpu_times(percpu=True)
# cpu_number = psutil.cpu_count()

# mem management info
# total mem
# free mem
# userd mem
# buffer,cached
# swap mem

# disk management info
# disk used
# read/write io count
# read/write io bytes
# read/write io time

# network management info
# sent/recv bytes
# sent/recv packets


def cpuinfo():
    """cpu info"""
    cpuinfo = psutil.cpu_times()
    print("----------CPU INFO-----------")
    print("User:", cpuinfo.user)
    print("system:", cpuinfo.system)
    print("iowait:", cpuinfo.iowait)
    print("Idle:", cpuinfo.idle)
    print("cpu physical number:", psutil.cpu_count(logical=False))
    print("cpu logical number:", psutil.cpu_count(logical=True))
    print("-----------------------------")


def meminfo():
    """mem info"""
    meminfo = psutil.virtual_memory()
    swap = psutil.swap_memory()
    print("-------MEM INFO(bytes)--------")
    print("total mem:", meminfo.total)
    print("used mem:", meminfo.used)
    print("free mem:", meminfo.free)
    print("buffers mem:", meminfo.buffers)
    print("cached mem:", meminfo.cached)
    print("swap total:", swap.total)
    print("swap used:", swap.used)
    print("swap free", swap.free)
    print("------------------------------")


def diskinfo():
    disk_part = psutil.disk_partitions()
    disk_used = psutil.disk_usage("/")
    disk_io = psutil.disk_io_counters()
    print("---------DISK INFO----------")
    print(disk_part)
    print(disk_used)
    print(disk_io)
    print("----------------------------")


def networkinfo():
    netinfo = psutil.net_io_counters()
    print("---------DISK INFO----------")
    print(netinfo)
    print("----------------------------")


def otherinfo():
    users = psutil.users()      # connected system currently
    print("----connected user----")
    for user in users:
        print("user name:", user.name)
        print("client ip:", user.host)
        print("connect time:", user.started)
    print("----------------------")
    print("------boot time--------")
    print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))



cpuinfo()
meminfo()
diskinfo()
networkinfo()
otherinfo()
