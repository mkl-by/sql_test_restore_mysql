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
        # select_bid = """SELECT  client_number, outcome
        #                 FROM bid JOIN event_value
        #                 WHERE bid.play_id = event_value.play_id """

        select_bid = """SELECT client_number as client, 
                                SUM(outcome = "win") as win, 
                                SUM(outcome = "lose") AS lose 
                                -- SUM(CASE WHEN outcome = "win" OR outcome = "lose" THEN 1 ELSE 0 END) AS Totalwinlose 
                        FROM bid
                        INNER JOIN event_value
                        ON bid.play_id = event_value.play_id
                        GROUP BY client_number; """
        
        with connection.cursor() as cursor:
            cursor.execute(select_bid)
            result = cursor.fetchall()
            print('+----------------------------------+')
            print('|Пользователь |', 'Побед |', 'Поражений |')
            print('+----------------------------------+')

            for n, win, lose in result:
                #  print(f'{n} {win} {lose}', end='\n')
                print('|', ' '*3, n, ' '*5,
                      '|', ' ', win,
                      ' |', ' '*2, lose, '    |'
                      )
            print('+----------------------------------+')


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
