import re

with open("contact.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix heading centering explicitly
content = content.replace(
    '<div class="text-center mb-16">',
    '<div class="flex flex-col items-center justify-center text-center mb-12">'
)
content = content.replace(
    '<span class="text-transparent bg-clip-text',
    '<span class="inline-block text-transparent bg-clip-text'
)

# Fix Cards
# Reduce grid max width
content = content.replace(
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">',
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-3xl mx-auto">'
)

# Call Card size reduction
content = content.replace(
    'class="group relative bg-background rounded-3xl p-8 border',
    'class="group relative bg-background rounded-2xl p-6 border'
)
content = content.replace(
    'class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-accent tracking-tight my-6 group-hover:scale-105 transition-transform duration-300"',
    'class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-accent tracking-tight my-4 group-hover:scale-105 transition-transform duration-300"'
)

# Email Card size reduction
content = content.replace(
    'class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-primary-text tracking-tight my-6 group-hover:scale-105 transition-transform duration-300"',
    'class="text-xl sm:text-2xl lg:text-3xl font-extrabold text-primary-text tracking-tight my-4 group-hover:scale-105 transition-transform duration-300"'
)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(content)

