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
        if k.lower() in words:
            pass
        else:
            words.append(k.replace('\r\n','').lower())

data_text = os.listdir('.')
for i in range(len(data_text)):
    with open (data_text[i], 'r') as ft:
        out = open('/export/storage/users/dsalazar/Bioinfo/p3v2/{}'.format(data_text[i])+'.parsed_by_the_1st_v2', 'w')
        file = ft.readlines()
        for line in file: #Opcion 3, separando por palabras
            tempo = line.split('\t')
            tempo = str(tempo[1]).split(' ')
            for t in tempo:
                if t.lower() in words:
                    out.write(line)
        out.close()
