from itertools import product

# Aqui valta agregar sus extensiones de donde va cada parametro. word es el ejemplo de lo que me refiero. ParA TODOS.
feactures = ['word', 'lemma', 'pos', 'ner']
bayes = ['MultinomialNB', 'SVM --kernel linear', 'SVM --kernel rbf']
selection = ['CHI250', 'CHI2100']
stop_word = ['TRUE', 'FALSE']
values = ['t', 'b', 'f']
N_gramas = ['1\t1', '2\t2','1\t2']



# Aqui solo necesitas hacer la primera parte, la de la funcion product. Lo demas lo puse para poder imprimirlo,
# Entonces el output puedes redirigirlo al archivo.
grid = [experiment for experiment in product(feactures, bayes, selection, stop_word, values , N_gramas)]
i=1
for experiment in grid:
    if (experiment[1] == 'SVM' + '\t' + 'kernel linear'):
        cad = 'SVM-lineal'
    if (experiment[1] == 'SVM' + '\t' + 'kernel rbf'):
        cad = 'SVM-rbf'
    if (experiment[1] == 'MultinomialNB'):
        cad = 'MultinomialNB' + '\t' + 'No_aplica'
    line = str(experiment[0]) + '\t' + str(cad) + '\t' + str(experiment[4]) + '\t' + str(experiment[5]) + '\t' + str(experiment[2]) + '\t' + str(experiment[3])
    print(line)
    if (i==10):
        print ('rm nohup.out')
    i=i+1


