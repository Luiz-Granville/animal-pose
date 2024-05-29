import json
import os

def load_annotations(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def load_images(image_dir):
    image_files = []
    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.endswith('.jpg'):
                image_files.append(os.path.join(root, file))
    return image_files

if __name__ == "__main__":
    keypoints_path = 'data/raw/keypoints/keypoints.json'
    keypoints_data = load_annotations(keypoints_path)
    
    bounding_box_annotations_dir = 'data/raw/bounding_boxes/annotations/'
    bounding_box_annotations = {}
    for file_name in os.listdir(bounding_box_annotations_dir):
        if file_name.endswith('.json'):
            category = file_name.split('.')[0]
            bounding_box_annotations[category] = load_annotations(os.path.join(bounding_box_annotations_dir, file_name))
    
    bounding_box_images_dir = 'data/raw/bounding_boxes/images/'
    bounding_box_images = {}
    for category in os.listdir(bounding_box_images_dir):
        category_path = os.path.join(bounding_box_images_dir, category)
        if os.path.isdir(category_path):
            bounding_box_images[category] = load_images(category_path)
