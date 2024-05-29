# Pose Estimation para Bovinos

## 1. Análise Exploratória

Realizamos uma análise exploratória dos dados para entender a distribuição das categorias e keypoints.

**Distribuição das Categorias:**

![Distribuição das Categorias](images/category_distribution.png)

**Descrição Textual:**

Observamos que a categoria de bovinos possui X imagens e Y anotações. A distribuição dos keypoints é mostrada no gráfico acima.

## 2. Filtragem e Processamento de Imagens

Filtramos o dataset para obter apenas as imagens de bovinos e realizamos o processamento para detectar e visualizar os keypoints.

**Etapas de Processamento:**

1. Carregar os dados de anotações e imagens.
2. Filtrar as anotações para bovinos.
3. Processar as imagens para visualizar os keypoints.

**Figura Ilustrativa do Processo:**

![Processo de Filtragem](images/process_flow.png)

## 3. Resultados Finais

**Distribuição dos Keypoints dos Bovinos:**

![Distribuição dos Keypoints](images/keypoints_distribution.png)

**Descrição Textual:**

Os keypoints dos bovinos estão distribuídos conforme o gráfico acima, mostrando a localização típica dos pontos-chave.

## 4. Conclusões Pessoais

### Principais Aprendizados

- A importância dos keypoints na estimativa de poses.
- Desafios no processamento e visualização dos dados.

### Limitações do Trabalho

- Qualidade das anotações e imagens pode variar.
- Dataset limitado em termos de variedade de poses.

### Sugestões para Trabalhos Futuros

- Uso de técnicas de deep learning para melhorar a precisão.
- Expansão do dataset com mais imagens e categorias.

## Repositório

O código da implementação realizada em scripts Python está disponível no repositório GitHub.

[Link para o repositório](https://github.com/username/repo)
[text](data/raw/bounding_boxes) [text](data/raw/bounding_boxes/annotations) [text](data/raw/bounding_boxes/annotations/antelope.json) [text](data/raw/bounding_boxes/annotations/bear.json) [text](data/raw/bounding_boxes/annotations/bobcat.json) [text](data/raw/bounding_boxes/annotations/hippocampi.json) [text](data/raw/bounding_boxes/annotations/orangutan.json) [text](data/raw/bounding_boxes/annotations/otter.json) [text](data/raw/bounding_boxes/annotations/rhino.json) [text](data/raw/bounding_boxes/images) [text](data/raw/bounding_boxes/images/antelope) [text](data/raw/bounding_boxes/images/bear) [text](data/raw/bounding_boxes/images/bobcat) [text](data/raw/bounding_boxes/images/chimpanzee) [text](data/raw/bounding_boxes/images/hippopotamus) [text](data/raw/bounding_boxes/images/otter) [text](data/raw/bounding_boxes/images/rhino) [text](data/raw/keypoints) [text](data/raw/keypoints/images) [text](data/raw/keypoints/keypoints.json)