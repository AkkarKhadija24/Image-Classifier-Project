import os

# Specify the directory path you want to list the files from
directory_path = 'output/train'

# Initialize an empty list to store file names
file_names = []

# Iterate over all the files in the directory
for filename in os.listdir(directory_path):
    file_names.append(filename)
    

# Print the list of file names
print(file_names)