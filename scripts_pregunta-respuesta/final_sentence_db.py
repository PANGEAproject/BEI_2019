
import json

def parsed_sentences(dict_sentences):
    for product in dict_sentences:
        for verb in dict_sentences[product]:
            dict_sentences[product][verb] = ' '.join(dict_sentences[product][verb])
    return dict_sentences

with open('verbal_sentences_p3v2_definition.json', 'r') as f:
    definition = json.load(f)
    definition_cat = parsed_sentences(definition)

with open('verbal_sentences_p3v2_funtion.json', 'r') as f2:
    function = json.load(f2)
    function_cat = parsed_sentences(function)

products = set(list(definition.keys())).add(list(function.keys()))





