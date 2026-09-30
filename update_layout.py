import os
from bs4 import BeautifulSoup
import re

def main():
    target_dir = "."
    files = [f for f in os.listdir(target_dir) if f.endswith(".html")]

    with open("about.html", "r", encoding="utf-8") as f:
        about_soup = BeautifulSoup(f.read(), "html.parser")
    
    header = about_soup.find("header", id="main-header")
    mobile_menu = about_soup.find("div", id="mobile-menu-drawer")
    footer = about_soup.find("footer", id="main-footer")
    
    # Also find the script at the bottom that might contain navbar logic
    scripts = about_soup.find_all("script")
    bottom_script = None
    for script in scripts:
        if script.string and "setActiveNavLink" in script.string:
            bottom_script = script
            break
            
    if not bottom_script and scripts:
        bottom_script = scripts[-1]

    for fname in files:
        if fname in ["about.html", "services.html"]:
            continue
            
        print(f"Updating {fname}...")
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
            
        soup = BeautifulSoup(content, "html.parser")
        
        target_header = soup.find("header", id="main-header")
        if target_header and header:
            target_header.replace_with(BeautifulSoup(str(header), "html.parser").header)
            
        target_mobile_menu = soup.find("div", id="mobile-menu-drawer")
        if target_mobile_menu and mobile_menu:
            target_mobile_menu.replace_with(BeautifulSoup(str(mobile_menu), "html.parser").div)
            
        target_footer = soup.find("footer", id="main-footer")
        if target_footer and footer:
            target_footer.replace_with(BeautifulSoup(str(footer), "html.parser").footer)
            
        # Optional: replace the script if needed
        # Just write back using original content with regex to preserve exact formatting if possible
        # Actually BS4 formatting can mess up the original formatting.
        
        # We can use regex for safer replacement without destroying format.

if __name__ == "__main__":
    main()
