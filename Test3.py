'''yue=21200
cunkuan="1000" # 字符串型
cunkuan=int(cunkuan)

print("存款后余额为：",yue+int(cunkuan))
'''

a="35.23"
g="hello"   # 这个就不可以转换成 int 型
b=22
c=3.14
d=""
e=0
f=None



print("转换前：",type(g))
#x=int(a)
#x=int(float(a))
x=bool(g)
print("转换后：",type(x))
print(x)