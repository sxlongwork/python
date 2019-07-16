import dns.resolver

# A record

domain = input("pls input a domain:")       # www.baidu.com
A = dns.resolver.query(domain, 'A')
for x in A:
    print(x)

# NS record
domain = input("pls input a domain:")       # baidu.com,
ns = dns.resolver.query(domain, 'NS')       # 返回解析该域名的dns服务器域名
for x in ns:
    print(x)

# CNAME record
domain = input("pls input a domain:")       # www.baidu.com
cname = dns.resolver.query(domain, 'CNAME') # www.a.shifen.com.
for x in cname:
    print(x)
