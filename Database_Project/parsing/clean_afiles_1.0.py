# -*- encoding: utf-8 -*-

###########################################################################################

									#clean_afiles_1.0.py

############################################################################################

"""Descrición
Autor: Luis Enrique

Version: 1.0

parametros: no recibe parametros, se tiene que correr en la carpeta donde están los archivos de snp138_col.txt, 1000GP_Phase_all_col.txt y rs_parsing.txt

el objetivo de este programa es tener los archivos de snp y 1000g solo con los rs's correctos

la lista de rs's correctos se compara con los archivos de snp138 y 1000GP y arroja solo los rs's correcos

1) snp: nombre del archivo de snp138
2) geno: nombre del archivo de 1000G
3) parcing: lista de rs's parceados 
4) snp_parsing: archivo de salida de los rs's parseados de snp
5) genom_parsing: archivo de salida de los rs's parseados de 1000GP
6) pars: set donde se guardan los rs's correctos
"""

from collections import defaultdict
with open ('./snp138_col.txt') as snp:
	with open ('./1000GP_Phase3_all_col.txt') as geno:
		with open ('./rs_parsing.txt') as parcing:
			with open ('./snp_parsing.txt', 'w') as snp_parsing:
				with open('./genom_parsing.txt','w') as genom_parsing:
					pars=set()
#se guardan todos los rs's correctos en el set
					for line in parcing:
						line=line.strip('\n')
						pars.add(line)
#por cada archivo se pregunta si la linea cuenta con algún rs correcto, si es así lo escribe en el archivo final
					for line in snp:
						line = line.strip('\n').split('\t')
						if line[3] in pars:
							snp_parsing.write(str(line).replace(',','\t').replace('\'', '').replace('[','').replace(']','') + '\n')
					for line in geno:
						line = line.strip('\n').split('\t')
						if line [0] in pars:
							genom_parsing.write(str(line).replace(',', '\t').replace('\'', '').replace('[','').replace(']','')  + '\n')
