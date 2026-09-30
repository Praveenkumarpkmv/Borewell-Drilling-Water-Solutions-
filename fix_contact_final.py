import re

with open("contact.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix heading text rendering issues
content = content.replace(
    '<h2 class="text-4xl sm:text-5xl md:text-6xl font-bold mb-6 text-primary-text leading-tight">\n                        Prefer to Talk <span class="inline-block text-transparent bg-clip-text bg-gradient-to-r from-accent to-cyan-500">Right Now?</span>\n                    </h2>',
    '<h2 class="text-3xl sm:text-4xl md:text-5xl font-extrabold mb-6 text-primary-text leading-tight text-center w-full">\n                        Prefer to Talk <span class="text-accent">Right Now?</span>\n                    </h2>'
)

# Make cards even smaller
content = content.replace(
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-3xl mx-auto">',
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-2xl mx-auto">'
)

content = content.replace(
    'class="group relative bg-background rounded-2xl p-6 border',
    'class="group relative bg-background rounded-2xl p-5 border'
)

# Shrink phone text size
content = content.replace(
    'class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-accent tracking-tight my-4',
    'class="text-xl sm:text-2xl lg:text-3xl font-extrabold text-accent tracking-tight my-3'
)

# Shrink email text size
content = content.replace(
    'class="text-xl sm:text-2xl lg:text-3xl font-extrabold text-primary-text tracking-tight my-4',
    'class="text-lg sm:text-xl lg:text-2xl font-extrabold text-primary-text tracking-tight my-3'
)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(content)

