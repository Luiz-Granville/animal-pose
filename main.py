from src import exploratory_analysis
from src import data_processing
from src import results
import os

def main():
    # Execute a análise exploratória
    bovine_annotations = 'data/processed/bovine_annotations.json'
    exploratory_analysis.exploratory_analysis(bovine_annotations)

    # Execute o processamento de dados
    from src.data_loading import load_annotations
    
    keypoints_path = 'data/raw/keypoints/keypoints.json'
    keypoints_data = load_annotations(keypoints_path)
    
    bounding_box_annotations_dir = 'data/raw/bounding_boxes/annotations/'
    bounding_box_annotations = {}
    for file_name in os.listdir(bounding_box_annotations_dir):
        if file_name.endswith('.json'):
            category = file_name.split('.')[0]
            bounding_box_annotations[category] = load_annotations(os.path.join(bounding_box_annotations_dir, file_name))
    
    bovine_images, bovine_annotations = data_processing.filter_bovine_data(keypoints_data, bounding_box_annotations)
    data_processing.save_processed_data(bovine_images, bovine_annotations)

    # Execute a geração de resultados
    results.generate_results(bovine_annotations)

if __name__ == "__main__":
    
    main()

