## 第2部分 Python基础篇（80题-II）



### 41、def func(a, b=[]) 这种写法有什么坑？

```
函数传参为列表陷阱，列表是可变数据类型，可能会在过程中修改里面的值
```

```
def func(a, b = []):
    b.append(1)
    print(a, b)

func(a = 2)     # 2 [1]
func(2)         # 2 [1, 1]
func(2)         # 2 [1, 1, 1]
```



### 42、如何实现 “1,2,3” 变成 [‘1’,’2’,’3’] ?

```
"1,2,3".split(',')
```



### 43、如何实现[‘1’,’2’,’3’]变成[1,2,3] ?

```
[int(x) for x in ['1', '2', '3']]
```



### 44、比较：`a=[1,2,3] 和 b=[(1),(2),(3)] 以及 c=[(1,),(2,),(3,)]` 的区别？

```
前两个列表内是int
最后一个列表内是元组
```

 补充：a=[1,2,3,4,5]，b=a和c=a[:]，有区别么？

```
b = a 		复制的是a的引用，修改b会印象到a
c = a[:]	产生一个新列表，修改c不影响a
```



### 45、如何用一行代码生成 [1,4,9,16,25,36,49,64,81,100] ?

```
[i*i for i in range(1, 11)]
```



### 46、一行代码实现删除列表中重复的值 ?

```
a = [1,2,3,3,4,5,5,5,6,7]

a = [*set(a)]
print(a)
```



### 47、如何在函数中设置一个全局变量 ?

```
通过global指定变量，该变量会变成全局变量
```

```
a = 100
b = 200

def func():
    global a, b
    a = 1000
    b = 2000

func()
print(a)
print(b)
```



### 48、logging模块的作用？以及应用场景？

```
作用：
	管理程序的执行日志，省去用print记录操作日志的操作，并且可以将标准输入输出保存到日志文件
	在程序的出现故障快速定位出错地方及故障分析
	
场景：
	爬虫爬取数据时，对爬取进行日志记录，方便分析、排错。
	主要有5个level:
		DEBUG
		INFO
		WARNING
		ERROR
		CRITICAL
```



### 49、请用代码简单实现stack(栈)

```
class Stack(object):
    # 初始化栈
    def __init__(self):
        self.items = []
    # 判断栈是否为空
    def is_empty(self):
        return self.items == []
    # 返回栈顶
    def peek(self):
        return self.items[len(self.items) - 1]
    # 返回栈大小
    def size(self):
        return len(self.items)
    # 压栈
    def push(self, item):
        self.items.append(item)
    # 出栈
    def pop(self):
        return self.items.pop()
```

实例代码：

```

class Stack(object):
    # 初始化栈
    def __init__(self):
        self.items = []
    # 判断栈是否为空
    def is_empty(self):
        return self.items == []
    # 返回栈顶
    def peek(self):
        return self.items[len(self.items) - 1]
    # 返回栈大小
    def size(self):
        return len(self.items)
    # 压栈
    def push(self, item):
        self.items.append(item)
    # 出栈
    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    stack = Stack()
    stack.push("H")
    stack.push("I")

    print(stack.is_empty())     # False
    print(stack.peek())         # I
    print(stack.size())         # 2
    print(stack.pop())          # I
```



### 50、常用字符串格式化有哪几种？

```
%	占位符
s = '%s' % 'abc'
print(s)

format 格式化输出
s = '{}'.format('abc')
print(s)
```

```
# 最方便的
# 缺点：需一个个的格式化
print('%s and %s' % ('aa', 'bb'))

# 最好用的
# 优点：不需要一个个的格式化，可以利用字典的方式，缩短时间
print('%(a)s and %(b)s' % {'a': 'aaa', 'b': 'bbb'})

# 最先进的
# 优点：可读性强
print('{a} and {b}'.format(a='aa', b='bb'))
```



### 51、简述 生成器、迭代器、可迭代对象，以及应用场景？

```
迭代器
	含有__iter__和__next__方法 (包含__next__方法的可迭代对象就是迭代器)

生成器
	包括含有yield这个关键字，生成器也是迭代器，调动next把函数变成迭代器
	
可迭代对象
	一个类内部实现__iter__方法且返回一个迭代器
```

应用场景：

```
生成器
	range/xrange
		py2：
			range() 会立即创建
			xrange() 生成器
		py3：
			range() 生成器
```



### 52、用Python实现一个二分查找的函数

```
L = [1,2,3,4,5,6,7,8,9,10]

def search(s, str, start=0, end=None):
    """
    :param s:
    :param str:
    :param start:
    :param end:
    :return:
    """
    end = len(str) if end is None else end
    middle = start + (end - start) // 2
    if start < end:
        if s > str[middle]:
            return search(s, str, start=middle + 1, end=end)
        elif s < str[middle]:
            return search(s, str, start=start, end=middle - 1)
        else:
            return '找到了，目标索引是：%s' % middle
    return '找不到这个值'


print(search(1, L))
```



