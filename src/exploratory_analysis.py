# src/exploratory_analysis.py

import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

from data_loading import load_annotations
from utils import count_images_by_category


# Função para plotar os dados
def plot_category_distribution(category_counts, categories):
    category_names = [categories[str(cat_id)] for cat_id in category_counts.keys()]
    counts = list(category_counts.values())
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_names, y=counts)
    plt.title('Distribution of Images by Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Images')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    data = load_annotations('data/keypoints.js')
    category_counts = count_images_by_category(data)
    
    categories = {
        "1": "dog",
        "2": "cat",
        "3": "sheep",
        "4": "horse",
        "5": "cow"
    }
    
    plot_category_distribution(category_counts, categories)
    print(f"Number of cow images: {category_counts.get(5, 0)}")
