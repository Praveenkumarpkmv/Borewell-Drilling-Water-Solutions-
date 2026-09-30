import re

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

# I will change step-connector to span the whole width, except for the first one?
# Or just span from center to center?
# The standard way to connect a grid is `left: -50%; right: 50%;` on items 2, 3, 4.
# But it's easier to just use `left: -20px; right: -20px;` or similar.
# Actually, if I just do `left: -50px; right: -50px;` on all of them, the line will be continuous, but stick out on the ends. 
# But let's look at the screenshot. The line sticks out on both sides of 1, 2, 3!
content = content.replace(
    '''        .step-connector {
            position: absolute;
            top: 40px;
            left: 40px;
            right: -20px;''',
    '''        .step-connector {
            position: absolute;
            top: 40px;
            left: -30px;
            right: -30px;'''
)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

