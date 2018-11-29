###########################################################################################

                                                  #load_tables.sql

############################################################################################

#se inicia secion en sql con la opcion --local-infile para cargar archivos
mysql -p --local-infile
#se usa nuestra base de datos
USE PANGEA_DB
SET GLOBAL local_infile = "ON";
#se inserta la tabla rs
LOAD DATA LOCAL INFILE '/home/luisrs/storage/Project/bin/parsing_end.txt' INTO TABLE RS FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
#se inserta la tabla alelos alternativos
LOAD DATA LOCAL INFILE '/home/luisrs/storage/Project/bin/parsing_end_alter.txt' INTO TABLE ALTERNATIVE_ALLELE FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
#se crea la tabla frecuencias
LOAD DATA LOCAL INFILE '/home/luisrs/storage/Project/bin/parsing_end_freq.txt' INTO TABLE FREQUENCY_RS_CONTINENT FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
SET GLOBAL local_infile = "OFF";
