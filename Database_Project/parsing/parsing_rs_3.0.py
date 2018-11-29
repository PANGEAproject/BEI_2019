# -*- encoding: utf-8 -*-


###########################################################################################

									#parsing_rs_2.0.py

############################################################################################

"""Descrición
Autor: Luis Enrique

Version: 2.0

Descripción: El programa filtra los rs's de acuerso con los siguientes parametros: que los rs's en el archivo de snp138 no esten en 2 cromosomas, que sus posiciones de inicio concuerden y que estén en los cromosomas 5, 9, 7 y 21.
En el archio de 1000 genomas filtra aquellos que tuvieran posciciones diferentes (lo cual no pasa)  y aquellos que tuvieran incongruencias con la posición final o en algunos casos la posición inicial en snp138.
finalmente se resta a los rs's filtrados de 1000 genomas los rs's que están mal en snp y se hace la unión de ambos

Parametros:
	1) Path del archivo de snp138 (previamente procesado por el scrip 'get_colums_1.0.sh')
	2) Path del archivo de 1000 genomas (previamente procesado por el scrip 'get_colums_1.0.sh')
	3) path del archivo donde se escribirán los rs's que se hayan filtrado

Ejemplo de uso: python parsing_rs_2.0.py 
output 1: introduce la direccion del archivo snp138:
input 1: './snp138_col.txt'

output 2: introduce la direccion del archivo 1000G:
input 2: './1000GP_Phase3_all_col.txt'

output 3: introduce la direccion del archivo snp138:
input 3: './rs_parsing.txt'

funciones:
1) rs_correct_1000G: funcion que crea un diccionario para guardar la posición de cada rs's en 1000 genomas, manda llamar a rs_correct_snp
2) rs_correct_snp: crea un diccionario de snp donde en las llaves guarda chr,posicion de inicio y final, si no se repiten (lo cual indica que son incorrectos) agrega mas valores al diccionario y eso se filtra junto con los cromosomas pedidos por el usuario. Manda a llamar a correct_intersection y con el set resultado de ésta y con el resultado del filtrado hace la unión final
3) correct_intersectio: si un rs esta en la intersección checa que su posición en 1000 genomas coincida con la de snp (inicio o final) y lo agrega al set que regresará la función. Si el rs no está en snp lo agrega sin preguntar.

Variables:

a) rs_file, geno_file. resul_file: direcciones de los archivos
b) union_rs: variable que contendrá el set que regresarán las funciones con la union de los correctos en 1000 genomas y snp138
c) genom: nombre que se le da al archivo de 1000 genomas
d) dic_1000: diccionario que contendrá la posición 
e) end: variable que contendrá el resultado final de la función
f) snp: nombre para el archivo de snp138
g) dic_rs_pos: diccionario que como valores contendrá cromosoma, pisición de inicio y posición de final
h) rs_geno: variable que contendrá un set que en la función correct_intersection donde se filtraran los rs's en la intersección que tengan incongruencia en las posiciones
i) chromo: lista de los cromosomas que deben estar en la base de datos 
j) mal_chr: set que contendrá los rs's que están mal(incongruencia en cromosoma o posición) para posteriormente quitarlos de 1000 genomas
k) chr: set donde se guardarán los rs's correctos deacuerdo con las rubricas indicadas anteriormente
l) uni: variable que contienen la unión de los rs's ya filtrados

"""
from collections import defaultdict
def rs_correct_100G(file1,file2):
	with open (file1) as genom:
		dic_1000 = defaultdict(list)
		for line in genom:
			line = line.strip('\n').split('\t')
			if line [0] in dic_1000:
				if line[1] in dic_1000[line[0]]:
					continue
			dic_1000[line[0]].append(line[1])
		for i in dic_1000:
			if len(dic_1000[i]) != 1:
				del dic_1000[i]
		end = rs_correct_snp(file2, dic_1000)
		return(end)

def rs_correct_snp (file2, dic_1000):
	with open (file2) as snp:
		dic_rs_pos = defaultdict(list)
		for line in snp:
			line = line.strip('\n').split('\t')
			if line[3] in dic_rs_pos:
				if line[0] == dic_rs_pos[line[3]][0] and line[1] == dic_rs_pos[line[3]][1]: 
					continue 
			dic_rs_pos[line[3]].append(line[0])
			dic_rs_pos[line[3]].append(line[1])
			dic_rs_pos[line[3]].append(line[2])
                rs_geno,mal_rs_geno = correct_intersection(dic_rs_pos, dic_1000)
                chromo = ['chr5','chr9','chr17','chr21']
                mal_chr=set()
                chr = set()
                for i in dic_rs_pos.keys():
                        if 'chr' not in  str(dic_rs_pos[i][2:len(dic_rs_pos[i])]):
                                if dic_rs_pos[i][0] in chromo:
                                        chr.add(i)
                        else:
                                mal_chr.add(i)
                rs_geno = rs_geno - mal_chr
                uni = chr.union(rs_geno)
                uni = (uni - mal_rs_geno) - mal_chr
                return(uni)




def correct_intersection (dic_rs_pos, dic_1000):
        rs_geno = set()
        mal_rs_geno = set()
        for key in dic_1000.keys():
                if dic_rs_pos.has_key(key):
                        if  dic_1000[key][0] in dic_rs_pos[key]:
                                rs_geno.add(key)
                        else :
                                mal_rs_geno.add(key)
                        continue
                rs_geno.add(key)
        print (mal_rs_geno)
        print (len(mal_rs_geno))
        print('longitud purificado 1000G: ' + str(len (rs_geno)))
        return(rs_geno, mal_rs_geno)


rs_file = input('introduce la direccion del archivo snp138:\n')
geno_file = input('introduce la direccion del archivo 1000G:\n')
resul_file = input('introduce la direccion del archivo de resultados:\n')

with open (resul_file, 'w') as exit:
        union_rs = rs_correct_100G(geno_file,rs_file)
        for i in union_rs:
                exit.write(i + '\n')

