from IPy import IP


def version(ipaddr):
    """ipaddr verion"""
    print("{} is ipv{} address.".format(ipaddr, IP(ipaddr).version()))


def iplist(ipfield):
    """ip list"""
    ip = IP(ipfield)
    print("{} has total {} ips".format(ipfield, ip.len()))
    for x in ip:
        print(x)


print("-----------ip field--------")
ips = IP("192.168.33.0/24")                # ['71.33.168.192.in-addr.arpa.']
print(ips.len())
print("地址反向解析:", ips.reverseNames())
print("ip type:", ips.iptype())                      # PRIVATE
print("网络地址:", ips.net())
print("掩码地址:", ips.netmask())
print("广播地址:", ips.broadcast())

print(IP("119.29.29.29").iptype())      # PUBLIC

print("--------single ip------------")
ip = IP("192.168.33.71")
print(ip.reverseNames())



# print(IP("172.17.0.2").make_net("255.255.0.0"))     # 172.17.0.0/16

# iplist("192.168.1.0/25")
# version("192.168.33.70")
