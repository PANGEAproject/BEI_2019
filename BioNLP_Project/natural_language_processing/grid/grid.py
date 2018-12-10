# -*- encoding: utf-8 -*-
###################################################################################################
                         #grid.py#
###################################################################################################
"""Descrición
Autor: Luis Enrique Ramírez y Jesús Vélez 
No recibe ningún parámetro, pero al correrlo se debe agregrar un '> #nombre_del_archivo.sh#'

Descripción: crea las lineas que recibe el archivo de python training-crossvalidation-testing-dom.py con todas las combinaciones de parametros que recibe dicho programa

Ejemplo de uso: grid.py '> grid.sh

Dependencias: intertools

"""
from itertools import product

# Aqui valta agregar sus extensiones de donde va cada parametro. word es el ejemplo de lo que me refiero. ParA TODOS.
feactures = ['word', 'lemma', 'pos', 'ner']
bayes = ['MultinomialNB', 'SVM --kernel linear', 'SVM --kernel rbf']
selection = ['CHI250', 'CHI2100']
stop_word = ['--removeStopWords', ' ']
values = ['t', 'b', 'f']
N_gramas = ['--ngrinitial 1 --ngrfinal 1', '--ngrinitial 2 --ngrfinal 2','--ngrinitial 1 --ngrfinal 2']



# Aqui solo necesitas hacer la primera parte, la de la funcion product. Lo demas lo puse para poder imprimirlo,
# Entonces el output puedes redirigirlo al archivo.
grid = [experiment for experiment in product(feactures, bayes, selection, stop_word, values , N_gramas)]
i=1
for experiment in grid:
    if (experiment[1] == 'SVM --kernel linear'):
        cad = 'SVM-lineal'
    if (experiment[1] == 'SVM --kernel rbf'):
        cad = 'SVM-rbf' 
    if (experiment[1] == 'MultinomialNB'):
        cad = 'MultinomialNB' 
    line = 'python training-crossvalidation-testing-dom.py --inputPath /home/luisrs/storage/Project/natural_language_processing/coretest2 --inputTrainingData trainingData.' + experiment[0] + ' --inputTrainingClasses trainingClass.' + experiment[0] + ' --inputTestingData testData.' + experiment[0] + ' --inputTestingClasses testClass.' + experiment[0] + ' --outputModelPath /home/luisrs/storage/Project/lcg-bioinfoI-bionlp/clasificacion-automatica/structural-domain-dataset/models --outputModelFile '  + cad +'-model.mod --outputReportPath /home/luisrs/storage/Project/lcg-bioinfoI-bionlp/clasificacion-automatica/structural-domain-dataset2/reports --outputReportFile ' + cad + '.txt --classifier ' + experiment[1] + ' --saveData --vectorizer ' + experiment[4] +' '+ experiment[5] + ' ' + experiment[3] + ' --reduction ' + experiment[2]
    print(line)
    if (i==10):
        print ('rm nohup.out')
    i=i+1
