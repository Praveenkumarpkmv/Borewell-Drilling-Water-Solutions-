import re

files = ["login.html", "signup.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix theme toggles
    content = content.replace(
        "themeToggles.forEach(btn => btn.addEventListener('click', () => {",
        "themeToggles.forEach(btn => {\n                if(btn) btn.addEventListener('click', () => {\n"
    )
    # The replacement for the closing bracket of the forEach is a bit tricky, let's just use regex for both:
    # Actually, we can just replace `btn => btn.addEventListener` with `btn => btn && btn.addEventListener`
    
    content = content.replace(
        "themeToggles.forEach(btn => btn.addEventListener",
        "themeToggles.forEach(btn => btn && btn.addEventListener"
    )
    
    content = content.replace(
        "langToggles.forEach(btn => btn.addEventListener",
        "langToggles.forEach(btn => btn && btn.addEventListener"
    )

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

