from collections import defaultdict
with open ('/home/luisrs/snp138_col.txt') as archivo:
        with open ('/home/luisrs/rs_uniq_1000g.txt') as inter:
                with open ('/home/luisrs/final44.txt','w') as resul:
                        dic_rs_pos = defaultdict(list)
                        for line in archivo:
                                line = line.strip('\n').split('\t')
                                if line[3] in dic_rs_pos:
                                         if line[0] and line[1] in dic_rs_pos[line[3]]:
                                                continue
                                dic_rs_pos[line[3]].append(line[0])
                                dic_rs_pos[line[3]].append(line[1])
                        cromo=['chr5','chr9','chr17','chr21']
                        chr=[]
                        for i in dic_rs_pos.keys():
                                if len(dic_rs_pos[i])==2:
                                        if dic_rs_pos[i][0] in cromo:
                                                chr.append(i)
                        inter_list = []
                        for line in inter:
                                line=line.strip('\n')
                                inter_list.append(line)
                        a=set(chr)
                        print (len(a))
                        b=set(inter_list)
                        print (len(b))
                        union = a.union(b)
                        intersection = a.intersection(b)
                        print (len(intersection), len (union))
                        for i in union:
                                resul.write(i + '\n')
print ('ya acabe')
quit()






