# Segmentador de EDUs
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![NLP](https://img.shields.io/badge/NLP-SpaCy-green)
## Descrição

Este projeto implementa um segmentador de texto em Unidades Discursivas Elementares (EDUs) baseado em regras linguísticas para o português brasileiro. Utiliza a biblioteca spaCy para tokenização e análise morfológica, permitindo a divisão de textos em unidades discursivas menores para análise de discurso.

O segmentador aplica uma sequência de regras para identificar pontos de quebra no texto, resultando em EDUs que podem ser usadas em tarefas de processamento de linguagem natural, como sumarização, análise de coerência e geração de texto.

## Funcionalidades

- **Tokenização avançada**: Usa spaCy com modelo `pt_core_news_sm` para análise morfológica e sintática.
- **Regras de segmentação**: Implementa múltiplas regras baseadas em pontuação, marcadores discursivos e estruturas sintáticas.
- **Processamento sequencial**: Aplica regras em ordem específica para refinar a segmentação.
- **Saída estruturada**: Retorna texto segmentado em listas de EDUs.

## Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip para gerenciamento de pacotes

### Passos
1. Clone ou baixe o repositório:
   ```bash
   git clone [URL do repositório]
   cd segmentador_regras
   ```

2. Instale as dependências:
   ```bash
   pip install spacy
   python -m spacy download pt_core_news_sm
   ```

## Uso

1. Prepare um arquivo de texto (ex: `textos/texto1.txt`) com o conteúdo a ser segmentado.

2. Execute o script principal:
   ```bash
   python main.py
   ```

O script irá processar o texto aplicando todas as regras em sequência e imprimir as EDUs segmentadas.

### Exemplo de Saída
```
['O navegador da Microsoft chegou a brutais 96% do mercado', 'esmagando o finado Netscape Navigator.']
```

## Arquitetura do Projeto

- `main.py`: Script principal que orquestra o processamento.
- `segmentador/segmentador.py`: Classe `segmentador_de_edus` com métodos para cada regra.
- `utils/utils.py`: Funções utilitárias para tokenização, leitura de arquivos e marcadores fortes.

## Regras de Segmentação

O projeto implementa as seguintes regras de segmentação, aplicadas em sequência:

| Regra | Descrição | Status da Implementação |
|-------|-----------|-------------------------|
| **Regra 1** | Segmentação por ponto final (.), exclamação (!) e interrogação (?) | ✅ Implementada |
| **Regra 9.3** | Informações parentéticas separadas por caracteres especiais e citações explícitas | ✅ Implementada |
| **Regra 2** | Segmentação por marcadores fortes (oposição, conclusão, temporalidade, condicionais, causalidade) | ✅ Implementada |
| **Regra 7** | Segmentação por orações relativas (todas) | ❌ Não implementada (placeholder) |
| **Regra 5** | Segmentação por verbo implícito (conjunção "e" seguida de verbo) | ✅ Implementada |
| **Regra 6** | Segmentação por orações reduzidas (verbo após vírgula) | ✅ Implementada |
| **Regra 8** | Segmentação por verbos públicos ou de atribuição de fala | ❌ Não implementada (placeholder) |

### Status Geral
- **Regras implementadas**: 5/7 (71%)
- **Regras pendentes**: 2/7 (29%) - Regras 7 e 8 necessitam implementação completa.

As regras não implementadas retornam o texto sem modificações, servindo como placeholders para desenvolvimento futuro.

## Desenvolvimento

### Executando Testes
O projeto inclui testes básicos no `__main__` de alguns módulos. Para testar:
```bash
python utils/utils.py
python segmentador/segmentador.py
```

### Melhorias Futuras
- Implementar regras 7 e 8
- Interface web ou CLI mais robusta

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-regra`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova regra'`)
4. Push para a branch (`git push origin feature/nova-regra`)
5. Abra um Pull Request

### Diretrizes
- Siga o estilo de código Python (PEP 8)
- Adicione comentários e docstrings
- Teste suas mudanças

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Veja o arquivo LICENSE para detalhes.

## Autores

- [Leonardo Cunha da Rocha] - Desenvolvimento inicial

## Agradecimentos

- Biblioteca spaCy por fornecer ferramentas de PLN robustas
