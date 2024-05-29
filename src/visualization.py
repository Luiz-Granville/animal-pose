import cv2
import matplotlib.pyplot as plt

def process_image(image_path, bounding_boxes):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    for bbox in bounding_boxes:
        cv2.rectangle(image, (bbox['xmin'], bbox['ymin']), (bbox['xmax'], bbox['ymax']), (0, 255, 0), 2)
    
    return image

def visualize_sample(image_path, bounding_boxes):
    processed_image = process_image(image_path, bounding_boxes)
    plt.imshow(processed_image)
    plt.show()

if __name__ == "__main__":
    with open('data/processed/bovine_annotations.json', 'r') as f:
       
        bovine_data = json.load(f)
    
    # Visualizar uma amostra de imagem com caixas delimitadoras
    sample_image_data = bovine_data['images'][0]
    sample_image_path = os.path.join('data/processed/bovine_images', sample_image_data['file_name'])
    sample_bounding_boxes = bovine_data['bounding_boxes'].get(sample_image_data['file_name'], [])
    
    visualize_sample(sample_image_path, sample_bounding_boxes)
