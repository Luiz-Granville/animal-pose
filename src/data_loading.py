# src/data_loading.py

import json

# Função para carregar os dados do JSON
def load_annotations(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
