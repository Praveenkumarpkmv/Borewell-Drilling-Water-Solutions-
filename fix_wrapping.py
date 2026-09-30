import re

with open("home2.html", "r", encoding="utf-8") as f:
    content = f.read()

# I will add whitespace-nowrap to the specific div containing "Parameters Tested"
content = content.replace(
    '<div class="text-sm text-secondary-text font-medium">Parameters Tested</div>',
    '<div class="text-sm text-secondary-text font-medium whitespace-nowrap">Parameters Tested</div>'
)

# And might as well do it for the others in this specific block to be safe
content = content.replace(
    '<div class="text-sm text-secondary-text font-medium">Impurity Removal</div>',
    '<div class="text-sm text-secondary-text font-medium whitespace-nowrap">Impurity Removal</div>'
)
content = content.replace(
    '<div class="text-sm text-secondary-text font-medium">Homes Served</div>',
    '<div class="text-sm text-secondary-text font-medium whitespace-nowrap">Homes Served</div>'
)
content = content.replace(
    '<div class="text-sm text-secondary-text font-medium">Client Retention</div>',
    '<div class="text-sm text-secondary-text font-medium whitespace-nowrap">Client Retention</div>'
)

with open("home2.html", "w", encoding="utf-8") as f:
    f.write(content)

