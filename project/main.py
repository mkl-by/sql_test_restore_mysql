import os
from time import sleep
from mysql.connector import connect, Error

sleep(2)
try:
    #  подключаемся MySQL
    with connect(
        host="my_db",
        port=3306,
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database="db_mysql",
    ) as connection:
        #  если подключились
        print("MYSQL:", connection)
        select_event = "SELECT play_id, outcome FROM event_value LIMIT 5"
        select_bid = """SELECT  client_number, outcome  
                        FROM bid JOIN event_value
                        WHERE bid.play_id = event_value.play_id 
                        
                        """
        select = "SELECT play_id FROM event_entity LIMIT 5"
        with connection.cursor() as cursor:
            cursor.execute(select_bid)
            result = cursor.fetchall()
            a = dict()
            b = set(result)  # выбираем
            print(b)
            a['win'] = []
            a['lose'] = []
            # делаем словарь с 2-мя ключами
            for i in b:
                a[i[1]].append([i[0], result.count(i)])
            # выводим на экран
            print('+---------------------------------------+')
            print('|Пользователь |', 'Побед |', 'Поражений |')
            print('+---------------------------------------+')
            for i in range(len(a['win'])):
                print('|', ' '*3, sorted(a['win'])[i][0], ' '*5,
                      '|', ' ', sorted(a['win'])[i][1],
                      ' |', ' '*2, sorted(a['lose'])[i][1], '    |'
                      )
            print('+---------------------------------------+')




except Error as e:
    # если ошибка
    print("ERROR:", e)







def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('ok')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
