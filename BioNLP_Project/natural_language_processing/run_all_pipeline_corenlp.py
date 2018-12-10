#!/usr/bin/python3
## Notes: V1.0, 25/11/2018
## Author(s): Velez Santiago Jesus, Cazares Rodriguez Jesus Antonio
## Email(s): jvelez@lcg.unam.mx, jesuscr@lcg.unam.mx

#===================================================================================================#
# Objetive: Automatically classify phrases with and without information about regulatory
#           interactions between transcription factors.
# Input:
#   1) --inputFiles:
#       1.1) File with sentences for the positive class.
#       1.2) File with sentences for the negative class.
#   2) --check:
#       2.1) Word or symbol not present in the text to add as identifier to inputFiles sentences.
#   3) --column:
#       3.1) Column of file to estract sentences in inputFiles.
#   4) --categories:
#       4.1) Characteristics to select from the parsed file of corenlp. {0:'word',1:'lemma',2:'pos',3:'ner',4:'headidx',5:'deprel'}
#   5) --category_name:
#       5.1) Name to add to positive class. 
#   6) --other_name:
#       6.1) Name to add to negative class.
#   7) --testsize:
#       7.1) Size of test class. Training class is equal to 1 - testsize.
#   8) --regexner:
#       8.1) Dictionary of categories to special words in inputFiles.
#       Note:
#           To know correct form of dictionary input file see:
#           https://stanfordnlp.github.io/CoreNLP/ner.html?fbclid=IwAR1cKqUR2aS4BxtMDy9BsC-uR-zPwwlfdKnl1DPFibS7awPfFOPvmGX8NbA
# Output:
#   1) Files with marks added at the end of each sentence.
#       Out: fileName.check
#   2) Raw results of corenlp per file.
#       Out: fileName.check.conll
#   3) Parsed results from corenlp.
#       Out: fileName.check.conll.parsed 
#   4) File per characteristic selected per input file.
#       Out: fileName.{word,lemma,pos,ner,headidx,deprel}
#   5) Files of test and training classes and respective sentences per characteristic selected.
#       Out: 
#           5.1) testClass.{word,lemma,pos,ner,headidx,deprel}
#           5.2) trainingClass.{word,lemma,pos,ner,headidx,deprel}
#           5.3) testData.{word,lemma,pos,ner,headidx,deprel} 
#           5.4) trainingData.{word,lemma,pos,ner,headidx,deprel}
#
# Dependencies: os, argparse,pandas, sklearn, corenlp program.
# Example to run:
#   Without regexner:
#   python extract_data_corenlp.py -fs sentences_RI_RIGC.txt sentences_Other.txt -col 2 -cat 0 1 2 3 -t 0.30
#   With regexner:
#   python extract_data_corenlp.py -fs sentences_RI_RIGC.txt sentences_Other.txt -re nerdicc.txt -col 2 -cat 0 1 2 3 -t 0.30
#===================================================================================================#

import os, argparse
import pandas as pd # Import pandas for using common data science methods.
from sklearn.model_selection import train_test_split # function to create train a test files.

def add_check_mark_to_sentences(files,check = 'PANGEA', col = 0):
    for file in files:
        with open(file + '.check', 'w') as out: # Send outputs to current file.
            with open(file,'r') as f:
                for line in f:
                    sentence = line.strip('\n').split('\t')[col] # Get column of sentence selected.
                    if sentence.endswith('.'):
                        out.write(sentence + check + '\n') # Add only check mark.
                    else:
                        out.write(sentence + ' .' + check + '\n') # Add space with dot and check.

def run_corenlp(files,regexner = None):
    if regexner: # Use dictionary to categorize special entities.
        for file in files:
            os.system('/export/apps/corenlp/corenlp.sh -annotators tokenize,ssplit,pos,lemma,ner,regexner -outputFormat conll -file {}.check -regexner.mapping {} -outputDirectory .'.format(file,regexner)) 
    else:
        for file in files:
            os.system('/export/apps/corenlp/corenlp.sh -annotators tokenize,ssplit,pos,lemma,ner -outputFormat conll -file {}.check -outputDirectory .'.format(file))

