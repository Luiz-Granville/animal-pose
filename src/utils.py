import os

def create_directory_if_not_exists(directory):
    os.makedirs(directory, exist_ok=True)
