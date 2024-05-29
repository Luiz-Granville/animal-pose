import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exploratory_analysis(bovine_annotations):
    # Carregar os dados processados
    with open('data/processed/bovine_annotations.json', 'r') as f:
        bovine_data = json.load(f)
    
    # Analisar os dados e gerar visualizações
    # Exemplo:
    bovine_images_count = len(bovine_data['images'])
    print(f"Total de imagens de bovinos: {bovine_images_count}")


