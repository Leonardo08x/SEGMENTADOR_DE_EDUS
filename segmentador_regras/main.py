from utils import utils
from segmentador.segmentador import segmentador_de_edus


if __name__ == "__main__":
    segmentador_de_edus()
    regra_1 = segmentador_de_edus.regra_1(utils.remove_tokens_singles(utils.tokenizer_spacy(utils.return_text_from_file(r"/home/mrsylky/Documentos/IC/CSTNews 6.0/C10_Mundo_BombardeioLibano/Textos-fonte/D3_C10_OGlobo.txt"))))
    print(regra_1)
    print("Regra 1 concluída")
    regra_9_3 = segmentador_de_edus.regra_9_3(regra_1)
    print(regra_9_3)
    print("Regra 9 e 3 concluídas")
    regra_2 = segmentador_de_edus.regra_2(regra_9_3, utils.marcadores_fortes_lista())
    #print(regra_2)
    print("Regra 2 concluída")
    regra_7 = segmentador_de_edus.regra_7(regra_2)
    print(regra_7)
    print("Regra 7 concluída")
    regra_5 = segmentador_de_edus.regra_5(regra_7)
    print(regra_5)
    print("Regra 5 concluída")
    regra_6 = segmentador_de_edus.regra_6(regra_5)
    #print(regra_6)
    print("Regra 6 concluída")
    regra_8 = segmentador_de_edus.regra_8(regra_6)
    #print(regra_8)
    print("Regra 8 concluída")
    texto_final = utils.retorna_texto(regra_8)
    print(texto_final)