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
        select_movies_query = "SELECT * FROM bid LIMIT 5"
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

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
