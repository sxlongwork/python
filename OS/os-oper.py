import os

hosts_content = os.popen("cat /etc/hosts").read()
print(hosts_content)

print(os.getcwd())
print(os.curdir)    # .
print(os.pardir)    # ..
print(os.chdir("/tmp"), os.getcwd())
