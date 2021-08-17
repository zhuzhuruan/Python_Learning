# --------------------------------------- 类 ------------------------------------------------
# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 例如: 工厂加工生产一批小猪玩具,流程为: 制作嘴巴\鼻子\耳朵\眼镜\手\腿等,可以把这些步骤写成一个一个的方法,但是如果要再制作小狗玩具呢,同样是鼻子\耳朵\眼睛等的方法,要重新写一次吗?
#      所以可以将这些相似的方法\属性等放在类中,继承这个类

# 面向对象重要的概念就是类(Class)和实例(Instance)，类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

# 1.类的定义与实例的创建
#   注意：我们定义的类都会继承于object类，当然也可以不继承object类；两者区别不大，但没有继承于object类使用多继承时可能会出现问题。

class Circle(object):  # 创建Circle类,Circle是类名
    pass  # 此处可添加属性和方法


circle1 = Circle()  # 创建实例使用 类名+()，类似函数调用的形式创建。
circle2 = Circle()

# 2.类中的实例属性和类属性
# 类的属性是用来表明这个类是什么的。类的属性分为实例属性与类属性两种: 实例属性用于区分不同的实例；
#                                                        类属性是每个实例的共有属性。
# 区别：实例属性每个实例都各自拥有，相互独立；而类属性有且只有一份，是共有的属性。

# 2.1、实例属性: 类的属性都是用来指明这个类"是什么"，实例属性是用来区分每个实例不同的基础。
# 在上面我们创建了Circle类，大家都知道所有圆都具备半径这个通用属性，下面我们为circle1、circle2 圆实例添加半径 r 这个属性并赋值。
circle1.r = 1  # r为实例属性
circle2.R = 2
print(circle1.r)  # 使用 实例名.属性名 可以访问我们的属性
print(circle2.R)


# 两个实例的属性名称不统一不利于后面的访问和使用，而且每次在创建圆后我们要再为实例添加属性会比较麻烦，所以我们可以在创建实例时给类初始属性。
# 在定义 Circle 类时，可以为 Circle 类添加一个特殊的 __init__() 方法，当创建实例时，__init__() 方法被自动调用为创建的实例增加实例属性。
class Circle(object):
    def __init__(self, r):  # 初始化一个属性r(不要忘记self参数,它是类下面所有方法必须的参数)
        self.r = r


# 创建实例时就必须要提供除 self 以外的参数：
circle1 = Circle(1)
circle2 = Circle(2)
print(circle1.r)
print(circle2.r)


# 注意：实例名.属性名 circle1.r 访问属性，是我们上面Circle类__init__() 方法中 self.r 的 r 这个实例属性名，而不是__init__(self, r)方法中的 r 参数名，如下更加容易理解：
class Circle(object):
    def __init__(self, R):  # 约定成俗这里应该使用r，它与self.r中的r同名
        self.r = R


circle1 = Circle(1)
print(circle1.r)  # 我们访问的是小写r


# 面试喜欢问的问题：创建类时，类方法中的self是什么？
# self 代表类的实例，是通过类创建的实例 (注意，在定义类时这个实例我们还没有创建，它表示的我们使用类时创建的那个实例)

# 3. 类属性
# 绑定在实例上的属性不会影响其他实例，但类本身也是一个对象，如果在类上绑定属性，则所有实例都可以访问该类的属性，并且所有实例访问的类属性都是同一个！！！
# 记住，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。
# 圆周率π为圆的共有属性，我们可以在Circle类添加pi这个类属性
class Circle(object):
    pi = 3.14  # 类属性

    def __init__(self, r):
        self.r = r  # 实例属性


