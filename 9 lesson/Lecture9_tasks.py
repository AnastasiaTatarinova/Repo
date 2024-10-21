'''Открытие и чтение файла:
Напишите программу, которая открывает текстовый файл
sample.txt и выводит его содержимое на экран.'''
with open('../../sample.txt') as file:
    content = file.read()
    print(content)

'''Запись в файл: Напишите программу, которая создает новый текстовый файл output.txt
и записывает в него строку "Hello, World!".'''
with open('../../output.txt', 'w+') as file:
    file.write('Hello, World!')
    file.seek(0)
    content = file.read()
    print(content)

'''Создание файла с числовыми данными: Напишите программу, которая создает файл
numbers.txt и записывает в него числа от 1 до 5, каждое на новой строке.'''
with open('../../numbers.txt', 'w+') as file:
    for i in range(1,6):
        file.write(str(i)+'\n')
    file.seek(0)
    content = file.read()
    print(content)

'''Добавление данных в файл: Напишите программу, которая открывает файл output.txt в
режиме добавления и записывает в него строку "Appending this line.".'''
with open('../../output.txt', 'a+') as file:
    file.write('\n'+''"Appending this line.")
    file.seek(0)
    content = file.read()
    print(content)

'''Подсчет строк в файле: Напишите программу, которая открывает файл sample.txt и
подсчитывает количество строк в этом файле.'''
with open('../../sample.txt') as file:
    list = file.readlines()
    lines = 0
    for i in list:
        lines += 1
print(f'Lines in file: {lines} ')

'''Чтение и запись файлов: Напишите программу, которая открывает файл input.txt,
читает его содержимое, затем создает новый файл copy.txt и записывает туда
прочитанные данные.'''
with open('../../input.txt') as file:
    initialFile = file.read()
with open('../../copy.txt', 'w+') as fileCopy:
    fileCopy.write(initialFile)
    fileCopy.seek(0)
    copiedFile = fileCopy.read()
    print(copiedFile)

'''Чтение файла и вывод конкретных строк: Напишите программу, которая открывает файл
data.txt и выводит только те строки, которые содержат слово "Python"'''
with open('../../data.txt') as file:
    content = file.readlines()
    for i in content:
        if 'Python' in i:
            print(i)





