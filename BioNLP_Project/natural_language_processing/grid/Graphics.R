##   get_grafics_fscore.R   ##
#Archivo que genera las gráficas de los mejores puntajes de la f-score de la fase de entrenamiento
#Recíbe como parámetro los archivos donde se almacenan las f-score de cada experimento.


#parte la figure region en cuatro cuadros, donde se agregarán las gráficas
lay<-layout(matrix(1:4,ncol = 2))
#se crea una tabla con el archivo de la f-score de el par SVM-lineal
f_score_svm_lineal<-read.table(file="C:/Users/Luis Enrique/Desktop/Carlos final/eval/SVM-lineal_training_fscore.txt",sep='\t')
plot(f_score_svm_lineal[,1],type = 'l', ylab = 'valores de F-score', xlab = '',main = "F-score de la fase de entrenamiento \n SVM lineal", col = colors()[617], lwd =3)
#se marca el punto máximo
points(grep(max (f_score_svm_lineal[,1]), f_score_svm_lineal[,1]), max(f_score_svm_lineal[,1]), col = 'red', cex=2, lwd =2)

#se crea una tabla con el archivo de la f-score de el par SVM-rbf
f_score_svm_rbf<-read.table(file="C:/Users/Luis Enrique/Desktop/Carlos final/eval/SVM-rbf_training_fscore.txt",sep='\t')
plot(f_score_svm_rbf[,1],type = 'l', ylab = 'valores de F-score', xlab = 'Número de Experimento',main = "F-score de la fase de entrenamiento \n SVM rbf", col = colors()[617], lwd =3)
#se marca el punto máximo
points(grep(max (f_score_svm_rbf[,1]), f_score_svm_rbf[,1]), max(f_score_svm_rbf[,1]), col = 'red', cex=2, lwd =2)

#se crea una tabla con el archivo de la f-score de el MultinomialNB
f_score_multinomial<-read.table(file="C:/Users/Luis Enrique/Desktop/Carlos final/eval/MultinomialNB_training_fscore.txt",sep='\t')
plot(f_score_multinomial[,1],type = 'l', ylab = '', xlab = '',main = "F-score de la fase de entrenamiento \n MultinomialNB", col = colors()[617], lwd =3)
#se marca el punto máximo
points(grep(max (f_score_multinomial[,1]), f_score_multinomial[,1]), max(f_score_multinomial[,1]), col = 'red', cex=2, lwd =2)

#se crea un vector con toda la grid, para graficar el valor mas álto de todo el experimento
f_score_general <- c(f_score_multinomial[,1],f_score_svm_lineal[,1], f_score_svm_rbf[,1])
plot(f_score_general,type = 'l', ylab = '', xlab = 'Número de Experimento',main = "F-score de la fase de entrenamiento \n general", col = colors()[617], lwd =3)
#se marca el punto máximo de todo el experimento
points(grep(max (f_score_general), f_score_general), max(f_score_general), col = 'red', cex=2, lwd =2)