def parse_corenlp_results(corenlp_results,check = 'PANGEA'):
    # Create a file that contains each word separated by
    # a tabulator and each category by word separated by a pipeline
    for corenlp_result in corenlp_results:
        with open(corenlp_result) as f:
            text = []
            paragraph = []
            for line in f:
                if not line.startswith('\n'): # Skip empty lines.
                    line = line.split('\t')
                    if line[1] == check:
                        text.append(' '.join(paragraph))
                        paragraph = []
                    else:
                        paragraph.append('|'.join(line[1:5]))
                        
        with open(corenlp_result + '.parsed','w') as out:
            out.write('\n'.join(text)) # Save results.

def get_categories(corenlp_resulsts_parsed,categories):
    extensions = {0:'.word',1:'.lemma',2:'.pos',3:'.ner',4:'headidx',5:'deprel'}
    for corenlp_resulst_parsed in corenlp_resulsts_parsed:
        for category in categories:
            filter_text = []
            with open(corenlp_resulst_parsed,'r') as f:
                for line in f:
                    line = line.strip('\n').split(' ')
                    filter_text.append(' '.join([word.split('|')[category] for word in line]))
                    
            outfile = corenlp_resulst_parsed + extensions[category]
            with open(outfile,'w') as out:
                out.write('\n'.join(filter_text))
    return [extensions[category] for category in categories]

def create_training_and_test_classes(category_files,other_files, extensions, test_size, category = 'RI', other = 'OTHER'):
    if len(category_files) == len(other_files) == len(extensions):
        for category_file, other_file, extension in zip(category_files,other_files,extensions):
            category_data, other_data = pd.read_table(category_file,header = None), pd.read_table(other_file, header = None)
            x_train, x_test, y_train, y_test = train_test_split(category_data,
                                                                pd.DataFrame([category] * len(category_data.index)),
                                                                test_size = test_size, random_state = 2)
            x_train1, x_test1, y_train1, y_test1 = train_test_split(other_data,
                                                                   pd.DataFrame([other] * len(other_data.index)),
                                                                   test_size = test_size, random_state = 2)

            outfiles = [name + extension for name in ['trainingData','testData','trainingClass','testClass']]
            pd.concat([x_train,x_train1]).to_csv(outfiles[0],header = None, index = False, columns = [0], sep = '\t')
            pd.concat([x_test,x_test1]).to_csv(outfiles[1],header = None, index = False, columns = [0], sep = '\t')
            pd.concat([y_train,y_train1]).to_csv(outfiles[2],header = None, index = False, columns = [0], sep = '\t')
            pd.concat([y_test,y_test1]).to_csv(outfiles[3],header = None, index = False, columns = [0], sep = '\t')
    else:
        print('Dimensions are not equal.')

def run_all():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fs','--inputFiles', dest = 'inputFiles', help = 'File one: positive class.\nFile 2: negative class.', nargs = 2, metavar = 'PATH')
    parser.add_argument('-c','--check', dest = 'check', help = 'Word or symbol not present in the text to add as identifier.', default = 'PANGEA')
    parser.add_argument('-col','--column', dest = 'column', help = 'Column to extract sentence in tab file.', default = 1, type = int)
    parser.add_argument('-cat','--categories', dest = 'categories', help='Categories to select of parsed corenlp file.', nargs = '+', type = int)
    parser.add_argument('-cname','--category_name', dest = 'category_name', default = 'RI')
    parser.add_argument('-cother','--other_name', dest = 'other_name', default = 'OTHER')
    parser.add_argument('-t', '--testsize', dest = 'test_size', type = float, help = 'Size of test class.')
    parser.add_argument('-re', '--regexner', dest='regexner', default=None)

    args = parser.parse_args() # Take arguments.

    add_check_mark_to_sentences(args.inputFiles, check = args.check, col = args.column)
    run_corenlp(args.inputFiles,args.regexner)
    parse_corenlp_results([file + '.check.conll' for file in args.inputFiles], check = args.check)
    extensions = get_categories([file + '.check.conll.parsed' for file in args.inputFiles], args.categories)
    category_files = [args.inputFiles[0] + '.check.conll.parsed' + extension for extension in extensions]
    other_files = [args.inputFiles[1] + '.check.conll.parsed' + extension for extension in extensions]
    create_training_and_test_classes(category_files,other_files,extensions,args.test_size, category=args.category_name,other=args.other_name)

# Run main program.
if __name__ == '__main__':
    run_all()
