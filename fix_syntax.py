import re

files = ["login.html", "signup.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Revert the broken theme logic and apply the correct one
    # Current broken:
    # themeToggles.forEach(btn => {
    #             if(btn) btn.addEventListener('click', () => {
    #
    #                 const next = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    #                 localStorage.setItem('theme', next);
    #                 applyTheme(next);
    #             }));

    content = content.replace(
        """themeToggles.forEach(btn => {
                if(btn) btn.addEventListener('click', () => {

                const next = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
                localStorage.setItem('theme', next);
                applyTheme(next);
            }));""",
        """themeToggles.forEach(btn => btn && btn.addEventListener('click', () => {
                const next = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
                localStorage.setItem('theme', next);
                applyTheme(next);
            }));"""
    )
    
    # Also the first script applied:
    # langToggles.forEach(btn => btn && btn.addEventListener('click', () => {
    # This one is probably fine since I only ran the second replace on it.

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

