# --------------------------------------- 字符串 ------------------------------------------------
# -*- coding: UTF-8 -*-
# 1.字符串大小写
name = "ada lovelace"
print(name.title())  # title() 以首字母大写的方式显示每个单词， 即将每个单词的首字母都改为大写
print(name.upper())  # upper() 转换为大写
print(name.upper())  # lower() 转换为小写

# 2.合并（拼接）字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

print("Languages:\nPython\nC\nJavaScript")
print(r"Languages:\nPython\nC\nJavaScript")

# 3.删除空白
favorite_language = 'python '
favorite_language.rstrip()  # 要确保字符串末尾没有空白，可使用方法rstrip()
favorite_language.lstrip()  # 要确保字符串开头没有空白，可使用方法lstrip()
favorite_language.strip()  # 要确保字符串开头和结尾没有空白，可使用方法lstrip()

# --------------------------------------- 数字 ------------------------------------------------
# 1.使用函数str() 避免类型错误
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)

age = 23
message = "Happy " + str(age) + "rd Birthdaty!"
print(message)

# --------------------------------------- 列表list ------------------------------------------------
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])  # 取列表的最后一个元素

for name in bicycles:
    sentence = "Hello, " + name + " World!"
    print(sentence)

for i in range(0, len(bicycles)):
    sentence = "Hello, " + bicycles[i] + " World!"
    print(sentence)

# 1.pop()方法
popped_bicycles = bicycles.pop()  # 被删除的额值存储在 popped_bicycles 变量中
print(popped_bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)  # pop()删除指定位置的元素
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# 如果你不确定该使用del 语句还是pop() 方法， 下面是一个简单的判断标准： 如果你要从列表中删除一个元素， 且不再以任何方式使用它， 就使用del 语句； 如果你要在删除元素后还能继续使用它， 就使用方法pop() 。

# 2.remove()方法: 不知道要删除的元素的位置，只知道要删除的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

# 3.实例
['Katy', 'Mary', 'Gigi', 'Bob', 'David', 'Jack', 'Cathy', 'Ann', 'John', 'Betty']
roster = ['Mary', 'Bob', 'Cindy', 'Jack', 'Cathy', 'Ann', 'John']
# for name in roster:
#     invitation = "Hello, " + name + ",I hope you can jon my birthday party in my house!"
#     print(invitation)
roster[2] = 'David'
roster.insert(0, 'Katy')
roster.insert(2, 'Gigi')
roster.append('Betty')
for i in range(0, len(roster)):
    while i < len(roster) - 2:
        loser_name = roster.pop(i)
        print("Hello, " + loser_name + ",I am sorry!" + str(len(roster)))
    print("Hello, " + roster[i] + ",I hope you can jon my birthday party in my house!")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 类似深拷贝（完全独立）
my_foods.append('orange')
friend_foods.append('apple')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # 类似浅拷贝
my_foods.append('orange')
friend_foods.append('apple')

# --------------------------------------- 字典 ------------------------------------------------
# 1.实例1
aliens = []
color = ['yellow', 'green']
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print('------------------')
print("Total number of aliens: " + str(len(aliens)))

# 2.实例2
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(username, user_info)
    for key, values in user_info.items():
        print(key, values)

# --------------------------------------- 用户输入和while循环 ------------------------------------------------
message = input('Tell me something,and I will repeat it back to you')
print(message)

name = input('Please input your name')
print("Hello," + name)

age = int(input('How old are you?'))
print(type(age))

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
while True:  # 以while True打头的循环，将不断执行
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Python continue 语句跳出本次循环，而break跳出整个循环。
# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
# continue语句用在while和for循环中。
for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print('当前字母 :', letter)

for letter in 'Python':  # 第一个实例
    if letter == 'h':
        break
    print('当前字母 :', letter)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# --------------------------------------- 函数 ------------------------------------------------
# 注意：Python将非空字符串解读为True
# 1.实例1
def build_person(firstname, lastname, age=''):
    person = {'first': 'firstname', 'last': 'lastname'}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', '34')
print(musician)


# 2.实例2
def get_formatted_name(firstname, lastname):
    full_name = firstname + ' ' + lastname
    return full_name.title()


while True:
    print('\nPlease enter your name: ')
    print("(enter 'q' at any time to quit)")

    f_name = input('Firstname: ')
    if f_name == 'q':
        break
    l_name = input('Lastname: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


# 3.实例3
def print_models(umprinted_designs, completed_models):
    while umprinted_designs:
        current_design = umprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
