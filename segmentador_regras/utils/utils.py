import spacy

def return_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def tokenizer_spacy(text_list):
    nlp = spacy.load("pt_core_news_sm")
    tokenized_text = []
    for sentence in text_list:
        sentence_tokens = []
        for token in nlp(sentence):
            sentence_tokens.append([token.text, token.lemma_, token.pos_, token.dep_, token.head.pos_])
        tokenized_text.append(sentence_tokens)
    return tokenized_text

def marcadores_fortes_lista():
    marcadores_fortes = [
    # Oposição (Adversativos e Concessivos)
    'mas', 'porem', 'todavia', 'contudo', 'entretanto', 'entanto', 'embora', 
    'conquanto', 'apesar de', 'ainda que', 'mesmo que', 'posto que',

    # Conclusão e Conseqüência
    'portanto', 'logo', 'assim', 'consequentemente', 'entao', 'porisso', 
    'por conseguinte', 'desta forma', 'desse modo',

    # Temporais
    'quando', 'enquanto', 'apenas', 'mal', 'desde que', 'depois que', 
    'logo que', 'assim que', 'sempre que', 'durante', 'apos', 'antes de', 
    'a partir de', 'ate que',

    # Condicionais
    'se', 'caso', 'desde que', 'contanto que', 'a menos que', 'a nao ser que',

    # Causalidade e Adição (Fortes)
    'porque', 'visto que', 'ja que', 'pois', 'alem disso', 'ademais', 'outrossim'
]
    return marcadores_fortes

#inutilizada, mas pode ser útil para futuras implementações
def checar_segmentar(tokenized_sentence):
    for token in tokenized_sentence:
        if token[2] == 'SEGMENTO':
            return True
    return False
    
def retorna_texto(tokenized_segmented):
    text = []
    for sentence in tokenized_segmented:
        sentence_text = " ".join([token[0] for token in sentence])
        text.append(sentence_text)
    return text
if __name__ == "__main__":
    print(tokenizer_spacy(["o navegador da Microsoft chegou a brutais 96% do mercado, esmagando o finado Netscape Navigator. ", "O primeiro navegador a ser violado, em meros cinco segundos, fio o Safari, seguido pelo Internet Explorer 8. |", ])[1])

