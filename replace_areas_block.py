import re

with open("areas.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'<div class="lg:col-span-3">.*?<div class="lg:col-span-2 space-y-4">'

new_html = """<div class="lg:col-span-3 h-full flex flex-col justify-center bg-background rounded-3xl p-8 sm:p-12 border border-border shadow-2xl relative overflow-hidden group">
                        <!-- Decorative subtle background -->
                        <div class="absolute -top-24 -right-24 w-64 h-64 bg-accent/5 rounded-full blur-[80px] pointer-events-none"></div>
                        
                        <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-accent/10 text-accent text-sm font-bold tracking-wide uppercase mb-8 self-start border border-accent/20">
                            <i class="fa-solid fa-layer-group"></i> Coverage Sectors
                        </div>
                        
                        <h2 class="text-3xl sm:text-4xl font-extrabold text-primary-text mb-10 leading-tight">
                            Engineered for Every <span class="text-accent">Terrain.</span>
                        </h2>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6">
                            
                            <!-- Sector 1 -->
                            <div class="flex items-start gap-4 p-4 sm:p-5 rounded-2xl bg-hover border border-transparent hover:border-border transition-all duration-300 hover:shadow-md hover:-translate-y-1">
                                <div class="w-12 h-12 rounded-xl bg-background border border-border text-accent flex items-center justify-center shrink-0 shadow-sm">
                                    <i class="fa-solid fa-city text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary-text mb-1">Urban Metro</h4>
                                    <p class="text-secondary-text text-sm leading-relaxed">Compact rigs designed for tight residential spaces.</p>
                                </div>
                            </div>

                            <!-- Sector 2 -->
                            <div class="flex items-start gap-4 p-4 sm:p-5 rounded-2xl bg-hover border border-transparent hover:border-border transition-all duration-300 hover:shadow-md hover:-translate-y-1">
                                <div class="w-12 h-12 rounded-xl bg-background border border-border text-accent flex items-center justify-center shrink-0 shadow-sm">
                                    <i class="fa-solid fa-industry text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary-text mb-1">Industrial Belts</h4>
                                    <p class="text-secondary-text text-sm leading-relaxed">High-yield, large diameter drilling for factories.</p>
                                </div>
                            </div>

                            <!-- Sector 3 -->
                            <div class="flex items-start gap-4 p-4 sm:p-5 rounded-2xl bg-hover border border-transparent hover:border-border transition-all duration-300 hover:shadow-md hover:-translate-y-1">
                                <div class="w-12 h-12 rounded-xl bg-background border border-border text-accent flex items-center justify-center shrink-0 shadow-sm">
                                    <i class="fa-solid fa-tractor text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary-text mb-1">Agricultural</h4>
                                    <p class="text-secondary-text text-sm leading-relaxed">Deep aquifer tapping for heavy irrigation demands.</p>
                                </div>
                            </div>

                            <!-- Sector 4 -->
                            <div class="flex items-start gap-4 p-4 sm:p-5 rounded-2xl bg-hover border border-transparent hover:border-border transition-all duration-300 hover:shadow-md hover:-translate-y-1">
                                <div class="w-12 h-12 rounded-xl bg-background border border-border text-accent flex items-center justify-center shrink-0 shadow-sm">
                                    <i class="fa-solid fa-mountain-sun text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary-text mb-1">Hard Rock</h4>
                                    <p class="text-secondary-text text-sm leading-relaxed">Pneumatic DTH drilling for impenetrable surfaces.</p>
                                </div>
                            </div>
                            
                        </div>
                    </div>

                    <div class="lg:col-span-2 space-y-4">"""

content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open("areas.html", "w", encoding="utf-8") as f:
    f.write(content)

