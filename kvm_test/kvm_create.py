import libvirt
import os

conn = libvirt.open("qemu:///system")


def conn_close():
    try:
        conn.close()
    except:
        print("close connection failed")
    else:
        print("colse connection success")


def show_running():
    """show running vhost"""
    running = conn.listDomainsID()
    dict_domain_names = {}
    for id in running:
        dict_domain_names[str(id)] = conn.lookupByID(id).name()

    print("------running vhost------")
    print("id\tvhostname")
    for domain_id,domain_host in dict_domain_names.items():
        print(domain_id, domain_host, sep="\t")


def show_hostInfo():
    """show host info"""
    hostInfo = conn.getInfo()
    print("-------host info--------")
    print("cpu module:", hostInfo[0])
    print("total mem(MB):", hostInfo[1])
    print("free mem(MB):", int(conn.getFreeMemory()/1024/1024))
    print("cpu numbers:", hostInfo[2])
    print("virtual type:", conn.getType())
    print("connect url:", conn.getURI())


def cretae_vhost():
    os.chdir("/home/kvm")


show_hostInfo()
show_running()




