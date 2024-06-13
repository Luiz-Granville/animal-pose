# main.py

import cv2
from matplotlib import pyplot as plt
from src.data_processing import process_image
from src.data_loading import load_annotations
from src.utils import count_images_by_category, filter_bovine_images, get_keypoints_and_skeleton_for_image, get_keypoints_for_image, remove_duplicate_annotations
from src.visualization import create_category_count_table_image, plot_category_distribution, display_results, plot_keypoints

def main():

    data = load_annotations('data/raw/keypoints/keypoints.json')

    data = remove_duplicate_annotations(data)
    
    # Análise Exploratória
    category_counts = count_images_by_category(data)
    
    
    # Filtragem de imagens de bovinos
    bovine_images = filter_bovine_images(data, 'data/raw/keypoints/cow_images')

    print(f"Number of bovine images filtered: {len(bovine_images)}")

    categories = {
        "1": "dog",
        "2": "cat",
        "3": "sheep",
        "4": "horse",
        "5": "cow"
    }

    i = 0

    #Processamento das imagens de bovinos
    for image_name in bovine_images[:5]:  # Mostrando exemplos
        image_path = f"data/raw/keypoints/cow_images/{image_name}"
        image = cv2.imread(image_path)
        keypoints, skeleton = get_keypoints_and_skeleton_for_image(data, image_name)
        processed_image, adjusted_keypoints = process_image(image, keypoints, 600, 600)

        
        output_path = f'./results/processed/cow_{i}.png'
        plot_keypoints(processed_image, adjusted_keypoints, skeleton, output_path=output_path)
        i += 1

    plot_category_distribution(category_counts, categories, output_path='./results/category_distribution.png')

    create_category_count_table_image(category_counts, categories, output_path='./results/category_count_table.png')



if __name__ == "__main__":
    main()
