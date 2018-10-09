#estas primeras lineas regresan los archivos con solo las lineas que necesitamos
cut -f1-11 -d ' ' 1000GP_Phase3_all.txt |perl -nae '/^(\w+):\w+:\w+:\w+\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(.+)\s(.+)\s(.+)\s(.+)\s(.+)\s(.+)/; print "$1\t$2\t$3\t$4\t$5\t$6\t$7\t$8\t$9\t$10\t$11\n";' > 1000GP_Phase3_all_col.txt
cut -f2-5,7,8,10,12 snp138.txt > snp138_col.txt

