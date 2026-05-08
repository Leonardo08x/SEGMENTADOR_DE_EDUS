import spacy

class segmentador_de_edus:
    def __init__(self):
        print("Iniciando o processo de segmentação...")


    def regra_1(text_local):
        ''' segmentação por ponto final, regra 1'''
        edus = []
        local_edus = []
        for token in text_local:
            
            if token[0] == "." or token[0] == "!" or token[0] == "?":
                local_edus.append(token)
                edus.append(local_edus)
                local_edus = []
            else:
                local_edus.append(token)
        
        edus.append(local_edus)
        return edus
    
    def regra_9_3(tokenized_text):
        '''informações parenteticas, separadas por caracteres especiais, regra 9
        e regra 3, citações explicitas'''
        tokenized_segmented = []
        for sentence in tokenized_text:
            sentence_segmented = []
            for token in sentence:
                if token[3] == "punct" and not token[0] != "." and not token[0] != "!" and not token[0] != "?" and not token[0] != ",":
                    if token[0] == ")" or token[0] == "}" or token[0] == "]" or token[0] == '"' or token[0] == "'":
                        sentence_segmented.append(token)
                        tokenized_segmented.append(sentence_segmented)
                        sentence_segmented = []
                        sentence_segmented.append(token)
                    else:
                        tokenized_segmented.append(sentence_segmented)
                        sentence_segmented = []
                        sentence_segmented.append(token)
                else:
                    sentence_segmented.append(token)
            if sentence_segmented != []:
             tokenized_segmented.append(sentence_segmented)
        return tokenized_segmented
    
    def regra_2(tokenized_text, marcadores_fortes):
        ''' segmentação por marcadores fortes'''
        tokenized_segmented = []
        for sentence in tokenized_text:
            sentence_segmented = []
            for token in sentence:
                if token[0] in marcadores_fortes:
                    tokenized_segmented.append(sentence_segmented)
                    sentence_segmented = []
                    sentence_segmented.append(token)
                else:
                    sentence_segmented.append(token)
            if sentence_segmented != []:
             tokenized_segmented.append(sentence_segmented)
        return tokenized_segmented
    
    def regra_7(tokenized_text):
        '''segmentação por orações relativas(todas)'''
        return tokenized_text

    def regra_5(tokenized_text):
        '''segmentação por verbo implicito'''
        tokenized_segmented = []
        for sentence in tokenized_text:
            sentence_segmented = []
            for token in sentence:
                if token[0] == "e" and token[4] in ["VERB", "AUX"]:
                        tokenized_segmented.append(sentence_segmented)
                        sentence_segmented = []
                        sentence_segmented.append(token)
                else:
                    sentence_segmented.append(token)
            if sentence_segmented != []:
                tokenized_segmented.append(sentence_segmented)
        return tokenized_segmented
    
    def regra_6(tokenized_text):
        '''segmentadando orações reduzidas'''
        tokenized_segmented = []
        for sentence in tokenized_text:
            sentence_segmented = []
            last_token_virgula = False
            for token in sentence:
                last_token_virgula = True if token[0] == "," else False
                if token[2] == "VERB" or "AUX" and last_token_virgula == True:
                    if sentence_segmented:
                        tokenized_segmented.append(sentence_segmented)
                        sentence_segmented = []
                        sentence_segmented.append(token)
                        
                else:
                    sentence_segmented.append(token)
            if sentence_segmented != []:
                tokenized_segmented.append(sentence_segmented)
        return tokenized_segmented
    def regra_8(tokenized_text):
        ''' segmentação por verbos publicos ou de atribuição de fala'''
        return tokenized_text
if __name__ == "__main__":
    segmentador_de_edus()
    print(segmentador_de_edus.regra_9_3([[['O', 'o', 'DET', 'det', 'false'], ['rato', 'rato', 'NOUN', 'nsubj', 'false'], ['roeu', 'roer', 'VERB', 'ROOT', 'false'], ['a', 'a', 'DET', 'det', 'false'], ['roupa', 'roupa', 'NOUN', 'obj', 'false'], ['do', 'de o', 'ADP DET', 'case det', 'false'], ['rei', 'rei', 'NOUN', 'nmod:poss', 'false'], ['de', 'de', 'ADP', 'case', 'false'], ['Roma.', 'Roma.', 'PROPN', 'nmod:npmod', 'false']]]))