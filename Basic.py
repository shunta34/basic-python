# 実行
# print('Good evening')
# print('Good afternoon')
# print('Good morning')



# 変数
# num = 1
# num01 = 2
# num_01 = 3
# num$01 = 4
# num-01 = 5
# 01num = 6
# NUM = 1
# Num = 2
# return = 10

# print(num)
# print(num01)
# print(num_01)
# print(num$01)
# print(num-01)
# print(01num)
# print(NUM)
# print(Num)
# print(return)



# データ型
# num01 = 123
# num02 = 1.23
# string_a = 'Hello,World!'
# a = 10
# b = 1
# bool01 = (a > b)
# bool01 = (a < b)

# print(type(num01))
# print(type(num02))
# print(string_a)
# print(type(string_a))
# print(bool01)
# print(type(bool01))



# リスト
# a = ['sato', 'suzuki', 'takahashi']
# a[1] = 'tanaka'
# a = [['sato', 'suzuki'], ['takahashi', 'tanaka']]

# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[0][0])
# print(a[0][1])
# print(a[1][0])
# print(a[1][1])



# 演算子
# x = 10
# y = 2
# z = 10
# x = 8
# y = 3
# y = 12
# z = 20
# x += 10
# z += y

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x > y)
# print(x <= y)
# print(x >= z)
# print(x == y)
# print(x != y)
# print(x >= 5 and x <= 10)
# print(y >= 5 and y <= 10)
# print(x == 3 or y == 3)
# print(x == 1 or y == 1)
# print(x)
# print(z)



# # 条件分岐
# age = 22
# age = 18
# age = 0

# if age >= 20:
#   print('adult')
# elif age == 0:
#   print('baby')
# else:
#   print('child')



# 繰り返し
# for i in range(5):
#   print(i)

# for i in range(5):
#   if i == 3:
#     break
#   print(i)

# for i in range(5):
#   if i == 3:
#     continue
#   print(i)

# for i in range(3):
#   for j in range(3):
#     print(i, j, sep = '-')

# arr = [2, 4, 6, 8, 10]

# for i in arr:
#   print(i)

# sum = 0
# for i in arr:
#   sum += i
#   print(sum)



# 関数
# def say_hello():
#   print('hello world')

# say_hello()
# say_hello()
# say_hello()

# def say_hello(greeting):
#   print(greeting)

# say_hello('hello world')
# hello = say_hello
# hello('Good Morning')

# def add(num01, num02):
  # print(num01 + num02)
  # return (num01 + num02)

# add(6, 2)
# print(add(6, 2))
# add_result = add(6, 2)
# print(add_result)

# def div(a, b, c):
#   return (a + b + c) / 3

# div_result = div(9, 4, 2)
# print(div_result)



# クラス
# class Student:
  # def __init__(self):
    # self.name = ''

  # def __init__(self, name):
  #   self.name = name

  # def avg(self, math, english):
  #   print((math + english) / 2)

# a001 = Student()
# a001.avg(80, 70)
# a001.avg(30, 70)
# a001.name = 'sato'
# a001 = Student('sato')
# a002 = Student()
# a002.name = 'tanaka'
# a002 = Student('tanaka',)

# print(a001.name)
# print(a001.gender)
# print(a002.name)



# 実践
class Student:
  def __init__(self, name):
    self.name = name

  def calculate_avg(self, data):
    sum = 0

    for num in data:
      sum += num

    avg = sum / len(data)
    return avg

  def judge(self, avg):
    if(avg >= 60):
      result = 'passed'
    else:
      result = 'failed'
    return result

a001 = Student('sato')
# data = [70, 65, 50, 90, 30]
data = [70, 65, 50, 10, 30]
avg = a001.calculate_avg(data)
result = a001.judge(avg)

print(avg)
print(a001.name + ' ' + result)
