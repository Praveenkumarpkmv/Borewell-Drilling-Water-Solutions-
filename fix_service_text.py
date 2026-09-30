import re

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the invisible bg-clip-text with solid text-accent
content = content.replace(
    '<span class="text-transparent bg-clip-text bg-gradient-to-r from-accent to-blue-400">',
    '<span class="text-accent">'
)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

