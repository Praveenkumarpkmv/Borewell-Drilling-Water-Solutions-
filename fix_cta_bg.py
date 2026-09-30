import re

with open("about.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the Wavy Background Shape div
pattern = r'<!-- Wavy Background Shape -->.*?</div>'
content = re.sub(pattern, '', content, flags=re.DOTALL)

with open("about.html", "w", encoding="utf-8") as f:
    f.write(content)
