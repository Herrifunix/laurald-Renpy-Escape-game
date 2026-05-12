import os
import re

# 1. Build an index of all exact image paths
image_index = {}
images_dir = os.path.join('game', 'images')
for root, dirs, files in os.walk(images_dir):
    for file in files:
        rel_path = os.path.relpath(os.path.join(root, file), images_dir).replace('\\', '/')
        image_index[file] = rel_path

# 2. Check all rpy files and automatically fix them
for root, dirs, files in os.walk('game'):
    for file in files:
        if file.endswith('.rpy'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Find all references starting with 'images/' or "images/"
            # e.g. "images/gui/click1.png"
            def replacer(match):
                quote = match.group(1)
                referenced_path = match.group(2)
                
                # Check if it actually exists there
                full_ref_path = os.path.join(images_dir, referenced_path.replace('/', os.sep))
                if not os.path.exists(full_ref_path):
                    filename = os.path.basename(referenced_path)
                    # If it exists somewhere else in game/images
                    if filename in image_index:
                        new_rel_path = image_index[filename]
                        print(f"[FIX] {file_path}: {referenced_path} -> {new_rel_path}")
                        return f"{quote}images/{new_rel_path}{quote}"
                    else:
                        print(f"[WARNING] Missing completely: {referenced_path} in {file_path}")
                return match.group(0)

            new_content = re.sub(r'([\'"])images/([^\'\"]+)[\'"]', replacer, content)
            
            if new_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file_path}")

print("Validation and fix complete.")