### 53、谈谈你对闭包的理解？

```
闭包函数就是内部的函数调用外部函数的变量，常用于装饰器。
判断闭包函数的方法：__closure__，输出的__closure__有cell元素说明是闭包函数

闭包的意义与应用：
	延迟计算
	装饰器就是闭包函数的一种应用场景
闭包的意义：      
	返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域
```



### 54. os和sys模块的作用？

```
os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口
sys模块负责程序与Python解释器的交互，提供了一系列的函数和变量，用于操控Python的运行时环境
```



### 55、如何生成一个随机数？

```
import random

print(random.random())          # 0.6403188679102396
print(random.randint(1, 10))    # 7   
```



### 56、如何使用python删除一个文件？

```
import os
file = r'D:\test.txt'

if os.path.exists(file):
    os.remove(file)
    print('delete success')
else:
    print('no such file:%s' % file)
```



### 57、谈谈你对面向对象的理解？

```
面对对象是一种编程思想，以类的眼光来来看待事物的一种方式。将有共同的属性和方法的事物封装到同一个类中。

封装
	将有共同的属性和方法封装到同一个类中
继承
	如果很多类中都有共同的方法，为了避免重复代码，就可以将方法提取到基类中实现，让所有派生类去继承即可
多态
	指基类的同一个方法在不同派生类中有着不同功能。Python天生支持多态。
```



### 58、Python面向对象中的继承有什么特点？

```
继承概念的实现方式主要有两种：实现继承、接口继承
	实现继承：使用基类的属性和方法而无需额外编码的能力
	接口继承：仅使用属性和方法的名称，但是子类必须提供实现的能力（子类重构父类的方法）
	
继承分为单继承和多继承
	Python是支持多继承的
	如果没有指定基类，Python的类默认继承 Object 类，Object类是所有Python类的基类
	
Python3中的继承机制
	子类在调用某个方法或变量的时候，首先在自己的内部查找，如果没有找到，则开始根据继承机制在父类中查找
	根据父类定义中的顺序，以深度优先的额方式逐一查找父类
	继承参数的书写有先后顺序，写在前面的被优先继承
```



### 59、面向对象深度优先和广度优先是什么？

```
Python的类可以继承多个类，Python的类如果继承了多个类，那么其查找父类的方式有两种
	当类是经典类时，多继承情况下，会按照深度优先方式查找
	当类时新式类时，多继承情况下，会按照广度优先方式查找
	简单说就是：
		经典类时纵向查找，新式类时横向查找
		
经典类和新式类的区别
	在声明类的时候，新式类需要加上object关键字
	在Python3中默认全是新式类
```



### 60、面向对象中super的作用？

```
主要在子类继承父类的所有属性和方法时来使用
```



### 61、是否使用过functools中的函数？其作用是什么？

```
在装饰器中，会用到
	functools.wraps() 主要在装饰器中用来装饰函数

Stark上下文管理源码中，走到视图阶段时有用到functools中的偏函数
	request = LocalProxy(partial(_lookup_req_object, 'request'))
	
functools的reduce() 函数，用于对可迭代对象进行累计操作
```



### 62、列举面向对象中带双下划线的特殊方法，如：`__new__`、`__init__`

```
__new__
	生成实例    
__init__
	生成实例的属性

__dict__
	存储对象属性的一个字典，其键为属性名，值为属性的值
	
__str__ 和 __repr__
	这两个方法都是用于显示的
	__str__ 是面向用户的
	__repr__ 是面向程序员
	
__del__
	当对象的所有引用都被删除后触发该方法
	
__get__
	访问属性，返回属性的值
__set__
	设置属性值，不返回任何内容
__delete__
	删除属性，不返回任何内容
	
__class__
	表示当前操作的对象的类是什么	obj.__class__
	
__call__
	实例对象加( )会执行def __call__:... 方法里边的内容。

__doc__
	类的描述信息，该描述信息无法被继承
```



### 63、如何判断是函数还是方法

```
看它的调用者是谁
	如果是类调用它，需要传入参数self，这时就是一个函数
	如果调用者是对象，不需要传入参数值self，这时是一个方法
```



### 64、静态方法和类方法区别？

```
静态方法可以没有任何参数

```

```
def static_func():
    """静态方法，无默认参数"""
    print('静态方法')


def class_func(cls):
    """ 定义类方法，至少有一个cls参数 """
    print('类方法')

static_func()
class_func(abs)
```



### 65、列举面向对象中的特殊成员以及应用场景

