
# -*- encoding: utf-8 -*-



###########################################################################################

                                                          #get_parsing_table_alternative_allele_1-0.py

############################################################################################
"""
Autor: Luis Enrique Ramírez


Descripción: se hace la intersección de los archivos,  se analizan grandes problematicas de estos y se solucionan

no recibe parametros, dentro del codigo se manda llamar a los dos archivos que tienen los datos y slos dos archivos salida con la estructura de la base de datos

"""



from collections import defaultdict
import string

with open ('genom_parsing.txt') as genom:
	with open ('snp_parsing.txt') as snp:
		with open ('./parsing_end_alter.txt','w') as alter:
			with open('./parsing_end_freq.txt', 'w') as freq:
				#diccionarios de snp, contendrán la informacion de la base de datos 
				dic_snp=defaultdict(list)  #diccionario de rs's que no esán en 1000g
				dic_snp_int=defaultdict(list) #contendrá los rs's que están en 100g
				dic_snp_type=defaultdict(list)  #contendrá el tipo de variante que para casos especiales
				dic_snp_pos=defaultdict(list)  # contendrá la cadena y la posición de final
				

				dic_geno=defaultdict(list)    #contendrá las variantes de cada rs
				dic_geno_freq=defaultdict(list)    #contendrá las frecuencias
				dic_geno_type=defaultdict(list)    #contendrá los tipos para casos especiales
				dic_geno_end=defaultdict(list)	   #contendrá la posicion de final
				
				#uni de los casos problema es Multiallelic_INDEL, que se hará a mano, los rs's que tengan esta variante se guardaran en esta lista
				multi =[]
				#para traducir una cadena
	                        trans = string.maketrans('ATGC', 'TACG')
				#recorre toda la base de datos de 1000G
				for line in genom:
					line = line.strip('\n').replace(' ','').split('\t')
					#se aislan los Multiallelic_INDEL
					if line[4] == 'Multiallelic_INDEL':
						multi.append(line[0])
						continue
					#casp base de llave que ya está en el diccionario
					if dic_geno.has_key(line[0]):
						dic_geno_freq[line[0]].append(line[5:11])
						dic_geno_end[line[0]].append(line[1])
						dic_geno_type[line[0]].append(line[4])
					#segundo caso esepecial, si es Biallelic_INDEL depende de la secuecia mas cortapra que se quede con '-'
						if line[4] == 'Biallelic_INDEL':
                                                        if len(line[2]) > len(line[3]):
                                                                dic_geno[line[0]].append('-')
                                                        if len(line[2]) < len(line[3]):
                                                                rep=line[3].replace(line[2],'',1)
								dic_geno[line[0]].append(rep)
							continue
                                                dic_geno[line[0]].append(line[3])
						continue
					#aqui cuando apenas será creado
					dic_geno_freq[line[0]] = [line[5:11]]
					dic_geno_type[line[0]] = [line[4]]
					dic_geno_end[line[0]] = [line[1]]
					#caso ruidoso
					if line[4] == 'Biallelic_INDEL':
                                        	if len(line[2]) > len(line[3]):
							rep = [line[2].replace(line[3],'',1),'-']
							dic_geno[line[0]]=rep
						if len(line[2]) <len(line[3]):
							rep=['-',line[3].replace(line[2],'',1)]
							dic_geno[line[0]]=rep
						continue
                                        dic_geno[line[0]]=[line[2],line[3]]

				doble = ['rs199809486','rs199936046','rs200693260','rs200959419','rs200962122','rs201065762','rs201766863','rs201771083','rs201785566,rs202019148']
				#en este bloque de código se llena el diccionario de snp para la intersección y la no intersección
				for line in snp:
					line = line.strip('\n').replace(' ','').split('\t')
					#si está en la intersección llenará 3 diccionarios con la información necesaria, si no solo llenará uno ya que solo sera un archivo
					if dic_geno.has_key(line[3]):
						#si la llave ya está en el diccionario solo agrega
						if dic_snp.has_key(line[3]):
							#en todo este bloque la cadena '-' se trata especialmente por algunas observaciones en el análisis de archivos
							if line[4]=='-':
								tempo = line[6].replace('/','\t').translate(trans).split('\t')
								dic_snp[line[3]].append(tempo)
								type_strand=[line[7],line[4]]
								dic_snp_type[line[3]].append(type_strand)
								dic_snp_pos[line[3]].append(line[2])
								continue
							tempo =  line[6].replace('/','\t').split('\t')
							dic_snp[line[3]].append(tempo)
							type_strand=[line[7],line[4]]
							dic_snp_type[line[3]].append(type_strand)
							dic_snp_pos[line[3]].append(line[2])
							continue
						#si no está en el diccionario lo agrega
						if line[4]=='-':
							tempo = line[6].replace('/','\t').translate(trans).split('\t')
							tempo2 = [line[5]]
							for i in range(len(tempo)):
								tempo2.append(tempo[i])
							dic_snp[line[3]]=tempo
							type_strand=[line[7],line[4]]
							dic_snp_type[line[3]]=type_strand
							dic_snp_pos[line[3]]=[line[2]]
							continue
						#
						tempo = [line[5]]
						tempo2= line[6].replace('/','\t').split('\t')
						for i in range(len(tempo2)):
							tempo.append(tempo2[i])
						dic_snp[line[3]]=tempo
						type_strand=[line[7],line[4]]
						dic_snp_type[line[3]]=type_strand
						dic_snp_pos[line[3]]=[line[2]]
					if line[3] in multi or line[3] in doble:
						continue
					
					if dic_snp_int.has_key(line[3]):
						tempo = line[6].replace('/','\t').translate(trans).split('\t')
						tempo2 = [line[5]]
						for i in range(len(tempo)):
							tempo2.append(tempo[i])
						tempo3 = [tempo2, line[2]]
						dic_snp_int[line[3]].append(tempo3)
					tempo = line[6].replace('/','\t').translate(trans).split('\t')
					tempo2 = [line[5]]
					for i in range(len(tempo)):
						tempo2.append(tempo[i])
					tempo3 = [tempo2, line[2]]
					dic_snp_int[line[3]] = tempo3
				print (dic_snp_int)
				id = 1
				#si se comparten rs se llenan las dos tablas, dependiendo del caso
				for key in dic_geno.keys():
					#caso1: el rs solo esta en 1000G, en este caso se llenan las 2 tablas solo con la informacion de 1000g
					if not dic_snp.has_key(key):
						for i in range(1,len(dic_geno[key])):
							line1=str(id) + ',' + str(key) + ',' + str(dic_geno[key][i]) + ',' + str(dic_geno_end[key][i-1])+'\n'
							line2=str(key) + ',' + str(id) + ',' + str(dic_geno_freq[key][i-1]).replace('[','').replace(']','')+'\n'
							alter.write(line1)
							freq.write(line2)
							id=id+1
					#caso2:si tambien está en snp hay tres casos 
					if dic_snp.has_key(key):
						a=set(dic_geno[key])
						b=set(dic_snp[key])
						uni=a.union(b)
						uni=list(uni)
						for i in range(len(uni)):
							if uni[i] == dic_geno[key][0]:
								continue
							#si el alelo alternativo esta solo en 1000g se llena con esta informacion
							if uni[i] in dic_geno[key] and not uni[i] in dic_snp[key]:
								ind=dic_geno[key].index(uni[i])
								line1=str(id) + ',' + str(key) + ',' + str(dic_geno[key][ind]) + ',' + str(dic_geno_end[key][ind-1])+'\n'
								line2=str(key) + ',' + str(id) + ',' + str(dic_geno_freq[key][ind-1]).replace('[','').replace(']','')+'\n'
								alter.write(line1)
								freq.write(line2)
								id=id+1
							#si solo esta en snp no se llena la tabla frecuencias
							if uni[i] not in dic_geno[key] and uni[i] in dic_snp[key]:
								ind=dic_snp[key].index(uni[i])
								line1=str(id) + ',' + str(key) + ',' + str(dic_snp[key][ind]) + ',' + str(dic_snp_pos[key][0]) + '\n'
								alter.write(line1)
								id=id+1
							#si esta en ambas se llenan las 2 tablas siempre prefiriendo snp
							if uni[i] in dic_geno[key] and uni[i] in dic_snp[key]:
								ind1=dic_geno[key].index(uni[i])
								ind2=dic_snp[key].index(uni[i])
								line1=str(id) + ',' + str(key) + ',' + str(dic_snp[key][ind2]) + ',' + str(dic_snp_pos[key][0]) + '\n'
								line2=str(key) + ',' +str(id) + ',' +  str(dic_geno_freq[key][ind1-1]).replace('[','').replace(']','') + '\n'
								alter.write(line1)
								freq.write(line2)
								id=id+1
				#aqui se llena el archivo si el no esta en la interseccion, solo se llena una tabla(de alelos alternativos) 
				for key in dic_snp_int:
					uni = set(dic_snp_int[key][0])
					uni = list(uni)
					for i in range(len(uni)):
						if uni[i]==dic_snp_int[key][0][0]:
							continue
						line=str(id)+','+str(key)+','+str(dic_snp_int[key][0][i])+','+str(dic_snp_int[key][1])+'\n'
						alter.write(line1)
						id = id+1
