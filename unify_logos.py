import re
import glob

# We will find all instances of the logo block and replace them with a unified identical block.

# Find everything that looks like:
# <a href="index.html" class="... font-serif ...">
#     <i class="fa-solid fa-water ..."></i>
#     <span class="...">AQUADRILL</span>
# </a>

unified_logo = """<a href="index.html" class="font-serif font-extrabold tracking-wide flex items-center gap-2 shrink-0 mb-0" style="font-size: 28px !important; line-height: 1 !important; text-decoration: none;">    
    <i class="fa-solid fa-water" style="color: #2563EB !important; font-size: 28px !important;"></i>
    <span style="color: #2563EB !important; font-size: 28px !important; letter-spacing: 1px;">AQUADRILL</span>
</a>"""

# Mobile drawer might need a smaller one, but user said "both should be in same size and color". 
# So we'll make them all identical.

# We'll use regex to replace all logos.
pattern = r'<a href="index\.html"[^>]*?font-serif[^>]*?>\s*<i class="fa-solid fa-water[^>]*></i>\s*<span[^>]*>AQUADRILL</span>\s*</a>'

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = re.sub(pattern, unified_logo, content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)
        
print("Done unifying logos.")
