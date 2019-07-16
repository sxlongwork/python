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


def show_all():
    """show all not running vhost"""
    all = conn.listDefinedDomains()
    print("-----stopped vhost list--------")
    for name in all:
        print(name)


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
    f = open("/home/vmm/centos7u6/centos.xml")  # xml文件需要事先准备好
    xml = f.read()
    conn.createXML(xml)         # 临时虚拟机
    f.close()


def define_vhost():
    f = open("/home/vmm/centos7u6/centos.xml")
    xml = f.read()
    conn.defineXML(xml)     # Define a domain, but does not start it
    f.close()


def undefine_vhost(vhost_name):
    dom = conn.lookupByName(vhost_name)
    dom.undefine()          # if vhost_name is running,it will remove it,if vhost is notting running,when you shutdown it,it will be removed auto
    print("undefined {}".format(vhost_name))


def suspand_vhost(vhost_name):
    dom = conn.lookupByName(vhost_name)
    dom.suspend()       # pause vhost
    print("{} pause success".format(vhost_name))


def resume(vhost_name):
    dom = conn.lookupByName(vhost_name)
    dom.resume()        # resume vhost
    print("{} resume running".format(vhost_name))


def start_vhost(vhost_name):
    dom = conn.lookupByName(vhost_name)
    dom.create()        # start vhost
    print("{} is staring......".format(vhost_name))


def shutdown_vhost(vhost_name):
    dom = conn.lookupByName(vhost_name)
    dom.shutdown()      # shutdown vhost
    print("{} is stopping......".format(vhost_name))


def destroy_vhost(vhost_name):
    dom = conn.lookupByName(vhost_name)
    dom.destroy()       # if vhost is running,it will shutdown vhost;
    print("{} is destroyed".format(vhost_name))


destroy_vhost("hosta")
# shutdown_vhost("hosta")
# start_vhost("hosta")
# uspand_vhost("hosta")
# resume("hosta")
# undefine_vhost("hosta")


# show_all()
# show_hostInfo()
# show_running()