```
__doc__			表示类的描述信息。
__module__ 		表示当前操作的对象在那个模块；
__class__		表示当前操作的对象的类是什么。
__init__ 		构造方法，通过类创建对象时，自动触发执行。
__call__ 		对象后面加括号，触发执行。
__dict__ 		类或对象中的所有成员。
__str__ 		如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值。
__getitem__、__setitem__、__delitem__
	用于索引操作，如字典。以上分别表示获取、设置、删除数据。
__iter__ 		用于迭代器，之所以列表、字典、元组可以进行for循环，是因为类型内部定义了 __iter__。
```



### 66、1、2、3、4、5 能组成多少个互不相同且无重复的三位数

题意理解：组成后的数值不相同，且组合的三个位数之间数字不重复

使用python内置的排列组合函数（不放回抽样排列）
product 		笛卡尔积　　（有放回抽样排列）
permutations 	排列　　（不放回抽样排列）
combinations 	组合,没有重复　　（不放回抽样组合）
combinations_with_replacement 	组合,有重复　　（有放回抽样组合）

```
import itertools

a = [1,2,3,4,5]

print(len(list(itertools.permutations(a, 3))))		# 60个
```



### 67、什么是反射？以及应用场景？

```
反射的核心本质就是以字符串的形式去导入个模块，利用字符串的形式去执行函数。

# 应用场景：
rest framework里面的CBV
```



### 68、metaclass作用？以及应用场景？

```
metaclass用来指定类是由谁创建的。
类的metaclass 默认是type。我们也可以指定类的metaclass值。
```



### 69、用尽量多的方法实现单例模式

```
1、使用模块

Python的模块就是天然的单例模式。因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。



2、使用装饰器



3、使用类



4、基于 `__new__` 方法实现
```



### 70、装饰器的写法以及应用场景

```
基本含义
	装饰器本质就是函数，为其他函数添加附加功能
原则
	不修改被修饰的函数的代码
	不修改被修饰函数的调用方式

应用场景
	无参装饰器在用户登录认证中常见
	有参装饰器在flask的路由系统中见到过
	高阶函数
	闭包
	装饰器
	functools.wraps(func)
```

实例：

```
import functools


def wrapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('这是个装饰器')
        return func
    return inner


@wrapper
def index():
    print('这是被装饰的函数')
    return None


index()

```



### 71、异常处理写法以及如何主动抛出异常（应用场景）

```
while True:
    try:
        x = int(input("请输入一个数字："))
        break
    except ValueError:
        print("错误, 输入的不是数字，请重试")
```

主动抛出异常：

```
class NetWorkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
        try:
            raise NetWorkError("Bad hostname")
        except NetWorkError as e:
            print(e.args)
```



### 72、什么是面向对象的mro

```
MRO：方法解析顺序
它定义了 Python 中多继承存在的情况下，解释器查找继承关系的具体顺序
```



### 73、isinstance作用以及应用场景？

```
判断一个对象是否是一个已知的类型
```

应用场景：rest framework 认证的流程



### 75、json序列化时，可以处理的数据类型有哪些？如何定制支持datetime类型？

```
可序列化的数据类型
	字典、列表、数字、字符串、如果是元组，则自动转成列表
```

自定义时间序列化转换器：

```
import json
from json import JSONEncoder
from datetime import datetime

class ComplexEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return super(ComplexEncoder, self).default(o)


d = {'name': 'Abby', 'data': datetime.now()}
print(json.dumps(d, cls=ComplexEncoder))    # {"name": "Abby", "data": "2020-02-28 20:47:55"}
```



### 76、json序列化时，默认遇到中文会转换成unicode，如果想要保留中文怎么办？

在序列化时，中文汉字总是被转换为unicode码

在dumps函数中添加参数ensure_ascii=False即可解决。

```
import json

a = json.dumps({"xxx": '你好'}, ensure_ascii=False)
b = json.dumps({"xxx": '你好'})

print(a)        # {"xxx": "你好"}
print(b)        # {"xxx": "\u4f60\u597d"}
```



### 77、什么是断言？应用场景？

```
assert 断言：条件成立则继续往下执行代码，否则抛出异常
一般用于：
	运行时检查程序逻辑
	检查约定
	程序常量
```



### 78、有用过with statement吗？它的好处是什么？

```
with语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作。
释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。
```



### 79、使用代码实现查看列举目录下的所有文件

```
import os

# path = os.listdir(os.getcwd())
path = os.listdir('.')      # 查看列举目录下的所有文件

print(path)
```



### 80、简述 yield和yield from关键字

```
yield 使用
	1 函数中使用yield可以是函数变成生成器，其本质是封装了__iter__和__next__方法的迭代器
		一个函数如果是生成一个数组，就必须把数据存储在内存中，
		如果使用生成器，则在调用的时候才生成数据，可以节省内存。
	2 生成器方法调用时，不会立即执行。需要调用 next() 或者使用for循环来执行。
	
yield from 使用
	为了让生成器（带yield的函数）能简易的在其他函数中直接调用，就产生了yield from
```













































