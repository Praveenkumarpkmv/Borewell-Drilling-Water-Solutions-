import re

with open("about.html", "r", encoding="utf-8") as f:
    content = f.read()

new_cta = """        <!-- ═══════ SECTION 6: CTA ═══════ -->
        <section class="py-24 bg-background relative overflow-hidden">
            <!-- Wavy Background Shape -->
            <div class="absolute top-0 left-0 w-full h-full overflow-hidden z-0">
                <svg class="absolute w-full h-full text-accent-light/50" preserveAspectRatio="none" viewBox="0 0 1440 320" style="min-width: 100vw; min-height: 100vh;">
                    <path fill="currentColor" fill-opacity="1" d="M0,192L48,197.3C96,203,192,213,288,229.3C384,245,480,267,576,250.7C672,235,768,181,864,160C960,139,1056,149,1152,165.3C1248,181,1344,203,1392,213.3L1440,224L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
                </svg>
            </div>

            <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 relative z-10">
                <div class="bg-accent rounded-[3rem] p-8 md:p-16 lg:p-20 relative overflow-hidden shadow-2xl shadow-accent/20 border-4 border-accent-light/20">
                    
                    <!-- Decorative Background Circles -->
                    <div class="absolute -top-24 -right-24 w-96 h-96 bg-blue-500 rounded-full opacity-60 mix-blend-screen filter blur-3xl pointer-events-none"></div>
                    <div class="absolute -bottom-24 -left-24 w-80 h-80 bg-cyan-400 rounded-full opacity-40 mix-blend-screen filter blur-3xl pointer-events-none"></div>
                    
                    <div class="flex flex-col lg:flex-row items-center justify-between gap-12 relative z-10">
                        
                        <!-- Left Content -->
                        <div class="w-full lg:w-3/5 text-left text-white">
                            <h2 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold mb-6 leading-tight">
                                Ready to Work With Us?
                            </h2>
                            <p class="text-blue-50 text-lg sm:text-xl leading-relaxed mb-10 max-w-xl">
                                Join hundreds of satisfied property owners. Whether it's a single residential borewell or a large industrial water system, we deliver excellence on every site.
                            </p>
                            
                            <ul class="flex flex-col sm:flex-row gap-6 font-medium">
                                <li class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-full bg-white/20 flex items-center justify-center backdrop-blur-md shadow-inner text-xl">
                                        <i class="fa-solid fa-droplet text-blue-100"></i>
                                    </div>
                                    Guaranteed Water
                                </li>
                                <li class="flex items-center gap-3">
                                    <div class="w-12 h-12 rounded-full bg-white/20 flex items-center justify-center backdrop-blur-md shadow-inner text-xl">
                                        <i class="fa-solid fa-stopwatch text-blue-100"></i>
                                    </div>
                                    Fast Execution
                                </li>
                            </ul>
                        </div>
                        
                        <!-- Right CTA Box -->
                        <div class="w-full lg:w-2/5">
                            <div class="bg-background rounded-3xl p-8 sm:p-10 shadow-[0_20px_50px_rgba(0,0,0,0.15)] text-center relative transform lg:scale-105">
                                <div class="absolute -top-6 left-1/2 -translate-x-1/2 bg-gradient-to-r from-blue-500 to-cyan-500 text-white px-6 py-2 rounded-full font-bold text-sm shadow-lg whitespace-nowrap">
                                    Free Assessment
                                </div>
                                
                                <h3 class="text-2xl font-bold text-primary-text mb-3 mt-4">Start Your Project</h3>
                                <p class="text-secondary-text mb-8">Get a free site assessment and a transparent, no-obligation quote today.</p>
                                
                                <a href="contact.html" class="block w-full bg-accent hover:bg-accent-hover text-white font-bold py-4 px-8 rounded-xl transition-colors mb-4 shadow-lg shadow-accent/30 text-lg">
                                    Book Consultation
                                </a>
                                <a href="tel:+18005550199" class="block w-full bg-hover hover:bg-border text-primary-text font-bold py-4 px-8 rounded-xl border-2 border-border transition-colors text-lg flex items-center justify-center">
                                    <i class="fa-solid fa-phone text-accent mr-3"></i> +1 (800) 555-0199
                                </a>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </section>"""

pattern = r'<!-- ═══════ SECTION 6: CTA ═══════ -->.*?</section>'
new_content = re.sub(pattern, new_cta, content, flags=re.DOTALL)

with open("about.html", "w", encoding="utf-8") as f:
    f.write(new_content)
