import re

# ----- PROCESS.HTML -----
with open("process.html", "r", encoding="utf-8") as f:
    process_content = f.read()

new_process_hero = """        <!-- ═══════ SECTION 1: PROCESS HERO ═══════ -->
        <section class="relative w-full pt-32 pb-20 bg-background overflow-hidden border-b border-border">
            <!-- Subtle background pattern -->
            <div class="absolute inset-0 opacity-[0.03] dark:opacity-[0.02]" style="background-image: radial-gradient(var(--color-primary-text) 1px, transparent 1px); background-size: 32px 32px;"></div>
            
            <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 relative z-10 flex flex-col lg:flex-row items-center justify-between gap-16">
                <div class="w-full lg:w-1/2">
                    <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-accent/10 text-accent text-sm font-bold tracking-wide uppercase mb-6 border border-accent/20">
                        <i class="fa-solid fa-list-check"></i> Our Methodology
                    </div>
                    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-primary-text leading-tight mb-6 tracking-tight">
                        From Dry Land to <br>
                        <span class="text-accent">Flowing Water.</span>
                    </h1>
                    <p class="text-secondary-text text-lg sm:text-xl leading-relaxed mb-8 max-w-lg">
                        We don't guess. We engineer. Discover our transparent, six-step methodology that guarantees water security on every single site.
                    </p>
                </div>
                
                <div class="w-full lg:w-1/2">
                    <div class="grid grid-cols-2 gap-4 sm:gap-6">
                        <div class="bg-hover border border-border p-6 sm:p-8 rounded-3xl flex flex-col items-center justify-center text-center gap-4 shadow-sm hover:border-accent/50 transition-colors">
                            <div class="w-14 h-14 rounded-full bg-background border border-border text-accent flex items-center justify-center text-2xl shadow-sm"><i class="fa-solid fa-map-location-dot"></i></div>
                            <span class="font-bold text-primary-text text-lg">1. Survey</span>
                        </div>
                        <div class="bg-hover border border-border p-6 sm:p-8 rounded-3xl flex flex-col items-center justify-center text-center gap-4 shadow-sm hover:border-accent/50 transition-colors transform translate-y-6 sm:translate-y-8">
                            <div class="w-14 h-14 rounded-full bg-background border border-border text-accent flex items-center justify-center text-2xl shadow-sm"><i class="fa-solid fa-truck-fast"></i></div>
                            <span class="font-bold text-primary-text text-lg">2. Setup</span>
                        </div>
                        <div class="bg-hover border border-border p-6 sm:p-8 rounded-3xl flex flex-col items-center justify-center text-center gap-4 shadow-sm hover:border-accent/50 transition-colors">
                            <div class="w-14 h-14 rounded-full bg-background border border-border text-accent flex items-center justify-center text-2xl shadow-sm"><i class="fa-solid fa-bore-hole"></i></div>
                            <span class="font-bold text-primary-text text-lg">3. Drill</span>
                        </div>
                        <div class="bg-hover border border-border p-6 sm:p-8 rounded-3xl flex flex-col items-center justify-center text-center gap-4 shadow-sm hover:border-accent/50 transition-colors transform translate-y-6 sm:translate-y-8">
                            <div class="w-14 h-14 rounded-full bg-background border border-border text-accent flex items-center justify-center text-2xl shadow-sm"><i class="fa-solid fa-faucet-drip"></i></div>
                            <span class="font-bold text-primary-text text-lg">4. Pump</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

process_content = re.sub(r'<!-- ═══════ SECTION 1: PROCESS HERO ═══════ -->.*?(?=<!-- ═══════ SECTION 2:)', new_process_hero, process_content, flags=re.DOTALL)
with open("process.html", "w", encoding="utf-8") as f:
    f.write(process_content)


# ----- AREAS.HTML -----
with open("areas.html", "r", encoding="utf-8") as f:
    areas_content = f.read()

new_areas_hero = """        <!-- ═══════ SECTION 1: AREAS HERO ═══════ -->
        <section class="relative w-full pt-32 pb-24 bg-hover overflow-hidden border-b border-border">
            <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 relative z-10 text-center">
                <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-background text-primary-text text-sm font-bold tracking-wide uppercase mb-8 shadow-sm border border-border">
                    <i class="fa-solid fa-earth-asia text-accent"></i> Coverage Zone
                </div>
                
                <h1 class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-black text-primary-text leading-tight mb-8 tracking-tight">
                    Drilling Across <br class="hidden sm:block"> The <span class="text-accent">Entire Region.</span>
                </h1>
                
                <p class="text-secondary-text text-lg sm:text-xl leading-relaxed max-w-2xl mx-auto mb-16">
                    From dense metropolitan cities to remote agricultural farms, our heavy-duty rigs and expert teams cover over 45 districts. Wherever you are, we can deploy.
                </p>
                
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 max-w-4xl mx-auto">
                    <div class="bg-background rounded-3xl p-8 border border-border shadow-sm transform transition hover:-translate-y-1 hover:shadow-md">
                        <div class="text-5xl font-extrabold text-accent mb-3">45+</div>
                        <div class="text-secondary-text font-bold uppercase tracking-widest text-xs">Districts Covered</div>
                    </div>
                    <div class="bg-background rounded-3xl p-8 border border-border shadow-sm transform transition hover:-translate-y-1 hover:shadow-md">
                        <div class="text-5xl font-extrabold text-accent mb-3">15</div>
                        <div class="text-secondary-text font-bold uppercase tracking-widest text-xs">Active Rigs</div>
                    </div>
                    <div class="bg-background rounded-3xl p-8 border border-border shadow-sm transform transition hover:-translate-y-1 hover:shadow-md">
                        <div class="text-5xl font-extrabold text-accent mb-3">24/7</div>
                        <div class="text-secondary-text font-bold uppercase tracking-widest text-xs">Deployment Ready</div>
                    </div>
                </div>
            </div>
        </section>"""

areas_content = re.sub(r'<!-- ═══════ SECTION 1: AREAS HERO ═══════ -->.*?(?=<!-- ═══════ SECTION 2:)', new_areas_hero, areas_content, flags=re.DOTALL)
with open("areas.html", "w", encoding="utf-8") as f:
    f.write(areas_content)

