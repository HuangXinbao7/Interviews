## 第1部分 Python基础篇（80题-I）



### 1、为什么学习Python？

```
因为Python相对其他语言非常优雅简洁，有着丰富的第三方库，我感觉很强大、很方便;
还有就是，我感觉Python简单易学，生态圈庞大，例如：web开发、爬虫、人工智能等，而且未来发展趋势也很不错。
出于编程的喜爱，以及行业本身的前瞻性，创造性，优越性，越是综合的科目越能检验一个人的能力，喜欢这种有挑战的事情。
```



### 2、通过什么途径学习的Python？

```
答1：
跟随老师学习，以及自己查询资料，结合实战，进行输入输出以及纠正。

答2：
通过自学，网上看视频资料，网上买书的方法学习
```



### 3、Python和Java、PHP、C、C#、C++等其他语言的对比？

```
Python、PHP是解释型语言，代码运行期间逐行翻译成目标机器码，下次执行时逐行解释
而C、Java是编译型语言，编译后再执行


Python的特点
	语法简洁优美，功能强大，标准库与第三方库非常强大，而且应用领域广；
	可移植性、可扩展性、可嵌入性
	Python是弱类型语言

Python的缺点
	运行速度慢
	

Python的优势：
1、Python 易于学习;
2、用少量的代码构建出很多功能;（高效的高级数据结构）
3、Python 拥有最成熟的程序包资源库之一;
4、Python完全支持面向对象;
5、Python 是跨平台且开源的；
6、Python是强类型加动态语言。
```



### 4、简述解释型和编译型编程语言？

```
解释型
	边解释边执行（Python、PHP）
	解释型在运行时由翻译器将高级语言代码翻译成易于执行的中间代码，并由解释器逐一将该中间代码解释成机器码并执行。

编译型
	编译后再执行（C、Java、C#）
	编译型语言是指在运行前先由编译器将高级语言代码编译为对应机器的cpu汇编指令集，再由汇编器汇编成目标机器码，生成可执行文件，然后最后运行生成的可执行文件。
```



### 5、Python解释器种类以及特点？

```
CPython		
是官方版本的解释器，使用C语言开发，所以叫CPython；
在领命行吓运行 Python 解释器就是启动 CPython解释器；
CPython是使用最广泛的解释器。

IPython
基于CPython之上的交互式解释器，只是在交互上有增强
CPython用>>>作为提示符，而IPython用In [序号]:作为提示符

JPython
Jython是运行在java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行
Java写的解释器。

PyPy
Python写的解释器，目前执行速度最快的解释器，采用JIT技术，对Python进行动态编译（注意不是解释）

IronPython
C#写的解释器，IronPython和Jython类似，只不过IronPython是运行在.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。
```



### 6、位和字节的关系？

```
1字节 = 8位
1Byte = 8bit （数据存储以字节(Byte)为单位）

位是计算机内部数据存储的最小单位，
字节是计算机中数据处理的基本单位，
计算机中以字节位单位存储和解释信息，
规定一个字节由8个二进制位构成。
```



### 7、b、B、KB、MB、GB 的关系？

```
b	表示位
B	表示字节
1字节等于8位

1B=8bit
1KB=1024B
1MB=1024KB
1G=1024MB
1T=1024G
```



### 8、请至少列举5个 PEP8 规范（越多越好）。

