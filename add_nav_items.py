import os
import glob

# Search blocks
desktop_search = '''                    <a href="areas.html" class="nav-link">Service Areas</a>
                    <a href="contact.html" class="nav-link">Contact</a>'''

desktop_replace = '''                    <a href="areas.html" class="nav-link">Service Areas</a>
                    <a href="work.html" class="nav-link">Our Work</a>
                    <a href="quote.html" class="nav-link">Get a Quote</a>
                    <a href="contact.html" class="nav-link">Contact</a>'''

mobile_search = '''                <a href="areas.html" class="block text-primary-text font-semibold text-lg py-2">Service Areas</a>
                <a href="contact.html" class="block text-primary-text font-semibold text-lg py-2">Contact</a>'''

mobile_replace = '''                <a href="areas.html" class="block text-primary-text font-semibold text-lg py-2">Service Areas</a>
                <a href="work.html" class="block text-primary-text font-semibold text-lg py-2">Our Work</a>
                <a href="quote.html" class="block text-primary-text font-semibold text-lg py-2">Get a Quote</a>
                <a href="contact.html" class="block text-primary-text font-semibold text-lg py-2">Contact</a>'''

footer_search = '''                        <li><a href="areas.html" class="footer-link">Service Areas</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>'''

footer_replace = '''                        <li><a href="areas.html" class="footer-link">Service Areas</a></li>
                        <li><a href="work.html" class="footer-link">Our Work</a></li>
                        <li><a href="quote.html" class="footer-link">Get a Quote</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>'''


for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = content.replace(desktop_search, desktop_replace)
    modified = modified.replace(mobile_search, mobile_replace)
    modified = modified.replace(footer_search, footer_replace)
    
    if modified != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(modified)
        print(f"Updated {file}")

