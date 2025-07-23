# Вам нужно считать данные из файла, обработать их и найти с помощью данных следующую информацию:
# 1. Какой номер самого дорого заказа за июль?
# 2. Какой номер заказа с самым большим количеством товаров?
# 3. В какой день в июле было сделано больше всего заказов?
# 4. Какой пользователь сделал самое большое количество заказов за июль?
# 5. У какого пользователя самая большая суммарная стоимость заказов за июль?
# 6. Какая средняя стоимость заказа была в июле?
# 7. Какая средняя стоимость товаров в июле?

import json

with open(r'C:\Users\Дмитрий\Desktop\orders_july_2023.json', 'r') as f:
    translator_json = f.read()

translator = json.loads(translator_json)

print('''
    Возможные действия:
    1. Какой номер самого дорого заказа за июль?
    2. Какой номер заказа с самым большим количеством товаров?
    3. В какой день в июле было сделано больше всего заказов?
    4. Какой пользователь сделал самое большое количество заказов за июль?
    5. У какого пользователя самая большая суммарная стоимость заказов за июль?
    6. Какая средняя стоимость заказа была в июле?
    7. Какая средняя стоимость товаров в июле?
    8. Выход из программы
    ''')

order_ = ''

while True:
    command = int(input('Введите номер действия: '))
    if command == 1:  # 1. Какой номер самого дорого заказа за июль?
        max_price = 0

        for order_id, order in translator.items():
            if order['date'][-2:] == '07':
                if order['price'] > max_price:
                    order_ = order_id
                    max_price = order['price']
        print(f'Самый дорогой заказ – это № {order_} с ценой = {max_price} р.')
    elif command == 2:  # 2. Какой номер заказа с самым большим количеством товаров?
        max_quantity = 0

        for order_id, order in translator.items():
            if order['quantity'] > max_quantity:
                order_ = order_id
                max_quantity = order['quantity']
        print(f'Заказ № {order_} с самым большим количеством товаров = {max_quantity}')
    elif command == 3:  # 3. В какой день в июле было сделано больше всего заказов?
        day = ''
        max_quantity = 0

        for order_id, order in translator.items():
            if order['quantity'] > max_quantity:
                day = order['date'][-2:]
                max_quantity = order['quantity']
        print(f'За {day} июля было сделано больше всего заказов = {max_quantity}')
    elif command == 4:  #  4. Какой пользователь сделал самое большое количество заказов за июль?
        max_quantity = 0
        user_id = ''

        for order_id, order in translator.items():
            if order['date'][-2:] == '07':
                if order['quantity'] > max_quantity:
                    user_id = order['user_id']
                    max_quantity = order['quantity']
        print(f'Пользователь {user_id} сделал самое большое количество заказов за июль = {max_quantity}')
    elif command == 5:  # 5. У какого пользователя самая большая суммарная стоимость заказов за июль?
        user_totals = {}

        for order_id, order in translator.items():
            if order['date'][5:7] == '07':
                user_id = order['user_id']
                order_total = order['price'] * order['quantity']
                if user_id in user_totals:
                    user_totals[user_id] += order_total
                else:
                    user_totals[user_id] = order_total

        max_user = ''
        max_total = 0

        for user_id, total in user_totals.items():
            if total > max_total:
                max_user = user_id
                max_total = total
        print(f"У пользователя {max_user} самая большая суммарная стоимость заказов за июль = {max_total}")
    elif command == 6: #  6. Какая средняя стоимость заказа была в июле?
        orders_in_july = []

        for order_id, order in translator.items():
           if order['date'][-2:] == '07':
               orders_in_july.append(order['price'])
        average_price_in_july = sum(orders_in_july)/len(orders_in_july)
        print(f'Cредняя стоимость заказа в июле = {average_price_in_july:.2f}')
    elif command == 7:  # 7. Какая средняя стоимость товаров в июле?
        product_in_july = []

        for order_id, order in translator.items():
            if order['date'][-2:] == '07':
                product_in_july.append(order['price'] * order['quantity'])
        average_price_product_in_july = sum(product_in_july) / len(product_in_july)
        print(f'Cредняя стоимость товаров в июле = {average_price_product_in_july:.2f}')
    elif command == 8:
        break
    else:
        print("Неизвестная команда")
