import re
import glob

# The pattern we want to match:
# <p class="text-lg leading-relaxed max-w-sm !text-white-400">
#     Rugged, dependable ...
# </p>                    
# <div class="flex gap-6 mt-10">

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add mt-5 to the paragraph, change mt-10 to mt-6 on the icons div
    content = content.replace(
        '<p class="text-lg leading-relaxed max-w-sm !text-white-400">',
        '<p class="text-lg leading-relaxed max-w-sm !text-white-400 mt-5">'
    )
    
    content = content.replace(
        '<div class="flex gap-6 mt-10">',
        '<div class="flex gap-6 mt-5">'
    )
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Spacing fixed!")
