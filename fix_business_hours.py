import re

with open("contact.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Monday - Friday with Mon - Fri and add text-xs sm:text-sm
content = content.replace(
    '<span class="text-secondary-text">Monday – Friday</span>',
    '<span class="text-secondary-text text-xs sm:text-sm whitespace-nowrap">Mon – Fri</span>'
)
content = content.replace(
    '<span class="font-bold text-primary-text">9:00 AM – 7:00 PM</span>',
    '<span class="font-bold text-primary-text text-xs sm:text-sm whitespace-nowrap">9:00 AM – 7:00 PM</span>'
)

# Apply to Saturday
content = content.replace(
    '<span class="text-secondary-text">Saturday</span>',
    '<span class="text-secondary-text text-xs sm:text-sm whitespace-nowrap">Saturday</span>'
)
content = content.replace(
    '<span class="font-bold text-primary-text">10:00 AM – 5:00 PM</span>',
    '<span class="font-bold text-primary-text text-xs sm:text-sm whitespace-nowrap">10:00 AM – 5:00 PM</span>'
)

# Apply to Sunday
content = content.replace(
    '<span class="text-secondary-text">Sunday</span>',
    '<span class="text-secondary-text text-xs sm:text-sm whitespace-nowrap">Sunday</span>'
)
content = content.replace(
    '<span class="text-xs font-bold text-accent bg-accent-light px-2.5 py-1 rounded-full">Emergency Only</span>',
    '<span class="text-[10px] sm:text-xs font-bold text-accent bg-accent-light px-2.5 py-1 rounded-full whitespace-nowrap">Emergency Only</span>'
)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(content)

