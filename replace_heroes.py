import re

# ----- PROCESS.HTML -----
with open("process.html", "r", encoding="utf-8") as f:
    process_content = f.read()

new_process_hero = """        <!-- ═══════ SECTION 1: PROCESS HERO ═══════ -->
        <section class="hero-process relative w-full pt-32 pb-24 flex items-center overflow-hidden bg-slate-900 border-b border-slate-800">
            <!-- Background element -->
            <div class="absolute inset-0 bg-[url('assets/process.avif')] bg-cover bg-center opacity-30 mix-blend-overlay"></div>
            <div class="absolute right-0 top-0 w-1/2 h-full bg-gradient-to-l from-blue-900/40 to-transparent"></div>
            
            <div class="relative z-10 max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 flex flex-col lg:flex-row items-center gap-12">
                <div class="w-full lg:w-3/5 text-white">
                    <div class="inline-flex items-center gap-2 px-3 py-1 mb-6 rounded-md bg-blue-600/20 text-blue-300 text-sm font-bold tracking-wide uppercase border-l-4 border-blue-500">
                        <i class="fa-solid fa-cogs"></i> Proven Methodology
                    </div>
                    <h1 class="text-4xl sm:text-5xl lg:text-7xl font-extrabold leading-tight mb-6 tracking-tight">
                        From Dry Land to<br>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">Flowing Water.</span>
                    </h1>
                    <p class="text-slate-300 text-lg sm:text-xl leading-relaxed max-w-xl mb-10 border-l border-slate-700 pl-6">
                        A transparent, methodical six-step process. This is the exact engineering framework we use to guarantee water security on every single site.
                    </p>
                </div>
                
                <div class="w-full lg:w-2/5 hidden md:block">
                    <!-- Abstract Process Visualization -->
                    <div class="relative w-full aspect-square max-w-md mx-auto">
                        <div class="absolute top-0 right-10 w-32 h-32 bg-blue-500/10 rounded-full border border-blue-500/30 flex items-center justify-center backdrop-blur-md animate-pulse">
                            <i class="fa-solid fa-1 text-4xl text-blue-400/50"></i>
                        </div>
                        <div class="absolute bottom-20 left-0 w-40 h-40 bg-cyan-500/10 rounded-full border border-cyan-500/30 flex items-center justify-center backdrop-blur-md" style="animation: pulse 3s infinite reverse;">
                            <i class="fa-solid fa-2 text-5xl text-cyan-400/50"></i>
                        </div>
                        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-48 h-48 bg-white/5 rounded-full border border-white/10 flex items-center justify-center backdrop-blur-xl shadow-2xl">
                            <i class="fa-solid fa-diagram-project text-6xl text-white"></i>
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
        <section class="relative w-full min-h-[60vh] flex items-end pb-16 pt-32 overflow-hidden">
            <!-- Background Map / Image -->
            <div class="absolute inset-0 bg-slate-800">
                <img src="assets/areas.avif" onerror="this.src='https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=2000&auto=format&fit=crop';" alt="Map Background" class="w-full h-full object-cover opacity-40 mix-blend-luminosity">
                <div class="absolute inset-0 bg-gradient-to-t from-background via-background/80 to-transparent"></div>
            </div>

            <div class="relative z-10 max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 w-full">
                <div class="bg-background/80 dark:bg-slate-900/80 backdrop-blur-xl border border-border p-8 sm:p-12 rounded-3xl shadow-2xl max-w-3xl">
                    <div class="flex items-center gap-3 text-accent font-bold mb-4">
                        <i class="fa-solid fa-location-crosshairs text-xl animate-spin-slow"></i> 
                        <span class="tracking-widest uppercase text-sm">Coverage Zone</span>
                    </div>
                    <h1 class="text-4xl sm:text-5xl md:text-6xl font-black text-primary-text mb-6">
                        Drilling Across The <span class="text-accent underline decoration-4 underline-offset-8">Region.</span>
                    </h1>
                    <p class="text-secondary-text text-lg sm:text-xl leading-relaxed">
                        From dense metropolitan cities to remote agricultural farms, our heavy-duty rigs and expert teams cover over 45 districts. Wherever you are, we can deploy.
                    </p>
                </div>
            </div>
        </section>"""

areas_content = re.sub(r'<!-- ═══════ SECTION 1: AREAS HERO ═══════ -->.*?(?=<!-- ═══════ SECTION 2:)', new_areas_hero, areas_content, flags=re.DOTALL)
with open("areas.html", "w", encoding="utf-8") as f:
    f.write(areas_content)


# ----- CONTACT.HTML -----
with open("contact.html", "r", encoding="utf-8") as f:
    contact_content = f.read()

new_contact_hero = """        <!-- ═══════ SECTION 1: CONTACT HERO ═══════ -->
        <section class="relative w-full pt-32 pb-20 overflow-hidden bg-background">
            <!-- Decorative blobs -->
            <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-accent/5 rounded-full blur-[120px] pointer-events-none translate-x-1/3 -translate-y-1/3"></div>
            
            <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 relative z-10">
                <div class="text-center max-w-3xl mx-auto">
                    <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-accent-light text-accent mb-6 shadow-lg shadow-accent/20">
                        <i class="fa-regular fa-comments text-2xl"></i>
                    </div>
                    <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold text-primary-text mb-6 tracking-tight">
                        Let's Talk About <br class="hidden sm:block"> Your Water Needs.
                    </h1>
                    <p class="text-secondary-text text-lg sm:text-xl leading-relaxed mb-0">
                        Need a site survey? Have questions about our drilling rigs? Want a free quote? We are here to help. Reach out to our certified engineers today.
                    </p>
                </div>
            </div>
        </section>"""

contact_content = re.sub(r'<!-- ═══════ SECTION 1: CONTACT HERO ═══════ -->.*?(?=<!-- ═══════ SECTION 2:)', new_contact_hero, contact_content, flags=re.DOTALL)
with open("contact.html", "w", encoding="utf-8") as f:
    f.write(contact_content)

