import spacy

def return_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def tokenizer_spacy(text_list):
    nlp = spacy.load("pt_core_news_sm")
    tokenized_text = []
    for sentence in text_list:
        sentence_tokens = []
        for token in nlp(sentence):
            sentence_tokens.append([token.text, token.lemma_, token.pos_, token.dep_, token.is_stop])
        tokenized_text.append(sentence_tokens)
    return tokenized_text

if __name__ == "__main__":
    print(tokenizer_spacy(["O rato roeu a roupa do rei de Roma.", "A raposa rápida pula sobre o cão preguiçoso."])[0])