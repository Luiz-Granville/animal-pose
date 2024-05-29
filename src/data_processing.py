import os
import json

def filter_bovine_data(keypoints_data, bounding_box_annotations):
    bovine_images = []
    bovine_annotations = {}
    
    # Filtrando as anotações de keypoints para bovinos
    for image_id, image_file in keypoints_data['images'].items():
        if 'cow' in image_file:  # Assumindo que 'cow' está presente no nome do arquivo de bovinos
            bovine_images.append({"id": image_id, "file_name": image_file})
            bovine_annotations[image_file] = bounding_box_annotations.get(image_file, [])
    
    return bovine_images, bovine_annotations

def save_processed_data(bovine_images, bovine_annotations):
    os.makedirs('data/processed/bovine_images', exist_ok=True)
    for image in bovine_images:
        image_path = os.path.join('data/raw/keypoints/images', image['file_name'])
        if os.path.exists(image_path):
            os.rename(image_path, os.path.join('data/processed/bovine_images', image['file_name']))
    
    with open('data/processed/bovine_annotations.json', 'w') as f:
        json.dump({'images': bovine_images, 'bounding_boxes': bovine_annotations}, f)

