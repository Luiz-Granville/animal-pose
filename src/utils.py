# src/utils.py

# Função para contar as imagens por categoria
def count_images_by_category(data):
    category_counts = {}
    for annotation in data['annotations']:
        category_id = annotation['category_id']
        if category_id in category_counts:
            category_counts[category_id] += 1
        else:
            category_counts[category_id] = 1
    return category_counts

def filter_bovine_images(data, output_dir):
    import os
    import shutil

    bovine_images = []
    for annotation in data['annotations']:
        if annotation['category_id'] == 5:  # Category ID for cows
            bovine_images.append(data['images'][str(annotation['image_id'])])
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for image in bovine_images:
        shutil.copy(os.path.join('data/raw/keypoints/images', image), os.path.join(output_dir, image))
    
    return bovine_images

def get_keypoints_for_image(data, image_name):
    image_id = None
    for key, value in data['images'].items():
        if value == image_name:
            image_id = int(key)
            break
    if image_id is None:
        return []
    
    for annotation in data['annotations']:
        if annotation['image_id'] == image_id:
            return annotation['keypoints']
    return []

def get_keypoints_and_skeleton_for_image(data, image_name):
    image_id = None
    category_id = None
    for key, value in data['images'].items():
        if value == image_name:
            image_id = int(key)
            break
    if image_id is None:
        return [], []
    
    for annotation in data['annotations']:
        if annotation['image_id'] == image_id:
            keypoints = annotation['keypoints']
            category_id = annotation['category_id']
            break
    
    if category_id is None:
        return keypoints, []
    
    skeleton = None
    for category in data['categories']:
        if category['id'] == category_id:
            skeleton = category['skeleton']
            break
    
    return keypoints, skeleton

def remove_duplicate_annotations(data):
    unique_annotations = []
    seen_image_ids = set()
    
    for annotation in data['annotations']:
        if annotation['image_id'] not in seen_image_ids:
            unique_annotations.append(annotation)
            seen_image_ids.add(annotation['image_id'])
    
    data['annotations'] = unique_annotations
    return data