circle1 = Circle(1)
circle2 = Circle(2)
print('------未修改前------')
print('pi=\t', Circle.pi)
print('circle1=\t', circle1.pi)
print('circle2=\t', circle2.pi)
print('------通过类名修改后------')
Circle.pi = 3.14159  # 通过类名修改类属性，所有实例的类属性被改变
print('pi=\t', Circle.pi)
print('circle1=\t', circle1.pi)
print('circle2=\t', circle2.pi)
print('----通过circle1实例名修改后-----')
circle1.pi = 3.14111  # 实际上这里是给circle1创建了一个与类属性同名的实例属性
print('pi=\t', Circle.pi)
print('circle1.pi=\t', circle1.pi)  # 实例属性的访问优先级比类属性高，所以是3.14111
print('circle2.pi=\t', circle2.pi)

# 仔细观察我们通过类创建的实例修改的类属性后，通过其他实例访问类属性他的值还是没有改变。其实是通过实例修改类属性是给实例创建了一个与类属性同名的实例属性而已，
# 实例属性访问优先级比类属性高，所以我们访问时优先访问实例属性，它将屏蔽掉对类属性的访问。
print('----删除circle1实例属性pi-----')
del circle1.pi
print('pi=\t', Circle.pi)
print('circle1.pi=\t', circle1.pi)
print('circle2.pi=\t', circle2.pi)


# 4.python类的实例方法
# 方法是表明这个类用是来做什么
# 在类的内部，使用 def 关键字来定义方法，与一般函数定义不同，类方法必须第一个参数为 self, self 代表的是类的实例（即你还未创建类的实例），其他参数和普通函数是完全一样。

class Circle(object):
    pi = 3.14  # 类属性
    __weight = 2  # 定义私有属性,私有属性在类外部无法直接进行访问

    def __init__(self, r):
        self.r = r  # 实例属性

    def get_area(self):
        return self.r ** 2 * Circle.pi  # 通过实例修改pi的值对面积无影响，这个pi为类属性的值
        return self.r ** 2 * self.pi  # 通过实例修改pi的值对面积我们圆的面积就会改变


circle1 = Circle(2)
print(circle1.get_area())
print(circle1.weight)


# 注意：示例中的 get_area(self) 就是一个方法，它的第一个参数是 self 。__init__(self, name)其实也可看做是一个特殊的实例方法。
# 在方法的内部需要调用实例属性采用 "self.属性名 " 调用。示例中 get_area(self) 对于 pi 属性的引用 Circle.pi 与 self.pi 存在一定区别。
# Circle.pi 使用的是类属性 pi，我们通过创建的实例去修改 pi 的值对它无影响。self.pi 为实例的 pi 值，我们通过创建的实例去修改 pi 的值时，由于使用 self.pi 调用的是实例属性，
# 所以 self.pi 是修改后的值。调用实例的方法中使用实例属性可采用 实例名.方法名(除self的参数) 使用。

# --------------------------------------- 单继承 ------------------------------------------------
# 类定义
class People(object):
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        # 调用父类的构函
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = Student('ken', 10, 60, 3)
s.speak()


# --------------------------------------- 多继承 ------------------------------------------------
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


# --------------------------------------- 实例1 ------------------------------------------------
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " roll over!")


my_dog = Dog("willie", 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


# ---------------------------------------- 实例2 ------------------------------------------------
class Car(object):
    def __init__(self, make, model, year):  # 实例属性
        self.odometer_reading = 0
        self.make = make
        self.model = model
        self.year = year
        # self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car = Car("subaru", 'outback', 2013)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23500)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()


# ---------------------继承-----------------
# super() : 是一个特殊函数， 帮助Python将父类和子类关联起来。 这行代码让Python调用ElectricCar 的父类的方法__init__() ， 让ElectricCar 实例包含父类的所有属性。 父类也称为超类
#          （superclass） ， 名称super因此而得名。
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # Car.__init__(self, make, model, year)    # super().和Car.()的小区别
        # self.battery_size = 70
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):  # 重写父类方法
        print("This car has a tank")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()


# 将实例用作属性
class Battery(object):
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.__init__(80)
my_tesla.battery.describe_battery()

