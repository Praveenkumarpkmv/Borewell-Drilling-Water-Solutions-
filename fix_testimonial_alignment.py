import re

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

# Modify the CSS for testimonial-card
content = content.replace(
    '''        .testimonial-card {
            background: var(--color-background);
            border: 1.5px solid var(--color-border);
            border-radius: 1.5rem;
            padding: 1.75rem;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }''',
    '''        .testimonial-card {
            background: var(--color-background);
            border: 1.5px solid var(--color-border);
            border-radius: 1.5rem;
            padding: 1.75rem;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }'''
)

# Add flex-1 to the paragraphs so they stretch and push the avatars down
content = content.replace(
    '<p class="text-secondary-text text-sm leading-relaxed mb-6 italic">',
    '<p class="text-secondary-text text-sm leading-relaxed mb-6 italic flex-1">'
)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

