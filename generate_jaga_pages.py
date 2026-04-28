import os

jaga_files = [
    ("A_star.py", "jaga_astar.html", "A* Search Algorithm"),
    ("Decision_tree.py", "jaga_decision_tree.html", "Decision Tree"),
    ("Linear_regeression(with package).py", "jaga_linear_regression_pkg.html", "Linear Regression (with package)"),
    ("Linear_regeression(without package).py", "jaga_linear_regression_nopkg.html", "Linear Regression (without package)"),
    ("Multilayer_perceptron.py", "jaga_mlp.html", "Multilayer Perceptron"),
    ("Naive_bayes.py", "jaga_naive_bayes.html", "Naive Bayes"),
    ("Water_jug(BFS).py", "jaga_water_jug_bfs.html", "Water Jug (BFS)"),
    ("Water_jug(DFS).py", "jaga_water_jug_dfs.html", "Water Jug (DFS)"),
    ("XGBoost.py", "jaga_xgboost.html", "XGBoost Regressor"),
    ("tic_tac_toe(exhaustive).py", "jaga_tictactoe_exhaustive.html", "Tic Tac Toe (Exhaustive)"),
    ("tic_tac_toe(minmax).py", "jaga_tictactoe_minmax.html", "Tic Tac Toe (Minimax)")
]

html_template = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>2 - {title}</title>
    <link rel="stylesheet" href="style.css" />
    <!-- PrismJS Dark Theme -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
  </head>
  <body>
    <header>
      <h1>{title}</h1>
      <div style="margin-top: 1rem;">
        <a href="jaga.html" class="copy-btn" style="text-decoration: none;">&larr; Back to 2's Repository</a>
      </div>
    </header>
    <main>
      <div class="experiment-content">
        <h2>Source Code: {filename}</h2>
        <button class="copy-btn" onclick="copyCode(this)">Copy Code</button>
        <pre><code class="language-python">{code_content}</code></pre>
      </div>
    </main>
    <script src="script.js"></script>
    <!-- PrismJS Core and Python language support -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  </body>
</html>
"""

for filename, out_html, title in jaga_files:
    # Choose the file that actually has content
    target_file = None
    base_file = os.path.join("Jaga_code", filename)
    base, ext = os.path.splitext(filename)
    alt_file = os.path.join("Jaga_code", f"{base} (1){ext}")
    
    # Check alternate file first since it usually has the content
    if os.path.exists(alt_file) and os.path.getsize(alt_file) > 0:
        target_file = alt_file
    elif os.path.exists(base_file) and os.path.getsize(base_file) > 0:
        target_file = base_file
    elif os.path.exists(base_file):
        target_file = base_file # fallback to empty if nothing else
    
    if target_file and os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            code = f.read()
            # Escape HTML characters so they render correctly in the code block
            code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            
        with open(out_html, "w", encoding="utf-8") as f:
            f.write(html_template.format(title=title, filename=filename, code_content=code))
        print(f"Created {out_html} from {target_file}")
    else:
        print(f"Could not find valid file for {filename}")

# Generate jaga.html
jaga_index_template = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>2 Profile - Code</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <header>
      <h1>2's Repository</h1>
      <p>Explore code implementations</p>
      <input type="text" id="search" placeholder="Search files..." />
      <div style="margin-top: 1rem;">
        <a href="index.html" class="copy-btn" style="text-decoration: none;">&larr; Back to Profiles</a>
      </div>
    </header>
    <main>
      <div class="experiments-list">
{cards}
      </div>
    </main>
    <script src="script.js"></script>
  </body>
</html>
"""

cards = ""
for filename, out_html, title in jaga_files:
    cards += f"""        <div class="experiment-card">
          <h2><a href="{out_html}">{title}</a></h2>
          <p>File: {filename}</p>
        </div>\n"""

with open("jaga.html", "w", encoding="utf-8") as f:
    f.write(jaga_index_template.replace("{cards}", cards))
print("Created jaga.html")
