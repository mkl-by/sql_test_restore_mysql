# Backup
docker exec CONTAINER /usr/bin/mysqldump -u root --password=root DATABASE > backup.sql

# Restore
cat backup.sql | docker exec -i CONTAINER /usr/bin/mysql -u root --password=root DATABASE


SELECT 
    client_number as client, 
    SUM(outcome = "win") as win , 
    SUM(outcome = "lose") AS lose, 
    SUM(CASE WHEN outcome = "win" OR outcome = "lose" THEN 1 ELSE 0 END) AS Totalwinlose 
FROM bid
INNER JOIN event_value
ON bid.play_id = event_value.play_id
GROUP BY client_number 