import re

with open("404.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix drawer crash
content = content.replace(
    "document.getElementById('mobile-menu-open').addEventListener('click', openDrawer);",
    "document.getElementById('mobile-menu-open')?.addEventListener('click', openDrawer);"
)
content = content.replace(
    "document.getElementById('mobile-menu-close').addEventListener('click', closeDrawer);",
    "document.getElementById('mobile-menu-close')?.addEventListener('click', closeDrawer);"
)
content = content.replace(
    "menuBackdrop.addEventListener('click', closeDrawer);",
    "menuBackdrop?.addEventListener('click', closeDrawer);"
)

# Fix toggles crash
content = content.replace(
    "themeToggles.forEach(btn => btn.addEventListener('click', () => {",
    "themeToggles.forEach(btn => btn && btn.addEventListener('click', () => {"
)
content = content.replace(
    "langToggles.forEach(btn => btn.addEventListener('click', () => {",
    "langToggles.forEach(btn => btn && btn.addEventListener('click', () => {"
)

with open("404.html", "w", encoding="utf-8") as f:
    f.write(content)