```
缩进使用4个空格，或者IDE中以TAB键当做4个空格。
所有行限制为最多79个字符
两个空白行围绕顶层函数和类定义
核心代码应始终使用UTF-8，所有标识符使用纯ascii标识符，并且应尽可能使用英文单词。
Import接口通常应该分开，导入始终放在文件的顶部，紧跟在任何模块注释和文档字符串之后，模块全局变量和常量之前。

4、必要时候，在每一行下写注释
5、使用文档注释，写出函数注释
6、在操作符和逗号之后使用空格，但是不要在括号内部使用
7、命名类和函数的时候使用一致的方式，
比如使用CamelCase来命名类，使用lower_case_with_underscores来命名函数和方法
8、在类中总是使用self来作为默认
9、尽量不要使用魔法方法
10、默认使用UTF-8，甚至ASCII作为编码方式
11、换行可以使用反斜杠，最好使用圆括号。
12、不要在一句import中多个库，


# 1、空格使用
a 各种右括号前不要加空格。
b 逗号、冒号、分号前不要加空格。
c 函数的左括号前不要加空格。如Func(1)。
d 序列的左括号前不要加空格。如list[2]。
e 操作符左右各加一个空格，不要为了对齐增加空格。
f 函数默认参数使用的赋值符左右省略空格。
g 不要将多句语句写在同一行，尽管使用‘；’允许。
8 if/for/while语句中，即使执行语句只有一句，也必须另起一行。

函数命名使用全部小写的方式，常量命名使用大写，类属性（方法和变量）使用小写
类的命名首字母大写


# 2、代码编排
a 缩进，4个空格，而不是tab键
b 每行长度79，换行可使用反斜杠，最好使用圆括号。
c 类与类之间空两行
d 方法之间空一行
```



### 9、通过代码实现如下转换：

```
二进制转换成十进制：v = 0b1111011
十进制转换成二进制：v = 18
八进制转换成十进制：v = 011
十进制转换成八进制：v = 30
十六进制转换成十进制：v = 0x12
十进制转换成十六进制：v = 87

################################
v = 0b1111011
print(int(v))

v = 18
print(bin(v))

v = '011'
print(int(v))
print(int("011",8))

v = 30
print(oct(v))

v = 0x12
print(int(v))
print(int('0x12', 16))

v = 87
print(hex(v))
```



### 10、请编写一个函数实现将IP地址转换成一个整数

```
如 10.3.9.12 转换规则为：
10	00001010
3 	00000011
9 	00001001
12 	00001100

再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？
```

```
IP = '10.3.9.12'

def addr2Dec(addr):
    """将点分十进制IP地址转换成十进制整数"""
    items = [int(x) for x in addr.split(".")]
    # return sum([items[i] << [24, 16, 8, 0][i] for i in range(4)])
    return sum([items[i]*2**[24, 16, 8, 0][i] for i in range(4)])


print(addr2Dec(IP))     # 167971084
```



### 11、Python递归深度的最大层数？

```
默认是1000。
但是这个阀值是可以修改的
```

```
# 测试默认递归深度
import sys
def foo(n):
    print(n)
    n += 1
    foo(n)


if __name__ == "__main__":
	# 默认是 1000
	print(sys.getrecursionlimit())      # 1000
    
    foo(1)	# 打印到996就抛出异常
```

```
# 手动设置递归深度的阈值
import sys
# 修改为 10000
sys.setrecursionlimit(10000)


def foo(n):
    print(n)
    n += 1
    foo(n)


if __name__ == "__main__":
	print(sys.getrecursionlimit())	# 10000
    foo(1)		# 能打印到 3924 才抛错
```



### 12、求结果：

```
v1 = 1 or 3 -- 1
v2 = 1 and 3 -- 3
v3 = 0 and 2 and 1 -- 0
v4 = 0 and 2 or 1 -- 1
v5 = 0 and 2 or 1 or 4 -- 1
v6 = 0 or Flase and 1 -- False
```

求结果：2 & 5

```
print(2 & 5)	# 10 & 101 => 000 => 0

```

求结果：2 ^ 5

```
print(2 ^ 5) # 10 ^ 101 => 111 => 1*2**0+1*2**1+1*2**2=1+2+4=7
```



### 13、字符编码ASCII、Unicode、GBK、UTF-8 区别？

