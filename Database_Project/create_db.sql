
###########################################################################################

                                                    #create_db.sql

############################################################################################
##Descripcion
#Autor: Jesus Velez
#Descripcion Este programa de sql crea la base de datos donde se guardaran los datos decuerdo con nuestro diagrama entidad relacion

#se crea la base de datos que utilizaremos
CREATE DATABASE PANGEA_DB;
USE PANGEA_DB;

-- RS
#se crea la tabla rs que contendra cromosoma, variacion,cadena,fuente, posicion de inicio y el link de cada rs a NCBI
CREATE TABLE RS
(
 rs_id            VARCHAR(15) NOT NULL ,
 reference_allele VARCHAR(1000) NOT NULL ,
 chromosome
ENUM('chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY') ,
 variation        ENUM('unknown', 'single', 'in-del', 'het', 'microsatellite', 'named', 'mnp', 'insertion', 'deletion', 'Multiallelic_SNP', 'Multiallelic_INDEL', 'Biallelic_SNP', 'Biallelic_INDEL') NOT NULL ,
 strand           ENUM('+','-') ,
 source           ENUM('SNP138','1000GP','SNP138-1000GP') NOT NULL ,
 start_position   INT unsigned ,
 link_NCBI VARCHAR(100) NOT NULL,
#se usa el propio rs como llave primaria 
PRIMARY KEY (rs_id)
);

-- ALTERNATIVE_ALLELE
#la tabla de alelo alternativo contendra cada alelo alternativo de cada rs, su posicion de fin 
CREATE TABLE ALTERNATIVE_ALLELE
(
 id_alternative_allele INT NOT NULL AUTO_INCREMENT ,
 rs_id                 VARCHAR(15) NOT NULL ,
 alternative_allele    VARCHAR(1000) NOT NULL ,
 end_position          INT unsigned NOT NULL ,
#se crea un id interno
PRIMARY KEY (id_alternative_allele, rs_id),
KEY `fkIdx_25` (rs_id),
#se conecta con la tabla rs, por cada rs hay uno o mas alelos
CONSTRAINT `FK_25` FOREIGN KEY `fkIdx_25` (rs_id) REFERENCES RS (rs_id)
);


-- FREQUENCY_RS_CONTINENT
#se crea la tabla de frecuencias con todas las frecuencias de cada alelo alternativo, si tiene
CREATE TABLE FREQUENCY_RS_CONTINENT
(
 rs_id        VARCHAR(15) NOT NULL ,
 id_alternative_allele INT NOT NULL,
 AFR          FLOAT unsigned NOT NULL, 
 AMR          FLOAT unsigned NOT NULL, 
 EAS          FLOAT unsigned NOT NULL, 
 EUR          FLOAT unsigned NOT NULL, 
 SAS          FLOAT unsigned NOT NULL,
 GLOBAL       FLOAT unsigned NOT NULL, 
#se crea un llave primaria compuesta de las 2 llaves foraneas (se conecta con alelo alternativo y con rs)
PRIMARY KEY (rs_id,id_alternative_allele),
CONSTRAINT `FK_rsid` FOREIGN KEY (rs_id) REFERENCES RS (rs_id),
CONSTRAINT `FK_alter` FOREIGN KEY (id_alternative_allele) REFERENCES ALTERNATIVE_ALLELE (id_alternative_allele)
);
