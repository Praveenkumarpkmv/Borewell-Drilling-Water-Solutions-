import re

with open("contact.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace padding
content = content.replace(
    'class="bg-background rounded-2xl p-4 border border-border text-center"',
    'class="bg-background rounded-2xl p-2 sm:p-4 border border-border text-center"'
)

# Replace text sizes and add whitespace-nowrap
content = content.replace(
    'class="text-2xl font-bold text-accent mb-1"',
    'class="text-lg sm:text-2xl font-bold text-accent mb-1 whitespace-nowrap"'
)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(content)

