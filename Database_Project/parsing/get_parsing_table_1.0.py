# -*- encoding: utf-8 -*-

###########################################################################################

									#get_parsing_table_1.0.py

############################################################################################

"""Descrición
Autor: Luis Enrique

Version: 1.0

el objetivo de este programa es conseguir las columnas de l atabla de rs

"""

from collections import defaultdict
with open ('./snp_parsing.txt') as snp:
	with open ('./genom_parsing.txt') as geno:
		with open ('./parsing_end.txt', 'w') as parsing:
			all_geno = defaultdict(list)
			all_snp = defaultdict(list)
			for line in geno:
				line = line.strip('\n').split('\t')
				if all_geno.has_key(line[0]):
					continue
				else:
					all_geno[line[0]].append(line[2])
					all_geno[line[0]].append('\N')
					all_geno[line[0]].append(line[4])
					all_geno[line[0]].append('\N')
					all_geno[line[0]].append('1000GP')
					all_geno[line[0]].append('\N')
			for line in snp:
				line = line.strip('\n').split('\t')
				if all_snp.has_key(line[3]):
					continue
				else:
					all_snp[line[3]].append(line[5])
					all_snp[line[3]].append(line[0])
					all_snp[line[3]].append(line[7])
					all_snp[line[3]].append(line[4])
					all_snp[line[3]].append('SNP138')
					all_snp[line[3]].append(line[1])
			print (len(all_snp))
			print(len(all_geno))
			for i in all_geno:
				if all_snp.has_key(i):
					continue
				tempo = str(i) + ',' + str(all_geno[i]).strip('[').strip(']') + '\n'
			for i in all_snp:
				if all_geno.has_key(i):
					tempo = str(i) + ',' +  str(all_snp[i]).strip('[').strip(']').replace('SNP138','SNP138-1000GP') + '\n'
					parsing.write(tempo)
					continue
				tempo = str(i) + ',' +  str(all_snp[i]).strip('[').strip(']') + '\n'
				parsing.write(tempo)

