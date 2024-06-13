# src/visualization.py

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import cv2
import dataframe_image as dfi

def plot_category_distribution(category_counts, categories, output_path=None):
    # Transformar em DataFrame para facilitar a manipulação
    data = {'Category': [categories[str(cat_id)] for cat_id in category_counts.keys()],
            'Count': list(category_counts.values())}
    df = pd.DataFrame(data)
    
    # Ordenar em ordem decrescente
    df = df.sort_values(by='Count', ascending=False)
    
    # Criar uma paleta de cores personalizada
    palette = sns.color_palette("husl", len(df))
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Count', data=df, hue='Category', dodge=False, palette=palette, legend=False)
    plt.title('Distribution of Images by Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Images')
    plt.xticks(rotation=45)
    
    if output_path:
        plt.savefig(output_path)
        plt.close()
    else:
        plt.show()

def display_results(bovine_images):
    

    results = {
        'Category': ['Bovine Images'],
        'Count': [len(bovine_images)]
    }
    df = pd.DataFrame(results)
    
    plt.figure(figsize=(6, 4))
    sns.barplot(x='Category', y='Count', data=df)
    plt.title('Results of Bovine Images Processing')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

def create_category_count_table_image(category_counts, categories, output_path=None):
    category_names = [categories[str(cat_id)] for cat_id in category_counts.keys()]
    counts = list(category_counts.values())
    
    df = pd.DataFrame({'Category': category_names, 'Count': counts})
    
    # Ordenar a tabela pelo número de contagens em ordem decrescente
    df = df.sort_values(by='Count', ascending=False)
    
    # Estilizar o DataFrame
    styled_table = df.style.background_gradient(cmap='viridis').set_table_styles(
        [{'selector': 'thead th', 'props': [('background-color', '#40466e'), ('color', 'white')]}]
    )
    
    # Salvar a tabela como uma imagem
    if output_path:
        dfi.export(styled_table, output_path)
    else:
        dfi.export(styled_table, 'styled_table.png')
        img = plt.imread('styled_table.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    
    return df




def plot_keypoints(image, keypoints, skeleton, output_path=None, line_width=1, point_size=3):
    if len(image.shape) == 2:  # Converter imagem para BGR se estiver em escala de cinza
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    keypoint_pairs = [(keypoints[i][0], keypoints[i][1], keypoints[i][2]) for i in range(len(keypoints))]
    
    for (i, j) in skeleton:
        if keypoint_pairs[i][2] > 0 and keypoint_pairs[j][2] > 0:  # Verificar visibilidade
            x1, y1 = keypoint_pairs[i][:2]
            x2, y2 = keypoint_pairs[j][:2]
            plt.plot([x1, x2], [y1, y2], 'r-', linewidth=line_width)
    
    for x, y, v in keypoint_pairs:
        if v > 0:  # Verificar visibilidade
            plt.plot(x, y, 'ro', markersize=point_size)
    
    if output_path:
        plt.savefig(output_path)
        plt.close()
    else:
        plt.show()

