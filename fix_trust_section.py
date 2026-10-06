import re

with open("quote.html", "r", encoding="utf-8") as f:
    content = f.read()

# Using regex to find the entire SECTION 4
pattern = r'(<!-- ═══════ SECTION 4: TRUST \(WHY QUOTE WITH US\) ═══════ -->\s*<section class="section-padding bg-hover">).*?(?=<!-- ═══════ SECTION 5:)'

new_section = '''<!-- ═══════ SECTION 4: TRUST (WHY QUOTE WITH US) ═══════ -->
        <section class="py-20 sm:py-28 relative overflow-hidden bg-[#0f172a] text-white border-t border-b border-blue-900/30">
            <!-- Decorative background elements -->
            <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
                <div class="absolute -top-[20%] -left-[10%] w-[50%] h-[50%] rounded-full bg-blue-600/10 blur-[120px]"></div>
                <div class="absolute -bottom-[20%] -right-[10%] w-[50%] h-[50%] rounded-full bg-cyan-500/10 blur-[120px]"></div>
                <!-- subtle grid overlay -->
                <div class="absolute inset-0 opacity-[0.03]" style="background-image: linear-gradient(to right, #ffffff 1px, transparent 1px), linear-gradient(to bottom, #ffffff 1px, transparent 1px); background-size: 40px 40px;"></div>
            </div>

            <div class="relative z-10 max-w-7xl mx-auto px-5 sm:px-8 lg:px-12">
                <div class="text-center max-w-3xl mx-auto mb-16 sm:mb-20">
                    <span class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-500/10 border border-blue-500/20 text-cyan-400 font-bold text-xs tracking-widest uppercase mb-6">
                        <i class="fa-solid fa-scale-balanced"></i> The Aquadrill Promise
                    </span>
                    <h2 class="text-4xl sm:text-5xl md:text-6xl font-bold leading-tight mb-6" style="font-family: 'Playfair Display', serif;">
                        A quote you can <br><span class="italic text-cyan-400">actually trust.</span>
                    </h2>
                    <p class="text-blue-100/70 text-lg sm:text-xl leading-relaxed">
                        We don't inflate. We don't hide charges. We give you the real cost of a real solution — and stand behind it.
                    </p>
                </div>

                <!-- Bento Box Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    
                    <!-- Card 1 -->
                    <div class="group bg-slate-800/50 border border-slate-700/50 rounded-3xl p-8 hover:bg-slate-800 transition-all duration-300 relative overflow-hidden backdrop-blur-sm">
                        <div class="w-14 h-14 rounded-2xl bg-blue-500/20 border border-blue-500/30 flex items-center justify-center mb-6 transform group-hover:scale-110 group-hover:bg-blue-500 transition-all">
                            <i class="fa-solid fa-shield-halved text-blue-400 group-hover:text-white text-xl transition-colors"></i>
                        </div>
                        <h3 class="text-xl font-bold mb-3 text-white">No Hidden Charges</h3>
                        <p class="text-slate-400 text-sm leading-relaxed">Every line item, clearly written. Nothing appears mid-project.</p>
                    </div>

                    <!-- Card 2 -->
                    <div class="group bg-slate-800/50 border border-slate-700/50 rounded-3xl p-8 hover:bg-slate-800 transition-all duration-300 relative overflow-hidden backdrop-blur-sm lg:translate-y-8">
                        <div class="w-14 h-14 rounded-2xl bg-cyan-500/20 border border-cyan-500/30 flex items-center justify-center mb-6 transform group-hover:scale-110 group-hover:bg-cyan-500 transition-all">
                            <i class="fa-solid fa-clock text-cyan-400 group-hover:text-white text-xl transition-colors"></i>
                        </div>
                        <h3 class="text-xl font-bold mb-3 text-white">24-Hour Turnaround</h3>
                        <p class="text-slate-400 text-sm leading-relaxed">We call within a day and send your written quote within 24 hours after the site visit.</p>
                    </div>

                    <!-- Card 3 -->
                    <div class="group bg-slate-800/50 border border-slate-700/50 rounded-3xl p-8 hover:bg-slate-800 transition-all duration-300 relative overflow-hidden backdrop-blur-sm">
                        <div class="w-14 h-14 rounded-2xl bg-indigo-500/20 border border-indigo-500/30 flex items-center justify-center mb-6 transform group-hover:scale-110 group-hover:bg-indigo-500 transition-all">
                            <i class="fa-solid fa-handshake text-indigo-400 group-hover:text-white text-xl transition-colors"></i>
                        </div>
                        <h3 class="text-xl font-bold mb-3 text-white">Fixed Pricing</h3>
                        <p class="text-slate-400 text-sm leading-relaxed">Your quote is your price. We don't add costs after work begins.</p>
                    </div>

                    <!-- Card 4 -->
                    <div class="group bg-slate-800/50 border border-slate-700/50 rounded-3xl p-8 hover:bg-slate-800 transition-all duration-300 relative overflow-hidden backdrop-blur-sm lg:translate-y-8">
                        <div class="w-14 h-14 rounded-2xl bg-sky-500/20 border border-sky-500/30 flex items-center justify-center mb-6 transform group-hover:scale-110 group-hover:bg-sky-500 transition-all">
                            <i class="fa-solid fa-user-tie text-sky-400 group-hover:text-white text-xl transition-colors"></i>
                        </div>
                        <h3 class="text-xl font-bold mb-3 text-white">Talk to Engineers</h3>
                        <p class="text-slate-400 text-sm leading-relaxed">No call centres. You speak directly with the team who'll do the work.</p>
                    </div>

                </div>
            </div>
        </section>
        
        '''

if re.search(pattern, content, re.DOTALL):
    new_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    with open("quote.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Success")
else:
    print("Pattern not found")