```
ASCII		8位一个字节
Unicode		32位 四个字节，支持中英文
GBK		英文：8位 一个字节；中文：16位 两个字节
UTF-8	英文：8位 一个字节；中文：16位 两个字节



Python2内容进行编码（默认ascii）, 而Python3对内容进行编码的默认为utf-8
ASCII 	最多只能用8位来表示（一个字节），即：2**8 = 256，所以，ASCII码最多只能表示 256 个符号。
Unicode 万国码，任何一个字符==两个字节
utf-8 	万国码的升级版 一个中文字符==三个字节 英文是一个字节 欧洲的是 2个字节
gbk 	国内版本 一个中文字符==2个字节 英文是一个字节
gbk 	转 utf-8 需通过媒介 unicode
```



### 14、字节码和机器码的区别？

```
机器码：
	机器语言
	机器码是电脑CPU直接读取运行的机器指令，运行速度最快，但是非常晦涩难懂，也比较难编写，一般从业人员接触不到。

字节码：
	汇编语言
	字节码是一种中间状态（中间码）的二进制代码（文件）。需要直译器转译后才能成为机器码。
```



### 15、三元运算规则以及应用场景？

运算规则：如果条件为真，把if前面的值赋值给变量，否则把else后面的值赋值给变量。

应用场景：简化if语句

```
a = 1 
b = 3
c = b if b > 2 else a
```



### 16、列举 Python2和Python3的区别？

```
print:
	Python2中的print是语句；
	Python3中的print() 是函数
    
编码
	Python2中默认是ASCII码
	Python3中默认使用UTF-8
	
字符串
	Python2中分ASCII码和Unicode码
	Python3中所有字符串都是Unicode码
	
True和False
	Python2中两个是全局变量（1和0），可以重复赋值
	python3中两个是关键字，不可以重新赋值
	
迭代 range
	Python2中使用 xrange和range
	Python3中使用 range
	
Nonlocal
	Python3中新增，声明为非全局变量
	
经典类和新式类
	Python2中有经典类和新式类
	Python3中新式类都默认继承 Object

yield
	python2中 yield
	Python3中 yield/yield from
	
文件操作
	Python2 中 
		readlines() 读取文件的所有行，返回一个列表，包含所有行的结束符
		xreadlines() 返回一个生成器，循环取值
	Python3中
		只有 readlines()
		
输出中文的区别
	Python2中要使用中文，必须在文件头声明 # -*- encoding:utf-8 -*-
	Python3中不需要

input不同
	Python2中使用 raw_input
	Python3中使用 input函数

性能
	Python3性能比Python2慢15%，但还有很大的提升空间。
	
语法
    去除print语句
    关键词加入as 和with，还有True,False,None
    删除了raw_input，用input代替
    新的metaclass语法

字符串和字节串
	字符串只有str一种类型

数据类型
	只有一种整型——int
	新增了bytes类型


面向对象
	容器类和迭代器类被ABCs化，所以cellections模块里的类型比Py2.5多了很多
	迭代器的next()方法改名为__next__()，并增加内置函数next()，用以调用迭代器的__next__()方法


不相等操作符"<>"被Python3废弃，统一使用"!="
long整数类型被Python3废弃，统一使用int
迭代器iterator的next()函数被Python3废弃，统一使用next(iterator)
异常StandardError 被Python3废弃，统一使用Exception
字典变量的has_key函数被Python废弃，统一使用in关键词
file函数被Python3废弃，统一使用open来处理文件，可以通过io.IOBase检查文件类型
```



### 17、用一行代码实现数值交换：

```
a = 1
b = 2
##############
a, b = b, a
```



### 18、Python3和Python2中 int 和 long的区别？

```
Python2中有long类型
Python3中没有long类型，只有int类型,统一使用int,大小和py2的long类似

int <= 32 位整数
long > 32 位整数
```



### 19、xrange和range的区别？

```
在python2中：
	xrange 返回的是一个迭代值（生成器）
	range 返回的是一个列表
	要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要开辟一块很大的内存空间。

在python3中：
	range 返回的是一个迭代值（生成器）
	在 Python 3 中，range() 是像 xrange() 那样实现，xrange()被抛弃。
```



### 20、文件操作时：xreadlines和readlines的区别？

```
readlines：
	读取文件的所有行，返回一个列表，包含所有行的结束符
xreadlines：
	返回一个生成器，循环使用和readlines基本一致。（py2有，py3被废弃）
```



