import spacy

def return_text_from_file(file_path):
    texto = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        texto = file.read()

    print(texto)
    return texto

def remove_tokens_singles(tokenized_text):
    '''remove tokens isolados, ou seja, tokens que estão sozinhos em um segmento'''
    tokenized_segmented = []
    for token in tokenized_text:
        if len(token) > 2:
            tokenized_segmented.append(token)
    return tokenized_segmented

def tokenizer_spacy(text_list):
    nlp = spacy.load("pt_core_news_sm")
    tokenized_text = []
    for token in nlp(text_list):
        tokenized_text.append([token.text, token.lemma_, token.pos_, token.dep_, token.head.pos_])
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
        sentença = ""
        for token in sentence:
            sentença += token[0] + " "
        #print([sentença])
        text.append(sentença)
    return text

def shift_and(texto, padrao):
    m = len(padrao)
    n = len(texto)
    
    if m == 0: return 0
    if m > 64:
        raise ValueError("O padrão é muito longo para uma implementação simples de bits.")

    mascara_caracteres = {}
    for i in range(m):
        char = padrao[i]
        mascara_caracteres[char] = mascara_caracteres.get(char, 0) | (1 << i)

    R = 0
    bit_sucesso = 1 << (m - 1)
    posicoes = []

    for i in range(n):
        char_atual = texto[i]
        R = ((R << 1) | 1) & mascara_caracteres.get(char_atual, 0)
        
        if R & bit_sucesso:
            posicoes.append(i - m + 1)

    return posicoes

if __name__ == "__main__":
    print(tokenizer_spacy(["o navegador da Microsoft chegou a brutais 96% do mercado, esmagando o finado Netscape Navigator. ", "O primeiro navegador a ser violado, em meros cinco segundos, fio o Safari, seguido pelo Internet Explorer 8. |", ])[1])

