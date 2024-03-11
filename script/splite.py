import os
import shutil
from sklearn.model_selection import train_test_split

# Path to the dataset
data_dir = 'data'
# Where to save the split datasets
output_dir = 'output'

# Ratios for splitting
train_ratio = 0.7
validation_ratio = 0.15
test_ratio = 0.15

# Create the output directories if they don't exist
for split in ['train', 'validation', 'test']:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Loop through each insect type directory
for insect_type in os.listdir(data_dir):
    insect_path = os.path.join(data_dir, insect_type)
    
    # Skip if not a directory
    if not os.path.isdir(insect_path):
        continue
    
    # Get all image filenames
    images = [f for f in os.listdir(insect_path) if os.path.isfile(os.path.join(insect_path, f))]
    
    # Split the data
    train_val, test = train_test_split(images, test_size=test_ratio, random_state=42)
    train, validation = train_test_split(train_val, test_size=validation_ratio / (train_ratio + validation_ratio), random_state=42)
    
    # Function to copy files to the respective directories
    def copy_files(files, dest_folder):
        os.makedirs(os.path.join(output_dir, dest_folder, insect_type), exist_ok=True)
        for f in files:
            src_path = os.path.join(insect_path, f)
            dst_path = os.path.join(output_dir, dest_folder, insect_type, f)
            shutil.copy(src_path, dst_path)
    
    # Copy the files to the respective split directories
    copy_files(train, 'train')
    copy_files(validation, 'validation')
    copy_files(test, 'test')

print("Data split and copied successfully.")
