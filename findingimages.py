import os

def strip_extension(file_name):
    return os.path.splitext(file_name)[0]

def sync_directories(dir1, dir2):
    # Get the base names (without extensions) of files in each directory
    files_in_dir1 = {strip_extension(f) for f in os.listdir(dir1)}
    files_in_dir2 = {strip_extension(f) for f in os.listdir(dir2)}
    
    # Identify files in dir2 that don't have a corresponding file in dir1 (ignoring extensions)
    extra_files_in_dir2 = [f for f in os.listdir(dir2) if strip_extension(f) not in files_in_dir1]
    
    # Delete the extra files in dir2
    for file in extra_files_in_dir2:
        file_path = os.path.join(dir2, file)
        try:
            os.remove(file_path)
            print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")
# Usage
dir1 = 'C:/RoboLabCopy/data/masks'
dir2 = 'C:/RoboLabCopy/data/images/train'
sync_directories(dir1, dir2)

