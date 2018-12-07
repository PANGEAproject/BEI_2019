#!usr/bin/python

##########################################################################
# Nombre: clean_triplets.py
# Autora: Diana Salazar
# Version: 1.0
# Creado: 18/11/10
# Descripcion: Obtener solo las lineas informativas por archivo 
#           de tripletas
# Output: Tripletas con la palabra de interes en alguna parte,
#           las oraciones separadas por tabuladores,
#           las busquedas sobre la primera columna de las tripletas
# Lenguaje: Python
##########################################################################

import os 

os.chdir('/export/storage/users/dsalazar/Bioinfo/output/') 

words = []
with open('/export/storage/users/dsalazar/Bioinfo/keywords/keywords.txt', 'r') as fw:
    keywords = fw.readlines()
    for k in keywords:
        words.append(k.replace('\r\n',''))

data_text = os.listdir('.')
for i in range(len(data_text)):
    with open (data_text[i], 'r') as ft:
        out = open('/export/storage/users/dsalazar/Bioinfo/p3/{}'.format(data_text[i])+'.parsed_by_the_1st', 'w')
        file = ft.readlines()
        for line in file: #Opcion 3, separando por palabras
            n = line.split('\t')
            n = str(n[1]).split(' ')
            for w in words:
                if w in n:
                    out.write(line)
        out.close()
