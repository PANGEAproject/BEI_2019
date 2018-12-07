import os 

def empty(srt_path):
    os.chdir(srt_path)
    data_text = os.listdir(".")
    for i in range(len(data_text)):
        with open (data_text[i], 'r') as ft:
            archivo = ft.readlines()
            if len(archivo) < 1:
                print data_text[i]

print "Empty triplets\n"
empty("/export/storage/users/dsalazar/Bioinfo/output")
print "\n   Empty 1\n"
empty("/export/storage/users/dsalazar/Bioinfo/p1")
print "\n   Empty 2\n"
empty("/export/storage/users/dsalazar/Bioinfo/p2")
print "\n   Empty 3\n"
empty("/export/storage/users/dsalazar/Bioinfo/p3")