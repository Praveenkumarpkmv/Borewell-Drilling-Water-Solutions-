import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# The wrapper is: <div class="fixed top-0 left-0 right-0 z-50 pt-4 pointer-events-none" id="main-header-wrap">\n <header ...>\n ... \n </header>\n </div>
# We want to replace it with just the <header ...> ... </header>

pattern = r'<div[^>]*id="main-header-wrap"[^>]*>\s*(<header[^>]*id="main-header"[^>]*>.*?</header>)\s*</div>'
content = re.sub(pattern, r'\1', content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
