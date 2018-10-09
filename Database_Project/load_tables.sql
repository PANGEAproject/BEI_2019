mysql -u -p --local-infile
USE PANGEA_DB
SET GLOBAL local_infile = "ON";
LOAD DATA LOCAL INFILE '/home/luisrs/storage/Project/bin/parsing_end.txt' INTO TABLE RS FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/luisrs/storage/Project/bin/parsing_end_2.txt' INTO TABLE FREQUENCY_RS_CONTINENT FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
SET GLOBAL local_infile = "OFF";
