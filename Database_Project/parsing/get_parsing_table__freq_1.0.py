# -*- encoding: utf-8 -*-

###########################################################################################

									#get_parsing_table__freq_1.0.py

############################################################################################

"""Descrición
Autor: Luis Enrique

Version: 1.0

el objetivo de este programa es conseguir las columnas de la atabla de frecuencias

"""

with open ('./genom_parsing.txt') as geno:
	with open('./parsing_end_2.txt', 'w') as final:
		for line in geno:
			line = line.strip('\n').replace(' ','').split('\t')
			temp = str(line[5:11]).replace('[','').replace(']','').replace('\'','').replace(' ','')+','+str(line[0]).replace('[','').replace(']','').replace('\'','').replace(' ','')+'\n'
			final.write(temp)
