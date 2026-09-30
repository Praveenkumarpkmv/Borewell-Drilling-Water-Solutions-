import re

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

new_cta = """        <!-- ═══════ SECTION 7: CTA ═══════ -->
        <section class="section-padding bg-hover relative overflow-hidden">
            <!-- Decorative Elements -->
            <div class="absolute top-0 right-0 w-96 h-96 bg-accent/5 rounded-full blur-3xl translate-x-1/2 -translate-y-1/2"></div>
            <div class="absolute bottom-0 left-0 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl -translate-x-1/2 translate-y-1/2"></div>
            
            <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 relative z-10">
                <div class="bg-background border border-border shadow-2xl rounded-3xl overflow-hidden flex flex-col lg:flex-row items-center">
                    
                    <!-- Left: Content -->
                    <div class="w-full lg:w-3/5 p-8 sm:p-12 lg:p-16">
                        <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-accent-light text-accent text-sm font-bold tracking-wide uppercase mb-6 border border-accent/20">
                            <i class="fa-solid fa-headset"></i> Expert Advice
                        </div>
                        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-bold mb-6 text-primary-text leading-tight">
                            Not Sure Which <span class="text-transparent bg-clip-text bg-gradient-to-r from-accent to-blue-400">Service</span> You Need?
                        </h2>
                        <p class="text-secondary-text text-base sm:text-lg mb-8 leading-relaxed max-w-xl">
                            Tell us about your water requirement and we'll recommend the exact combination of services you need — backed by a clear, no-obligation quote and our expertise.
                        </p>
                        
                        <div class="flex flex-col sm:flex-row items-center gap-4 mb-8">
                            <a href="contact.html" class="btn-primary w-full sm:w-auto px-8 py-4 rounded-xl font-bold text-base flex items-center justify-center gap-2">
                                <i class="fa-solid fa-calendar-check"></i> Book Free Consultation
                            </a>
                            <a href="tel:+18005550199" class="btn-outline w-full sm:w-auto px-8 py-4 rounded-xl font-bold text-base flex items-center justify-center gap-2 bg-background">
                                <i class="fa-solid fa-phone"></i> +1 (800) 555-0199
                            </a>
                        </div>
                        
                        <div class="flex flex-wrap items-center gap-x-6 gap-y-3 text-sm font-medium text-secondary-text">
                            <span class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-accent"></i> Free Site Assessment</span>
                            <span class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-accent"></i> Transparent Pricing</span>
                            <span class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-accent"></i> 24/7 Support</span>
                        </div>
                    </div>

                    <!-- Right: Image/Visual -->
                    <div class="w-full lg:w-2/5 min-h-[300px] lg:h-auto self-stretch relative bg-slate-100 hidden sm:block">
                        <img src="assets/services.avif" onerror="this.src='https://images.unsplash.com/photo-1541888087652-32692298e727?q=80&w=1000&auto=format&fit=crop';" alt="Expert Consultation" class="absolute inset-0 w-full h-full object-cover">
                        <!-- Overlay gradient -->
                        <div class="absolute inset-0 bg-gradient-to-t lg:bg-gradient-to-r from-background via-transparent to-transparent"></div>
                        
                        <!-- Floating Badge -->
                        <div class="absolute bottom-6 right-6 bg-background rounded-xl p-4 shadow-xl border border-border flex items-center gap-4 float-anim">
                            <div class="w-12 h-12 rounded-full bg-accent-light text-accent flex items-center justify-center text-xl">
                                <i class="fa-solid fa-star"></i>
                            </div>
                            <div>
                                <div class="font-bold text-primary-text">4.9/5 Rating</div>
                                <div class="text-xs text-secondary-text">From 500+ Clients</div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>"""

pattern = r'<!-- ═══════ SECTION 7: CTA ═══════ -->.*?</section>'
new_content = re.sub(pattern, new_cta, content, flags=re.DOTALL)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(new_content)
