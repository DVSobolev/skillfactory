# Задание: Доработайте код итогового проекта, расширив его список команд.
# Добавьте еще команды, которые, на ваш взгляд, могут быть полезны для этой задачи.

import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить и редактировать данные по оценкам, предметам и ученикам
        5. Вывести информацию по всем оценкам для определенного ученика
        6. Вывести средний балл по каждому предмету по определенному ученику
        7. Вывести словарь с оценками
        8. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # Выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4: # Добавьте возможность удалять и редактировать данные по оценкам, предметам и ученикам.
        print('4. Удалить и редактировать данные по оценкам, предметам и ученикам')
        # считываем имя ученика
        student = input(f"Введите имя ученика: ")
        print('''
            Возможные действия:
            1 - удалить ученика,
            2 - изменить имя ученика,
            3 - удалить предмет,
            4 - изменить наименование предмета,
            5 - удалить оценку,
            6 - изменить оценку.
            ''')
        if student in students_marks.keys():
            action = int(input("Введите цифру, которая соответсвует действию с учеником: "))
            if action == 1:
                del students_marks[student]
                print(f'Ученик {student} удален')
            elif action == 2:
                new_student = input(f"Введите новое имя ученика взамен {student}: ")
                students_marks[new_student] = students_marks[student]
                del students_marks[student]
                print(f'Имя ученика {student} изменено на {new_student}')
            elif action == 3:
                class_ = input('Введите название предмета для удаления: ')
                if class_ in students_marks[student]:
                    del students_marks[student][class_]
                    print(f"Предмет {class_} удалён у ученика {student}")
                else:
                    print(f"Предмет {class_} не найден")
            elif action == 4:
                class_ = input('Введите название предмета, который хотите заменить: ')
                new_class = input('Введите название нового предмета: ')
                if class_ in students_marks[student]:
                    students_marks[student][new_class] = students_marks[student][class_]
                    del students_marks[student][class_]
                    print(f"Предмет {class_} изменён на {new_class}")
                else:
                    print(f"Предмет {class_} не найден")
            elif action == 5:
                class_ = input('Введите название предмета, для которого хотите удалить оценку: ')
                if class_ in students_marks[student]:
                    print(f'Оценки: {students_marks[student][class_]}')
                    mark = int(input('Введите оценку, которую хотите удалить: '))
                    if mark in students_marks[student][class_]:
                        students_marks[student][class_].remove(mark)
                        print(f"Оценка {mark} удалена")
                        print(students_marks)
                    else:
                        print(f"Оценка {mark} не найдена")
                else:
                    print(f"Предмет {class_} не найден")
            elif action == 6:
                class_ = input('Введите название предмета, для которого хотите изменить оценку: ')
                if class_ in students_marks[student]:
                    print(f'Оценки: {students_marks[student][class_]}')
                    mark = int(input('Введите оценку, которую хотите изменить: '))
                    new_mark = int(input('Введите новую оценку: '))
                    # if mark in students_marks[student][class_]:
                    for mark_ in range(len(students_marks[student][class_])):
                        if students_marks[student][class_][mark_] == mark:
                            students_marks[student][class_][mark_] = new_mark
                            break
                        print(f"Оценка {mark} изменена на {new_mark}")
                    else:
                        print(f"Оценка {mark} не найдена")
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 5: # Добавьте вывод информации по всем оценкам для определенного ученика.
        print('5. Вывести информацию по всем оценкам для определенного ученика')
        # считываем имя ученика
        student = input(f"Введите имя ученика: ")
        # имя ученика введено верно
        if student in students_marks.keys():
            # Ввод переменной для суммирования оценок
            class_sum = 0
            for key, value in students_marks.items():
                if key == student:
                    for key_, value_ in value.items():
                        # Цикл по оценкам по всем предматам
                        for elem in value_:
                            # Суммирование всех оценок по всем предматам
                            class_sum += elem
            # Вывод суммы оценок по всем прдеметам
            print(f'Сумма оценок по всем прдеметам ученика {student} = {class_sum}')
        # имя ученика введено неверно
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 6: # Добавьте вывод среднего балла по каждому предмету по определенному ученику.
        print("6. Вывести средний балл по каждому предмету по определенному ученику")
        # считываем имя ученика
        student = input(f"Введите имя ученика: ")
        # имя ученика введено верно
        if student in students_marks.keys():
            for key, value in students_marks.items():
                if key == student:
                    print(f'У ученика {student}:')
                    for key_, value_ in value.items():
                        # Подсчёт среднего балла по каждому предмету
                        print(f'Средний балл по предмету {key_} = {(sum(value_)/len(classes)):.2f}')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 7:
        # выводим словарь с текущими оценками:
        print(f'Текущий словарь с оценками:')
        print()
        for student in students:
            print(f'''{student}
                    {students_marks[student]}''')
    elif command == 8:
        print('8. Выход из программы')
        break