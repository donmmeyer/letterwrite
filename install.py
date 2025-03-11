import os
import shutil
from pathlib import Path

def setup_environment(target_location):
    # Set the source package directory explicitly
    package_dir = Path("C:/Users/don_m/anaconda3/Lib/site-packages/letterwrite")

    # Define subfolders to copy
    folders_to_copy = ["formbase", "contacts", "log"]

    # Ensure the target location exists
    os.makedirs(target_location, exist_ok=True)

    # Copy each folder
    for folder in folders_to_copy:
        source_folder = package_dir / folder
        destination_folder = Path(target_location) / folder

        if source_folder.exists():
            shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)
            print(f"Copied {source_folder} to {destination_folder}")
        else:
            print(f"Source folder {source_folder} does not exist.")


# Example usage
setup_environment("C:/Users/don_m/Python/ZDAnalytics/temp")