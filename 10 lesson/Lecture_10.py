'''1. Простая функция: Напишите функцию greet, которая принимает одно имя в качестве
аргумента и выводит строку "Hello, [name]!".'''
def greet(name):
    print(f'Hello, {name}')

greet('Anastasia')

'''2. Функция сложения: Напишите функцию, которая принимает два числа в качестве
аргументов и возвращает их разницу.'''
def minus(a,b):
    minus = a-b
    return minus

print(minus(3,4))

'''3. Функция с дефолтным параметром: Напишите функцию welcome, которая принимает
два аргумента — имя и сообщение, причем сообщение по умолчанию равно "Welcome!".
Функция должна выводить сообщение вида: "Welcome, [name]!".'''
def welcome(name, message='Welcome'):
    print(f'{message}, {name}!')

welcome('Ivan')
#welcome('Kate', 'Hello')

'''4. Функция с несколькими аргументами: Напишите функцию multiply, которая
принимает любое количество чисел в качестве аргументов и возвращает их произведение.'''
def multiply(*args):
    result = 1
    for i in args:
        result *=i
    return result

print(multiply(2,3,4))

'''5. Функция для деления: Напишите функцию divide, которая принимает два числа и
возвращает результат их деления. Предположите, что второй аргумент всегда будет
ненулевым. Примените эту функцию для нескольких пар чисел.'''
def divide(a,b):
    #if b == 0:
        #print('Second argument has inccorect value')
        #b = int(input('Enter another value '))
    return a/b

print(divide(1,2))
print(divide(10,5))
print(divide(647,7))
#print(divide(647,0))