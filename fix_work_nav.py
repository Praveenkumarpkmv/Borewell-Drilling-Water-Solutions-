import re

def get_section(filename, start_tag, end_tag):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find the section
    pattern = f"({start_tag}.*?{end_tag})"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def replace_section(filename, start_tag, end_tag, new_content):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = f"{start_tag}.*?{end_tag}"
    new_file_content = re.sub(pattern, new_content, content, flags=re.DOTALL | re.IGNORECASE)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_file_content)

# Get sections from index.html
head_content = get_section("index.html", "<head>", "</head>")
header_content = get_section("index.html", "<header", "</header>")
# Also the mobile drawer which is <div id="mobile-drawer" ... </div> right after header usually. Wait, in this project the drawer is <div id="mobile-drawer" class="...">...</div> 
# Let's check how the drawer is delimited