### 21、列举布尔值为False的常见值？

```
[] {} None '' () 0 -0 False set() 不成立的表达式
```



### 22、字符串、列表、元组、字典每个常用的5个方法？

**字符串：**

字符串用单引号(')或双引号(")括起来，不可变

```
字母处理相关
upper()			全部大写，无参数
lower()			全部小写，无参数
swapcase()		大小写互换，无参数
capitalize()	首字母大写，其他字母小写，无参数
title()			每个单词的首字母大写，无参数


格式化相关
ljust(width[, fillchar])	获取固定长度，左对齐，右边不够默认用空格补齐
rjust(width[, fillchar])	获取固定长度，右对齐，左边不够默认用空格补齐
center(width[, fillchar])	获取固定长度，居中对齐，两边边不够默认用空格补齐
zfill(width)		  		获取固定长度，右对齐，左边不够用0补齐


字符串搜索相关
find(str, beg=0, end=len(string))		搜索指定字符串，找不到返回-1
rfind(str, beg=0 end=len(string))		返回字符串最后一次出现位置，找不到返回-1
count(sub, start= 0,end=len(string))	统计字符串中某个字符串出现的次数
上面所有方法都可用index代替，不同的是使用index查找不到会抛异常，而find返回-1


字符串替换相关
replace(old, new[, max])	替换字符串，不超过 max 次
join()						将序列中的元素以指定的字符连接生成一个新的字符串

字符串去空格及去指定字符
strip([chars])		移除字符串头尾指定的字符，默认为空格
lstrip([chars])		移除字符串左边的指定字符，默认为空格
rstrip([chars])		移除字符串末尾的指定字符，默认为空格
split()				按指定字符分割字符串为数组


字符串判断相关
startswith()	检查字符串是否是以指定子字符串开头，区分大小写
endswith()		检查字符串是否是以指定子字符串结尾，区分大小写
isalnum()		是否全为字母或数字
isalpha()		是否全字母
isdigit()		是否全数字
islower()		是否全小写
isupper()		是否全大写


expandtabs() 	把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8
swapcase() 		大小写翻转
format()		格式化输出
```

format() 方法的三种使用方式：

```
# 不带参数，默认按顺序传递值
res1 = '{} {} {}'.format('Abby', 18, 'male')
print(res1)     # Abby 18 male
# 使用位置参数
res2 = '{1} {0} {1}'.format('Abby', 18, 'male')
print(res2)     # 18 Abby 18
# 使用关键字参数
res3 = '{name} {age} {sex}'.format(sex='male', age=18, name='Abby')
print(res3)     # Abby 18 male
```



**列表：**

索引、切片、加、乘、检查成员

```
append()		在列表末尾添加新对象
count()			统计某个元素在列表中出现的次数
extend()		在列表末尾一次性添加多个元素
index()			从列表中找出某个元素第一个匹配项的索引位置
insert()	按索引将新对象插入到列表中
pop()		移除列表中的一个元素（默认最后一个元素），并返回该元素的值
remove()	移除列表中某个值的第一个匹配项，没有返回值
reverse()	反转列表中元素
sort()		对原列表进行排序
clear()		清空列表
copy()		复制列表
```



**元组**

元组的元素不能修改

```
count()		统计某元素在元组中出现的次数
index()		返回指定元素首次出现的索引位置，不存在则报错
tuple(seq)		将可迭代对象转换为元组

注意
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含0或1个元素的元组的特殊语法规则
4、元组也可以使用+操作符进行拼接。
```



**字典**

```
copy()		返回一个字典的浅复制
clear() 	删除字典内所有元素
items()  	以列表返回可遍历的(键, 值) 元组数组
keys()		以列表返回一个字典所有的键
values() 	以列表返回字典中的所有值
popitem()  	返回并删除字典中的最后一对键和值
update(dict2) 	把字典dict2的键/值对更新到dict里

fromkeys()				
	创建一个新字典，以序列seq中元素做字典的键（忽略重复的元素），
	val为所有键对应的初始值
pop(key[, default])		
	删除指定键所对应的键值对，返回被删除的值。key必须指出。
	如果key不存在，则需要指定默认的返回值，否则报错
get(key, default=None)        
	返回指定键的值，如果值不在字典中返回None或default值
setdefault(key, default=None) 
	和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default


字典的特点：
    无序（不能索引）
    数据关联性强
    键值对，键值对。唯一一个映射数据类型。
    字典的键必须是可哈希的，即不可变类型。
    在同一个字典中，键(key)必须是唯一的。


字典与列表的比较：
	列表是有序的对象集合，字典是无序的对象集合。
	字典当中的元素是通过键来存取的，而不是通过偏移存取
```



### 23、lambda表达式格式以及应用场景？

```
格式：
lambda [arg1 [,arg2,.....argn]]: expression

应用场景：
Filter(), map(), reduce(), sorted()函数中经常用到，它们都需要函数形参数；
一般定义调用一次。（reduce()对参数序列中元素进行累积）

# 例子
sum = lambda arg1, arg2: arg1 + arg2
print(sum(10, 20))      # 30


注意：
lambda只是一个表达式，函数体比def简单很多
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
```



### 24、pass的作用？

```
pass一般用于站位语句，保持代码的完整性，不会做任何操作。
```



### 25、*arg和**kwarg作用

```
他们是一种动态传参，一般不确定需要传入几个参数时，可以使用其定义参数，然后从中取参

*args		代表位置参数，它会接收任意多个参数并把这些参数作为元祖传递给函数。
**kwargs	代表的关键字参数，返回的是字典，位置参数一定要放在关键字前面

同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
```



### 26、is和==的区别

```
==		判断某些值是否一样，比较的是值
is		比较的是两个实例对象是不是完全相同，比较的是内存地址（引用的内存地址不一样，唯一标识：id）
```



### 27、简述Python的深浅拷贝以及应用场景？

```
浅拷贝：
	不管多么复杂的数据结构，只copy对象最外层本身，该对象引用的其他对象不copy
	内存里两个变量的地址是一样的，一个改变另一个也改变
	浅拷贝只是增加了一个指针指向一个存在的地址
	
深拷贝：
	完全复制原变量的所有数据，内存中生成一套完全一样的内容
	只是值一样，内存地址不一样，一方修改另一方不受影响


```

一层的情况：

```
import copy

# 浅拷贝
L1 = [1, 2, 3]
L2 = L1.copy.copy(L1)
L1.append(4)
print(L1, L2)   # [1, 2, 3, 4] [1, 2, 3]

# 深拷贝
L1 = [1, 2, 3]
L2 = copy.deepcopy(L1)
L1.append(4)
print(L1, L2)   # [1, 2, 3, 4] [1, 2, 3]
```

多层的情况：

```
import copy

# 浅拷贝 指向共有的地址
li1 = [1, 2, 3, [4, 5], 6]
li2 = copy.copy(li1)
li1[3].append(7)
print(li1)     # [1, 2, 3, [4, 5, 7], 6]
print(li2)     # [1, 2, 3, [4, 5, 7], 6]

# 深拷贝 重指向
li1 = [1, 2, 3, [4, 5], 6]
li2 = copy.deepcopy(li1)
li1[3].append(7)
print(li1)      # [1, 2, 3, [4, 5, 7], 6]
print(li2)      # [1, 2, 3, [4, 5], 6]
```



### 28、Python垃圾回收机制？

引用计数、标记-清除、分代回收

**引用计数**

```
引用计数原理：
	当一个对象的引用被创建或者复制时，对象的引用计数加1；
	当一个对象的引用被销毁时，对象的引用计数减1，
	当对象的引用计数减少为0时，就意味着对象已经再没有被使用了，可以将其内存释放掉。
	
优点：
	引用计数有一个很大的优点，即实时性，任何内存，一旦没有指向它的引用，就会被立即回收，而其他的垃圾收集技术必须在某种特殊条件下才能进行无效内存的回收。
	
缺点：
	引用计数机制所带来的维护引用计数的额外操作与Python运行中所进行的内存分配和释放，引用赋值的次数是成正比的，这显然比其它那些垃圾收集技术所带来的额外操作只是与待回收的内存数量有关的效率要低。
	同时，引用技术还存在另外一个很大的问题－循环引用，因为对象之间相互引用，每个对象的引用都不会为0，所以这些对象所占用的内存始终都不会被释放掉。如下：
	
a = []
b = []
a.append(b)
b.append(a)

print(a)    # [[[...]]]
print(b)    # [[[...]]]

对于如今的强大硬件，缺点1尚可接受，但是循环引用导致内存泄露，注定python还将引入新的回收机制。(标记清除和分代收集)
```



**标记-清除**

```
标记－清除只关注那些可能会产生循环引用的对象
显然，像是PyIntObject、PyStringObject这些不可变对象是不可能产生循环引用的，因为它们内部不可能持有其它对象的引用。
Python中的循环引用总是发生在container对象之间，也就是能够在内部持有其它对象的对象，比如list、dict、class等等。这也使得该方法带来的开销只依赖于container对象的的数量

原理：
1. 寻找根对象（root object）的集合作为垃圾检测动作的起点，根对象也就是一些全局引用和函数栈中的引用，这些引用所指向的对象是不可被删除的；
2. 从root object集合出发，沿着root object集合中的每一个引用，如果能够到达某个对象，则说明这个对象是可达的，那么就不会被删除，这个过程就是垃圾检测阶段；
3. 当检测阶段结束以后，所有的对象就分成可达和不可达两部分，所有的可达对象都进行保留，其它的不可达对象所占用的内存将会被回收，这就是垃圾回收阶段。（底层采用的是链表将这些集合的对象连接在一起）

缺点：
标记和清除的过程效率不高。
```



**分代回收**

```
原理：
将系统中的所有内存块根据其存活时间划分为不同的集合，每一个集合就成为一个“代”，Python默认定义了三代对象集合，垃圾收集的频率随着“代”的存活时间的增大而减小。也就是说，活得越长的对象，就越不可能是垃圾，就应该减少对它的垃圾收集频率。

那么如何来衡量这个存活时间：
通常是利用几次垃圾收集动作来衡量，如果一个对象经过的垃圾收集次数越多，可以得出：该对象存活时间就越长。
```



### 29、Python的可变类型和不可变类型？

```
可变类型：
	列表、字典、集合
	
不可变类型：
	整型，浮点型、字符串、元祖
	
（可变与否指内存中那块内容value）
```



### 30、求结果：

```
v = dict.fromkeys(['k1', 'k2'], [])
v['k1'].append(666)
print(v)
v['k1'] = 777
print(v)
```

```
# 内存中k1和k2都指向同一个[]（内存地址相同），只要指向的[]发生变化，k1和k2都要改变(保持一致)
{'k1': [666], 'k2': [666]}
{'k1': 777, 'k2': [666]}
```



### 31、求结果：

```
def num():
return [lambda x:i*x for i in range(4)]		# 返回一个列表，里面是四个函数对象 i=3

print([m(2) for m in num()])
```

```
[6, 6, 6, 6]
原因：
	只有到需要计算i的值时，才会真正计算i的值
	函数返回值为一个列表表达式，经过4次循环结果为包含四个lambda函数的列表，由于函数未被调用，循环中的i值未被写入函数，经过多次替代，循环结束后i值为3，故结果为：6,6,6,6
```



### 32、列举常见的内置函数？

```
abs()	返回数字的绝对值
map()	
	根据函数对指定序列做映射
	map()函数接收两个参数，一个是函数，一个是可迭代对象，
	map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
	
	返回值：
		Python2 返回列表
		Python3 返回迭代器
		
filter()
	filter()函数接收一个函数 f(函数)和一个list（可迭代对象），这个函数f的作用是对每个元素进行判断，返回True或 False
	根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

isinstance() 
	判断一个对象是否是一个已知的类型，类似 type()。
	isinstance() 与 type() 区别：
        type() 不会认为子类是一种父类类型，不考虑继承关系。
        isinstance() 会认为子类是一种父类类型，考虑继承关系。
        如果要判断两个类型是否相同推荐使用 isinstance()。
        
zip()
	拉链函数
    将对象中对应的元素按顺序打包成一个个元组，
    然后返回由这些元组组成的列表迭代器。
    如果各个迭代器的元素个数不一致，则返回列表的长度与最短的对象的长度相同。
    
reduce()
	reduce() 函数会对参数序列中元素进行累积
	函数将一个数据集合(链表、元组等)中的所有数据进行下列操作
	
	注意：
		Python3已经将reduce() 函数从全局名字空间里移除了，
		它现在被放置在 fucntools 模块里，如果想要使用它，
		则需要通过引入 functools 模块来调用 reduce() 函数：
		
		
```

abs()和map()的例子：

```
def mul(x):
    return x * x

n = [1,2,3,4,5]
res = list(map(mul, n))     # 将map() 函数返回的迭代器转成列表
print(res)          # [1, 4, 9, 16, 25]

# abs() 的例子
ret = map(abs, [-1, -5, 6, -7])
print(list(ret))    # [1, 5, 6, 7]
```

filter()的例子：

```
def is_odd(x):
    return x % 2 == 1

v = list(filter(is_odd, [1,4,6,7,9,12,17]))
print(v)    # [1, 7, 9, 17]
```

map与filter对比总结：

```
参数: 都是一个函数名 + 可迭代对象
返回值: 都是返回可迭代对象

区别:
filter 是做筛选的，结果还是原来就在可迭代对象中的项
map 是对可迭代对象中每一项做操作的，结果不一定是原来就在可迭代对象中的项
```

isinstance() 的例子：

```
a = 2
print(isinstance(a, int))       # True
print(isinstance(a, str))       # False

# type() 与 isinstance() 区别
class A:
    pass

class B(A):
    pass


print("isinstance", isinstance(A(), A))     # isinstance True
print("type", type(A()) == A)               # type True

print('isinstance', isinstance(B(), A))     # isinstance True
print('type', type(B()) == A)               # type False
```

zip()的例子

```
print(list(zip([1,2,3], [5,6,7], ['a', 'b'])))      #[(1, 5, 'a'), (2, 6, 'b')]


# 例子2
a = [1, 2, 3]
b = [4, 5, 6]
c = ['a', 'b', 'c', 'd']

zab = zip(a, b)      # 打包为元组的列表，返回迭代器
print(list(zab))     # [(1, 4), (2, 5), (3, 6)]

zac = zip(a, c)     # 元素个数与最短的列表一致
print(list(zac))    # [(1, 'a'), (2, 'b'), (3, 'c')]

zab = zip(a, b)  
zba = zip(*zab)     # 与 zip 相反，可理解为解压，返回二维矩阵式
print(list(zba))    # [(1, 2, 3), (4, 5, 6)]
```

reduce() 的例子：

```
from functools import reduce


def add(x, y):
    return x + y

print(reduce(add, [1,2,3,4,5]))                 # 15
print(reduce(lambda x,y: x+y, [1,2,3,4,5]))     # 15
print(reduce(add, range(1, 101)))               # 5050
```



### 33、filter、map、reduce的作用？

**filter(function, iterable)**

过滤函数，对序列里面的元素进行筛选，最终获取符合条件的序列。新的内容少于等于原内容的时候，才能使用filter。

filter()函数用于过滤序列，过滤不符合条件的元素，返回由符合条件元素组成的心列表

```
参数：
	function 函数
	iterable 可迭代对象
	返回值:
		返回列表
```

filter() 的例子：

```
def is_odd(x):
    if x > 10:
        return True

ret = filter(is_odd, [1,4,5,7,9,12,15,17,22])
print(ret)          # <filter object at 0x0000021DFC882C48>
print(list(ret))    # [12, 15, 17, 22]
```



**map(function, iterable, ...)**

遍历序列，为每一个序列进行操作，获取一个新的序列

```
参数:
	function -- 函数
	iterable -- 一个或多个序列
	返回值:
		Python2 返回列表
		Python3 返回迭代器
```

map() 的例子：

```
# abs() 函数返回数字的绝对值
# 新的内容的个数等于原内容的个数
ret = map(abs, [-1, -5, 6, -7])
print(list(ret))
```



**reduce(function, iterable[, initializer])**

对于序列里面的所有内容进行累计操作

```
参数
    function 	-- 函数，有两个参数
    iterable 	-- 可迭代对象
    initializer -- 可选，初始参数

  - 获取序列所有元素的和
    - li = [11, 22, 33]
    - result = reduce(lambda arg1, arg2: arg1 + arg2, li)

```

reduce()的例子：

```
from functools import reduce

li = [11, 22, 33]
ret = reduce(lambda arg1, arg2: arg1+arg2, li)
print(ret)		# 66
```



### 34、一行代码实现9*9乘法表

```
print('\n'.join([' '.join(['%s*%s=%2s' % (j, i, i*j) for j in range(1, i+1)]) for i in range(1, 10)]))
```



### 35、如何安装第三方模块？以及用过哪些第三方模块？

```
安装：
可以在cmd终端下用 pip install 模块名 来进行联网安装
可以在pycharm的settings里面手动下载添加第三方模块

第三方模块：
request
django
tornado
flask
redis
pymysql
```



### 36、至少列举8个常用模块都有那些？

```
os 模块
	提供了一种方便的使用操作系统函数的方法
sys 模块
	用于提供对解释器相关的访问及维护，并有很强的交互功能
time 模块
	提供各种操作时间的函数，包括时间的访问和转换
datetime 模块
	基本的日期和时间类型
json 模块
	数据持久化方式	
pickle 模块
	Python 对象序列化，与json类似，但pickle是Python独有的
hashlib 模块
	用于加密相关的操作，代替了md5模块和sha模块
random 模块
	生成随机变量
re 模块
	正则表达式操作
math 模块
	数学函数
string 模块
	常见的字符串操作
```

```
#######################
json和pickle的比较：
	json是文本形式的存储，pickle则是二进制形式存储
	json是人可读的，pickle是不可读的
	json广泛用于包括Python在内的其他领域，pickle则是Python独有的
	json只能dump一些Python的内置对象，pickle可以存储几乎所有对象。

总结：
	如果偏向应用特别是web应用方面，可以常用JSON格式。
	如果偏向算法方面，尤其是机器学习，则应该使用 cPickle
#######################
```



### 37、re的match和search区别？

```
match：
	从字符串起始位置开始匹配，如果没有就返回 None
serch
	从字符串的起始位置开始匹配，扫描整个字符串并返回第一个成功的匹配
```



### 38、什么是正则的贪婪匹配？

```
正则表达式一般趋向于最大长度匹配，也就是所谓的贪婪匹配
```



### 39、求结果

```
[ i % 2 for i in range(10) ]
( i % 2 for i in range(10) )
```

```
[ i % 2 for i in range(10) ]	# 得到的是一个列表   [0 1 0 1 0 1 0 1 0 1]
( i % 2 for i in range(10) )	# 得到的是一个生成器
```



### 40、求结果

```
1 or 2
1 and 2
1 < (2==2)
1 < 2 == 2
```

```
1 or 2			# 1
1 and 2			# 2
1 < (2==2)		# False
1 < 2 == 2		# True
```

```
逻辑表达式：
x and y
	如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值
x or y
	如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值
	
	
为什么 "1 < 2 == 2" 得到的结果是 True？
	实际上这涉及到了Python的链式对比(Chained Comparisons)
	相当于 2 == 2 and 2 > 1
	这个式子就等价于True and True
	所以返回的结果为True
```





