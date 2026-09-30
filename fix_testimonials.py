import re

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix names
content = re.sub(
    r'<div class="font-bold text-primary-text text-sm">(.*?)</div>',
    r'<div class="font-bold text-primary-text text-sm whitespace-nowrap">\1</div>',
    content
)

# Fix titles/locations
content = re.sub(
    r'<div class="text-secondary-text text-xs">(.*?)</div>',
    r'<div class="text-secondary-text text-xs whitespace-nowrap">\1</div>',
    content
)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

