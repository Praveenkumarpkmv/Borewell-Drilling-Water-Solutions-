import os
import re

def extract_block(text, start_marker, end_marker):
    start = text.find(start_marker)
    if start == -1:
        return None
    end = text.find(end_marker, start)
    if end == -1:
        return None
    end += len(end_marker)
    return text[start:end]

def extract_tag(text, tag, tag_id):
    import re
    # Match the opening tag with the specific id
    pattern = re.compile(rf'<{tag}[^>]*id="{tag_id}"[^>]*>', re.IGNORECASE)
    match = pattern.search(text)
    if not match:
        return None
        
    start_idx = match.start()
    
    # Simple tag balancer
    depth = 0
    i = start_idx
    tag_start = rf'<{tag}\b'
    tag_end = rf'</{tag}>'
    tag_start_re = re.compile(tag_start, re.IGNORECASE)
    tag_end_re = re.compile(tag_end, re.IGNORECASE)
    
    while i < len(text):
        next_start_match = tag_start_re.search(text, i)
        next_end_match = tag_end_re.search(text, i)
        
        if not next_start_match and not next_end_match:
            break
            
        start_pos = next_start_match.start() if next_start_match else float('inf')
        end_pos = next_end_match.start() if next_end_match else float('inf')
        
        if start_pos < end_pos:
            depth += 1
            i = next_start_match.end()
        else:
            depth -= 1
            i = next_end_match.end()
            
        if depth == 0:
            return text[start_idx:i]
            
    return None

def main():
    with open("about.html", "r", encoding="utf-8") as f:
        about_text = f.read()

    header_block = extract_tag(about_text, "header", "main-header")
    drawer_block = extract_tag(about_text, "div", "mobile-menu-drawer")
    footer_block = extract_tag(about_text, "footer", "main-footer")
    
    # Extract scripts
    script_start = about_text.rfind("<script>")
    script_end = about_text.rfind("</script>") + len("</script>")
    script_block = about_text[script_start:script_end]

    files = [f for f in os.listdir(".") if f.endswith(".html")]
    for fname in files:
        if fname in ["about.html", "services.html"]:
            continue
            
        print(f"Processing {fname}...")
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
            
        orig_header = extract_tag(content, "header", "main-header")
        if orig_header and header_block:
            content = content.replace(orig_header, header_block)
            
        orig_drawer = extract_tag(content, "div", "mobile-menu-drawer")
        if orig_drawer and drawer_block:
            content = content.replace(orig_drawer, drawer_block)
            
        orig_footer = extract_tag(content, "footer", "main-footer")
        if orig_footer and footer_block:
            content = content.replace(orig_footer, footer_block)
            
        # replace bottom script
        orig_script_start = content.rfind("<script>")
        orig_script_end = content.rfind("</script>") + len("</script>")
        if orig_script_start != -1 and script_start != -1:
            orig_script_block = content[orig_script_start:orig_script_end]
            content = content.replace(orig_script_block, script_block)
            
        with open(fname, "w", encoding="utf-8") as f:
            f.write(content)
            
if __name__ == "__main__":
    main()
