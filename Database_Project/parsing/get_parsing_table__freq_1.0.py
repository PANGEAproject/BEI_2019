# -*- encoding: utf-8 -*-

###########################################################################################

									#get_parsing_table__freq_1.0.py

############################################################################################

"""Descrición
Autor: Luis Enrique

Version: 1.0

parámetros: no tiene parametros, se corre en la carpeta donde se encuentra genom_parsing.txt

el objetivo de este programa es conseguir las columnas de la atabla de frecuencias

ya que la estructura de la tabla de frecuencias solo requiere los rs's y las frecuencias se recorre el archivo parseado de 1000genomas,en donde está la intersección y los que no están en snp que son los únicos que cunetan con frecuencia

1) geno: nombre del archivo que contiene los rs's correctos de mil genomas
2) final: nombre que se le da al archivo de salida
3) line: el archivo se recorre por línea y se separa por tabuladores
4) tempo: variable temporal donde se le da la estuctura a la line que se esccribirá en el archivo final

"""

with open ('./genom_parsing.txt') as geno:
	with open('./parsing_end_2.txt', 'w') as final:
		for line in geno:
			line = line.strip('\n').replace(' ','').split('\t')
			temp = str(line[0]).replace('[','').replace(']','').replace('\'','').replace(' ','')+','+','+str(line[5:11]).replace('[','').replace(']','').replace('\'','').replace(' ','')+'\n'
			final.write(temp)
