import spacy

class segmentador_de_edus:
    def __init__(self):
        print("Iniciando o processo de segmentação...")

    def checar_segmentar(tokenized_sentence):
        for token in tokenized_sentence:
            if token[2] == 'SEGMENTO':
                return True
        return False
    
    def regra_1(text_local):
        for token in text_local.copy():
            if token == '.':
                text_local[text_local.index(token)] += "|"
        edus = text_local.split("|")
        return edus
    
    def regra_2_3(tokenized_text):
        tokenized_segmented = []
        for sentence in tokenized_text:
            sentence_segmented = []
            for token in sentence:
                if token[3] == "punct" and not token[0] != ".":
                    sentence_segmented.append(token)
                    sentence_segmented.append(['|','|', 'SEGMENTO', 'SEG', 'false'])
                else:
                    sentence_segmented.append(token)
            tokenized_segmented.append(sentence_segmented)
        return tokenized_segmented
    

if __name__ == "__main__":
    segmentador_de_edus()
    print(segmentador_de_edus.regra_2_3([[['O', 'o', 'DET', 'det', 'false'], ['rato', 'rato', 'NOUN', 'nsubj', 'false'], ['roeu', 'roer', 'VERB', 'ROOT', 'false'], ['a', 'a', 'DET', 'det', 'false'], ['roupa', 'roupa', 'NOUN', 'obj', 'false'], ['do', 'de o', 'ADP DET', 'case det', 'false'], ['rei', 'rei', 'NOUN', 'nmod:poss', 'false'], ['de', 'de', 'ADP', 'case', 'false'], ['Roma.', 'Roma.', 'PROPN', 'nmod:npmod', 'false']]]))