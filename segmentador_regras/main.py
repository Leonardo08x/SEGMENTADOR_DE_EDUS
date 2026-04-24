from utils import utils
from segmentador.segmentador import segmentador_de_edus


if __name__ == "__main__":
    segmentador_de_edus()
    regra_1 = utils.tokenizer_spacy(segmentador_de_edus.regra_1(utils.return_text_from_file("textos/texto1.txt")))
    regra_9_3 = segmentador_de_edus.regra_9_3(regra_1)
    regra_2 = segmentador_de_edus.regra_2(regra_9_3, utils.marcadores_fortes_lista())
    regra_7 = segmentador_de_edus.regra_7(regra_2)
    regra_5 = segmentador_de_edus.regra_5(regra_7)
    regra_6 = segmentador_de_edus.regra_6(regra_5)
    regra_8 = segmentador_de_edus.regra_8(regra_6)
    print(utils.retorna_texto(regra_8))