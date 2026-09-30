import re

with open("areas.html", "r", encoding="utf-8") as f:
    areas_content = f.read()

new_areas_hero = """        <!-- ═══════ SECTION 1: AREAS HERO ═══════ -->
        <section class="hero-areas relative w-full pt-32 pb-24 overflow-hidden border-b border-border">
            <!-- Glassmorphic overlay for extreme legibility -->
            <div class="absolute inset-0 bg-black/60 backdrop-blur-[2px]"></div>
            
            <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 relative z-10 text-center">
                <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-900/50 text-blue-300 text-sm font-bold tracking-wide uppercase mb-8 shadow-sm border border-blue-500/30 backdrop-blur-md">
                    <i class="fa-solid fa-earth-asia"></i> Coverage Zone
                </div>
                
                <h1 class="text-4xl sm:text-5xl lg:text-7xl font-black text-white leading-tight mb-8 tracking-tight drop-shadow-lg">
                    Drilling Across <br class="hidden sm:block"> The <span class="text-blue-400">Entire Region.</span>
                </h1>
                
                <p class="text-blue-50 text-lg sm:text-xl leading-relaxed max-w-2xl mx-auto mb-16 drop-shadow-md">
                    From dense metropolitan cities to remote agricultural farms, our heavy-duty rigs and expert teams cover over 45 districts. Wherever you are, we can deploy.
                </p>
                
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 max-w-4xl mx-auto">
                    <div class="bg-black/40 backdrop-blur-xl rounded-3xl p-8 border border-white/10 shadow-2xl transform transition hover:-translate-y-1 hover:border-blue-500/50">
                        <div class="text-5xl font-extrabold text-blue-400 mb-3 drop-shadow">45+</div>
                        <div class="text-blue-100 font-bold uppercase tracking-widest text-xs">Districts Covered</div>
                    </div>
                    <div class="bg-black/40 backdrop-blur-xl rounded-3xl p-8 border border-white/10 shadow-2xl transform transition hover:-translate-y-1 hover:border-blue-500/50">
                        <div class="text-5xl font-extrabold text-blue-400 mb-3 drop-shadow">15</div>
                        <div class="text-blue-100 font-bold uppercase tracking-widest text-xs">Active Rigs</div>
                    </div>
                    <div class="bg-black/40 backdrop-blur-xl rounded-3xl p-8 border border-white/10 shadow-2xl transform transition hover:-translate-y-1 hover:border-blue-500/50">
                        <div class="text-5xl font-extrabold text-blue-400 mb-3 drop-shadow">24/7</div>
                        <div class="text-blue-100 font-bold uppercase tracking-widest text-xs">Deployment Ready</div>
                    </div>
                </div>
            </div>
        </section>"""

areas_content = re.sub(r'<!-- ═══════ SECTION 1: AREAS HERO ═══════ -->.*?(?=<!-- ═══════ SECTION 2:)', new_areas_hero, areas_content, flags=re.DOTALL)
with open("areas.html", "w", encoding="utf-8") as f:
    f.write(areas_content)

