# -*- encoding: utf-8 -*-

###########################################################################################

									#clean_afiles_1.0.py

############################################################################################

"""Descrición
Autor: Luis Enrique

Version: 1.0

el objetivo de este programa es tener los archivos de snp y 1000g solo con los rs's correctos
"""

from collections import defaultdict
with open ('./snp138_col.txt') as snp:
	with open ('./1000GP_Phase3_all_col.txt') as geno:
		with open ('./rs_parsing.txt') as parcing:
			with open ('./snp_parsing.txt', 'w') as snp_parsing:
				with open('./genom_parsing.txt','w') as genom_parsing:
					pars=set()
					for line in parcing:
						line=line.strip('\n')
						pars.add(line)
					for line in snp:
						line = line.strip('\n').split('\t')
						if line[3] in pars:
							snp_parsing.write(str(line).replace(',','\t').replace('\'', '').replace('[','').replace(']','') + '\n')
					for line in geno:
						line = line.strip('\n').split('\t')
						if line [0] in pars:
							genom_parsing.write(str(line).replace(',', '\t').replace('\'', '').replace('[','').replace(']','')  + '\n')
