import os

for i in range(1, 12):
    file_path = f"exp{i}.html"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if '<script src="script.js"></script>' not in content:
            content = content.replace(
                '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>',
                '<script src="script.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>'
            )
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {file_path}")
