#!usr/bin/python

##########################################################################
# Nombre: get_triplets.py
# Autora: Diana Salazar
# Version: 1.0
# Creado: 18/11/10
# Descripcion: Obtner las tripletas de cada archivo con los articulos de 
#           Salmonella
# Output: Por cada archivo en el directorio text-pdftxtractor regresa un
#           archivo con sus tripletas correspondientes
# Lenguaje: Python
##########################################################################

import os 

os.chdir("/export/apps/corenlp")        # Situarse en la carpeta donde esta instalado CoreNLP
data_text = os.listdir("/export/storage/users/dsalazar/Bioinfo/text-pdftxtractor")      # Listar a todas los archivos de Salmonella
for i in range(len(data_text)):         # Para cada archivo, obtener las tripletas y mandarlas a un nuevo archivo en la carpeta 'output'
    os.system("java -mx4g -cp stanford-corenlp-3.9.1.jar:stanford-corenlp-3.9.1-models.jar:CoreNLP-to-HTML.xsl:slf4j-api.jar:slf4j-simple.jar edu.stanford.nlp.naturalli.OpenIE  /export/storage/users/dsalazar/Bioinfo/text-pdftxtractor/{} > /export/storage/users/dsalazar/Bioinfo/output/{}".format(data_text[i],data_text[i]+'.out'))