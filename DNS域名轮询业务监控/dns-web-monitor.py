import dns.resolver
import http.client

ip_list = []

domain = 'www.baidu.com'


def get_iplist():
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print("get ip list error", e)
    else:
        for ip in A.response.answer:
            for x in ip.items:
                ip_list.append(x)


def http_check(ip):
    url = ip + ":80"
    conn = http.client.HTTPConnection(url)
    try:
        conn.request("GET", "/", headers={"Host": domain})
        r = conn.getresponse()
        content = r.read(15)
        content = content.decode("utf-8")
    except Exception as e:
        print("http request error", e)
    else:
        if content == "<!DOCTYPE html>":
            print(ip, " OK")
        else:
            print(ip, " Error")


if __name__ == "__main__":
    get_iplist()
    for ip in ip_list:
        http_check(str(ip))

