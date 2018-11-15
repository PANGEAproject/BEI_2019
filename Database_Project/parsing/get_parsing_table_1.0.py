# -*- encoding: utf-8 -*-

###########################################################################################

									#get_parsing_table_1.0.py

############################################################################################

"""Descrición
Autor: Luis Enrique

Version: 1.0

parametros: no tiene ningún parametro, se tiene que correr en la carpeta donde están snp_parsing.txt y genom_parsing.txt

el objetivo de este programa es conseguir las columnas de la atabla de rs

el archivo de snp138 tiene todos los datos de esta tabla, por lo que si no está en la intersección solo se agrega, si está en la intersección solo se cambia la fuente (SNP138-1000GP) y su está solo en 1000GP pone NULL en todos los campos que no cuenta 1000GP.

1) snp: nombre del archivo de snp con los rs's correctos
2) geno: nombre del archivo de 1000GP con los rs's correctos
3) parsing: nombre del archivo donde se escribirá el resultado
4) all_geno: nombre del diccionario que contendrá los datos de 1000G requeridos en la tabla de RS, si no está es NULL
5) all_snp: nombre del diccionario que contensrá los datos de snp requeridos en la tabla de RS, este documento los tiene todos.


"""


from collections import defaultdict
with open ('./snp_parsing.txt') as snp:
	with open ('./genom_parsing.txt') as geno:
		with open ('./parsing_end.txt', 'w') as parsing:
			all_geno = defaultdict(list)
			all_snp = defaultdict(list)
#en este par de ciclos se guardan los datos útiles de cada uno de los 2 archivos, en 1000G ens NULL si no lo hay# 
			for line in geno:
				line = line.strip('\n').replace(' ','').split('\t')
				if all_geno.has_key(line[0]):
					continue
				else:
					all_geno[line[0]].append(line[2])
					all_geno[line[0]].append('NULL')
					all_geno[line[0]].append(line[4])
					all_geno[line[0]].append('NULL')
					all_geno[line[0]].append('1000GP')
					all_geno[line[0]].append('NULL')
			for line in snp:
				line = line.strip('\n').replace(' ', '').split('\t')
				if all_snp.has_key(line[3]):
					continue
				else:
					all_snp[line[3]].append(line[5])
					all_snp[line[3]].append(line[0])
					all_snp[line[3]].append(line[7])
					all_snp[line[3]].append(line[4])
					all_snp[line[3]].append('SNP138')
					all_snp[line[3]].append(line[1])
#si el rs solo está en 1000G se imprime lo que tiene en el diccionario
			for i in all_geno:
				if all_snp.has_key(i):
					continue
				tempo = str(i) + ',' + str(all_geno[i]).replace('[','').replace(']','').replace('\'','').replace('NULL', '\N').replace(' ','') + ',' + 'https://www.ncbi.nlm.nih.gov/snp/' + str(i) + '\n'
				parsing.write(tempo)
#si el rs está en ambas bases se escribe lo que está en SNP, pero con la fuente cambiada
			for i in all_snp:
				if all_geno.has_key(i):
					tempo = str(i) + ',' +  str(all_snp[i]).replace('[','').replace(']','').replace('\'','').replace('SNP138','SNP138-1000GP').replace(' ','')+ ',' + 'https://www.ncbi.nlm.nih.gov/snp/' + str(i) + '\n'
					parsing.write(tempo)
					continue
#si no está en la intersección solo se escribe la información de SNP
				tempo = str(i) + ',' +  str(all_snp[i]).replace('[','').replace(']','').replace('\'','').replace(' ','') + ',' + 'https://www.ncbi.nlm.nih.gov/snp/' + str(i) + '\n'
				parsing.write(tempo)

