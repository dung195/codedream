import os

# Define the parent directory and folder names
parent_dir = "Test"
os.makedirs(parent_dir, exist_ok=True)  # Create the parent "Test" folder if it doesn't exist

# Create subfolders "Test 01" to "Test 05"
for i in range(1, 6):
    folder_name = f"Test {i:02}"  # Format as "Test 01", "Test 02", etc.
    folder_path = os.path.join(parent_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")