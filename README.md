Тестовое SQL
--------------------------------------

Имеется урезанная БД букмекерской конторы, в которой имеются следующие таблицы:

1)event_entity,  в которой имеются  столбцы play_id - идентификатор игры, sport_name - название спорта, home_team и away_team - название домашней и выездной команды соответственно;

2) event_value, в которой хранятся play_id - идентификатор игры, value - коэффициент на определённый исход, attribute - исход события, outcome - сыграла ставка либо нет;

3) bid, в которой имеются столбцы b_id - идентификатор ставки, client_number - идентификатор клиента, play_id - идентификатор игры, amount - сумму, которую поставил клиент, coefficient - коэффициент, на который поставил клиент.

Задание
-----------------------

1. Необходимо написать запрос, который находит  сколько ставок сыграло и не сыграло у каждого пользователя. Неполный результат запроса представлен на рисунке sql/result_1.png.

2. Необходимо написать запрос, который находит сколько раз между собой играли команды. Важно, если команда А играла против команды В, а затем команда В играла против команды А, то это считается как одно и тоже событие. То есть, результат должен быть следующим: А против В - 2 игры.  Неполный результат запроса представлен на рисунке sql/result_2.png.

СУБД: MySQL
Дамп БД находится в sql/test_task_sql.sql

# Backup
docker exec CONTAINER /usr/bin/mysqldump -u root --password=root DATABASE > backup.sql

# Restore
cat backup.sql | docker exec -i CONTAINER /usr/bin/mysql -u root --password=root DATABASE
