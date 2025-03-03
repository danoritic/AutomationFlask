import os
import json
import shutil

# Create the required output directory structure for Vercel
os.makedirs(".vercel/output/static", exist_ok=True)
os.makedirs(".vercel/output/functions/vercel_app.func", exist_ok=True)
os.makedirs("data/screenshots", exist_ok=True)

# Create static data directory if it doesn't exist
os.makedirs("data", exist_ok=True)
os.makedirs("data/screenshots", exist_ok=True)

# Make sure data directory is writable
os.system("chmod -R 777 data")

# Create a config file for the function
config = {
    "runtime": "python3.9",
    "handler": "vercel_app.py",
    "excludeFiles": "(^test/.*|screenshots/.*)"
}

# Write the config to a file
with open(".vercel/output/functions/vercel_app.func/config.json", "w") as f:
    json.dump(config, f)

# Copy all the necessary files to the function directory
def copy_recursively(source_dir, target_dir, ignore=None):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)
        
        if ignore and item in ignore:
            continue
            
        if os.path.isdir(source_item):
            copy_recursively(source_item, target_item, ignore)
        else:
            shutil.copy2(source_item, target_item)

# Copy the application files
copy_recursively(".", ".vercel/output/functions/vercel_app.func", 
                ignore=[".git", ".vercel", "venv", "__pycache__", "node_modules"])

# Create a simple _static.json file
with open(".vercel/output/static/_static.json", "w") as f:
    json.dump({"type": "static"}, f)

print("Build completed successfully!") 
