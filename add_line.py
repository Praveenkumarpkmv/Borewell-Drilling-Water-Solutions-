import re

with open("contact.html", "r", encoding="utf-8") as f:
    content = f.read()

# Current section 1 opening tag: <section class="relative w-full pt-32 pb-20 overflow-hidden bg-background">
# I'll add border-b border-border to it.

new_class = 'class="relative w-full pt-32 pb-20 overflow-hidden bg-background border-b border-border"'
content = content.replace('class="relative w-full pt-32 pb-20 overflow-hidden bg-background"', new_class)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(content)
