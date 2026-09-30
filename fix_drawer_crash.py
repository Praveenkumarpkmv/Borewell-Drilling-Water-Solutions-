import re

files = ["login.html", "signup.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Add optional chaining to the drawer listeners
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

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

