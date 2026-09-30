import re

with open("areas.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace from `<div class="lg:col-span-3">` up to `<!-- Right: Highlights -->` or `<div class="lg:col-span-2 space-y-4">`
pattern = r'<div class="lg:col-span-3">.*?<div class="lg:col-span-2 space-y-4">'

new_html = """<div class="lg:col-span-3">
                        <div class="relative w-full h-[400px] sm:h-[500px] lg:h-full min-h-[400px] rounded-3xl overflow-hidden shadow-2xl group">
                            <img src="asserts/areas2.avif" alt="Our Service Fleet" class="absolute inset-0 w-full h-full object-cover transform transition-transform duration-700 group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1578508496468-b328328eb92f?q=80&w=2000&auto=format&fit=crop';">
                            <!-- Gradient overlay -->
                            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                            
                            <!-- Bottom Info Card -->
                            <div class="absolute bottom-6 left-6 right-6 sm:bottom-8 sm:left-8 sm:right-8">
                                <div class="bg-background/95 backdrop-blur-xl rounded-2xl p-6 border border-border shadow-2xl">
                                    <div class="flex items-center gap-4">
                                        <div class="w-14 h-14 rounded-full bg-accent-light flex items-center justify-center text-accent shrink-0 shadow-inner">
                                            <i class="fa-solid fa-truck-fast text-2xl"></i>
                                        </div>
                                        <div>
                                            <h3 class="text-xl font-bold text-primary-text mb-1">Fleet on the Move</h3>
                                            <p class="text-secondary-text text-sm">Over 15 heavy-duty rigs actively deployed across the region daily.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="lg:col-span-2 space-y-4">"""

content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open("areas.html", "w", encoding="utf-8") as f:
    f.write(content)

