import re

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

# Make the bottom container fixed height so the avatars align perfectly
content = content.replace(
    '<div class="flex items-center gap-3">',
    '<div class="flex items-center gap-3 h-20">'
)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

