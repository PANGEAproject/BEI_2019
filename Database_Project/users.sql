-----------------------------------------------------------------------------------------------------------

-- Nombre: users.sql
-- Autora: Diana Salazar
-- Version 1.0
-- Creado: 25/11/10
-- Descripción: Creación de la tabla de usuarios
-- Lenguaje: MySQL

create table USERS(

	users varchar(50) not null, 
    passwords varchar (50) not null, 

	constraint users primary key(users)

	)ENGINE=InnoDB;
