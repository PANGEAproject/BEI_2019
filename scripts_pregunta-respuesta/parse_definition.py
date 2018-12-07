#!usr/bin/python

##########################################################################
# Nombre: get_key_sentences.py
# Autora: Diana Salazar
# Version: 1.0
# Creado: 18/11/10
# Descripcion: Obtener solo las lineas informativas por archivo 
#           de tripletas
# Output: Obtener oraciones informativas para que es y que hace una ente biologico
# Lenguaje: Python
##########################################################################

import os
import json

################################### Funciones ###################################

def get_words(path):
    words = []
    with open(path, 'r') as fw:
        keywords = fw.readlines()
        for k in keywords:
            if k.lower() in words:
                pass
            else:
                words.append(k.replace('\r\n','').lower())
        return words

def get_verbs(path):
    with open(path, 'r') as v:
        return v.readlines()

def get_products_tabs(path, words):
    products_salmonella = {}
    with open(path, 'r') as fs:
        file = fs.readlines()
        for line in file:
            n = line.split('\t')[1]
            if n.lower() in words:
                try:
                    products_salmonella[n.lower()].append(line)
                except KeyError:
                    products_salmonella[n.lower()] = [line]
    return products_salmonella

def get_products_by_1st(path, words):
    products_salmonella = {}
    with open (path, 'r') as fs:
        file = fs.readlines()
        for line in file:
            tempo = line.split('\t')
            tempo = str(tempo[1]).split(' ')
            for n in tempo:
                if n.lower() in words:
                    try:
                        products_salmonella[n.lower()].append(line)
                    except KeyError:
                        products_salmonella[n.lower()] = [line]
    return products_salmonella

def get_verbal_sentences(dict_products, verbs):
    products_by_verbs = {}
    for k in dict_products:
        products_by_verbs[k] = {}     
        for line in dict_products[k]:
            verb = line.split('\t')[2]
            # print k, verb
            #if verb in verbs:
            #    if verb in products_by_verbs[k]:
            #        products_by_verbs[k][verb].append(line)
            #    else:
            #        products_by_verbs[k][verb] = [line]
            if verb in verbs:
                try:
                    products_by_verbs[k][verb].append(line)
                except KeyError:
                    products_by_verbs[k][verb] = [line]
    return products_by_verbs

def get_the_largest_sentece(dict_sentences):
    for gene in dict_sentences:
        for verb in dict_sentences[gene]:
            dict_sentences[gene][verb] = max(dict_sentences[gene][verb], key=len)
    return dict_sentences

def parsed_sentences(dict_sentences):
    for product in dict_sentences:
        for verb in dict_sentences[product]:
            dict_sentences[product][verb] = '||||'.join(dict_sentences[product][verb])
    return dict_sentences
    
def save_dict(dict_name, file_name):
    with open(file_name, 'w') as fp:
        json.dump(dict_name, fp, sort_keys=True, indent=4)

############################## Programa principal ##############################

# Obtener los productos celulares
path_words = '/export/storage/users/dsalazar/Bioinfo/keywords/keywords.txt'
words = get_words(path_words)

# Obtener las listas de verbos para cada caso
with open('verbs_1.txt', 'r') as v:
    archivo =  v.readlines()
    verbs=[]
    for verb in archivo:
        verb = verb.strip('\r\n')
        verbs.append(verb)

# Obtener palabras clave por parseo
path_p3v2 = '/export/storage/users/dsalazar/Bioinfo/parsed_triplets_raw/salmonella.parsed_by_the_1st_v2'

# Obtener el diccionario con todas las frases por producto biologico
dict_p3v2 = get_products_by_1st(path_p3v2, words)

# Obtener el diccionario con todas las frases por verbo y por producto biologico
verbal_sentences_p3v2 = get_verbal_sentences(dict_p3v2, verbs)

# Parsear para concatenar todas las frases y guardar
verbal_sentences_p3v2_parsed = parsed_sentences(verbal_sentences_p3v2)
save_dict(verbal_sentences_p3v2_parsed,'raw_verbal_sentences_p3v2_definition.json')

# Redefino el diccionario
verbal_sentences_p3v2 = get_verbal_sentences(dict_p3v2, verbs)

# Obtener el diccionario con una frase por verbo y por producto genico
largest_p3v2 = get_the_largest_sentece(verbal_sentences_p3v2)
save_dict(largest_p3v2,'verbal_sentences_p3v2_definition.json')

