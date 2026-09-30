import re

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add step-connector to 04
content = content.replace(
    '''<div class="relative text-center">
                        <div class="relative inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-custom-gradient text-white text-2xl font-bold shadow-xl mb-5 z-10">04</div>''',
    '''<div class="relative text-center">
                        <div class="step-connector"></div>
                        <div class="relative inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-custom-gradient text-white text-2xl font-bold shadow-xl mb-5 z-10">04</div>'''
)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

