# input and output

name = input("pls input you name:")
age = int(input("pls input your age:"))
print("hello", name, ",you are", age, "years old")
print("hello {}, you are {} years old. ".format(name, age))
print("hello %s, you are %d years old" % (name, age))

