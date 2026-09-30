import re

with open("areas.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '<p class="text-blue-100/80 text-sm mb-4">',
    '<p class="text-blue-100/80 text-sm mb-4 min-h-[60px] md:min-h-[80px]">'
)

with open("areas.html", "w", encoding="utf-8") as f:
    f.write(content)

