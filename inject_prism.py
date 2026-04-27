import os
import re

css_tag = '\n    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />'
js_tags = '\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>'

for i in range(1, 12):
    file_path = f"exp{i}.html"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Add CSS if not present
        if "prism-tomorrow" not in content:
            content = content.replace('</head>', f'{css_tag}\n  </head>')
        
        # Add JS if not present
        if "prism.min.js" not in content:
            content = content.replace('</body>', f'{js_tags}\n  </body>')
            
        # Update <pre><code> to <pre><code class="language-python">
        content = re.sub(r'<pre>\s*<code>', '<pre><code class="language-python">', content)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"File {file_path} not found")
