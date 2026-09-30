import re

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add shrink-0 to the avatar divs (RV, SP, AK)
content = content.replace(
    '<div class="w-12 h-12 rounded-full bg-custom-gradient flex items-center justify-center font-bold text-white text-sm">RV</div>',
    '<div class="w-12 h-12 rounded-full bg-custom-gradient flex items-center justify-center font-bold text-white text-sm shrink-0">RV</div>'
)
content = content.replace(
    '<div class="w-12 h-12 rounded-full bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center font-bold text-white text-sm">SP</div>',
    '<div class="w-12 h-12 rounded-full bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center font-bold text-white text-sm shrink-0">SP</div>'
)
content = content.replace(
    '<div class="w-12 h-12 rounded-full bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center font-bold text-white text-sm">AK</div>',
    '<div class="w-12 h-12 rounded-full bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center font-bold text-white text-sm shrink-0">AK</div>'
)

# Remove whitespace-nowrap from the text to allow wrapping if necessary
content = content.replace(
    '<div class="font-bold text-primary-text text-sm whitespace-nowrap">',
    '<div class="font-bold text-primary-text text-sm">'
)
content = content.replace(
    '<div class="text-secondary-text text-xs whitespace-nowrap">',
    '<div class="text-secondary-text text-xs">'
)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

