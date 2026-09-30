import re

# Update process.html
with open("process.html", "r", encoding="utf-8") as f:
    process_content = f.read()

new_process_cta = """        <!-- ═══════ SECTION 6: CTA ═══════ -->
        <section class="py-20 relative overflow-hidden bg-hover border-y border-border">
            <!-- Diagonal slash background -->
            <div class="absolute inset-0 z-0">
                <div class="absolute inset-y-0 left-0 w-full lg:w-2/3 bg-accent [clip-path:polygon(0_0,100%_0,85%_100%,0_100%)] hidden lg:block"></div>
                <div class="absolute inset-0 bg-accent lg:hidden"></div>
            </div>

            <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-12 relative z-10">
                <div class="flex flex-col lg:flex-row items-center gap-16">
                    
                    <!-- Left: Text -->
                    <div class="w-full lg:w-3/5 text-white">
                        <div class="inline-flex items-center gap-3 mb-6 bg-white/10 backdrop-blur-md px-4 py-2 rounded-full border border-white/20">
                            <span class="flex h-3 w-3 relative">
                              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
                              <span class="relative inline-flex rounded-full h-3 w-3 bg-cyan-400"></span>
                            </span>
                            <span class="font-semibold text-sm tracking-wide uppercase text-blue-50">Start Today</span>
                        </div>
                        
                        <h2 class="text-4xl sm:text-5xl lg:text-6xl font-bold mb-6 leading-tight">
                            Ready to Start <br>
                            <span class="text-cyan-300">Step One?</span>
                        </h2>
                        <p class="text-blue-100 text-lg sm:text-xl leading-relaxed mb-10 max-w-lg">
                            Every successful project begins with a free consultation and a detailed site survey. No obligation, no pressure — just honest advice from our certified engineers.
                        </p>
                        
                        <div class="flex flex-col sm:flex-row items-center gap-4">
                            <a href="contact.html" class="bg-white hover:bg-blue-50 text-accent w-full sm:w-auto px-8 py-4 rounded-xl font-bold text-lg shadow-[0_10px_25px_rgba(0,0,0,0.2)] transition-all transform hover:-translate-y-1 flex items-center justify-center gap-3">
                                <i class="fa-solid fa-flag-checkered text-accent"></i> Initiate Project
                            </a>
                        </div>
                    </div>

                    <!-- Right: Info/Cards -->
                    <div class="w-full lg:w-2/5 grid gap-6">
                        <div class="bg-background rounded-2xl p-6 shadow-xl border border-border flex items-start gap-4 transform transition hover:-translate-y-2 hover:shadow-2xl">
                            <div class="w-14 h-14 rounded-full bg-accent-light flex items-center justify-center text-accent shrink-0">
                                <i class="fa-solid fa-map-location-dot text-2xl"></i>
                            </div>
                            <div>
                                <h4 class="text-xl font-bold text-primary-text mb-1">Free Site Survey</h4>
                                <p class="text-secondary-text text-sm">We analyze your terrain and geological data before any commitments.</p>
                            </div>
                        </div>
                        
                        <div class="bg-background rounded-2xl p-6 shadow-xl border border-border flex items-start gap-4 transform transition hover:-translate-y-2 hover:shadow-2xl lg:-ml-12">
                            <div class="w-14 h-14 rounded-full bg-accent-light flex items-center justify-center text-accent shrink-0">
                                <i class="fa-solid fa-file-invoice-dollar text-2xl"></i>
                            </div>
                            <div>
                                <h4 class="text-xl font-bold text-primary-text mb-1">Fixed Quote Guarantee</h4>
                                <p class="text-secondary-text text-sm">Clear, transparent pricing. Absolutely no hidden charges mid-project.</p>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>"""

pattern = r'<!-- ═══════ SECTION 6: CTA ═══════ -->.*?</section>'
process_content = re.sub(pattern, new_process_cta, process_content, flags=re.DOTALL)

with open("process.html", "w", encoding="utf-8") as f:
    f.write(process_content)


# Update contact.html
with open("contact.html", "r", encoding="utf-8") as f:
    contact_content = f.read()

new_contact_cta = """        <!-- ═══════ SECTION 6: CTA ═══════ -->
        <section class="py-24 relative overflow-hidden bg-background">
            <!-- Modern Gradient Mesh Background -->
            <div class="absolute inset-0 opacity-40 dark:opacity-20 pointer-events-none">
                <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-accent/20 rounded-full mix-blend-multiply filter blur-[100px]"></div>
                <div class="absolute bottom-0 left-10 w-[600px] h-[600px] bg-cyan-400/20 rounded-full mix-blend-multiply filter blur-[120px]"></div>
            </div>

            <div class="max-w-6xl mx-auto px-5 sm:px-8 relative z-10">
                <div class="text-center mb-16">
                    <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-accent text-white shadow-xl shadow-accent/40 mb-8 animate-bounce">
                        <i class="fa-solid fa-phone-volume text-3xl"></i>
                    </div>
                    <h2 class="text-4xl sm:text-5xl md:text-6xl font-bold mb-6 text-primary-text leading-tight">
                        Prefer to Talk <span class="text-transparent bg-clip-text bg-gradient-to-r from-accent to-cyan-500">Right Now?</span>
                    </h2>
                    <p class="text-secondary-text text-lg sm:text-xl max-w-2xl mx-auto leading-relaxed">
                        Skip the forms. Give us a ring and speak directly to a certified engineer. No call centers, no wait times — just real answers.
                    </p>
                </div>

                <!-- Dual Action Cards -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                    <!-- Call Card -->
                    <a href="tel:+18005550199" class="group relative bg-background rounded-3xl p-8 border border-border shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden text-center block hover:-translate-y-2">
                        <div class="absolute inset-0 bg-accent-light opacity-0 group-hover:opacity-10 transition-opacity"></div>
                        <div class="relative z-10">
                            <h3 class="text-xl font-bold text-primary-text mb-2 group-hover:text-accent transition-colors">Immediate Support</h3>
                            <div class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-accent tracking-tight my-6 group-hover:scale-105 transition-transform duration-300">
                                +1 (800) 555-0199
                            </div>
                            <p class="text-secondary-text font-medium flex items-center justify-center gap-2">
                                <i class="fa-solid fa-headset text-accent"></i> 24/7 Availability • Real Engineers
                            </p>
                        </div>
                    </a>

                    <!-- Email Card -->
                    <a href="mailto:info@aquadrill.com" class="group relative bg-background rounded-3xl p-8 border border-border shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden text-center block hover:-translate-y-2">
                        <div class="absolute inset-0 bg-cyan-50 dark:bg-cyan-900/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                        <div class="relative z-10">
                            <h3 class="text-xl font-bold text-primary-text mb-2 group-hover:text-cyan-500 transition-colors">Detailed Inquiries</h3>
                            <div class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-primary-text tracking-tight my-6 group-hover:scale-105 transition-transform duration-300">
                                info@aquadrill.com
                            </div>
                            <p class="text-secondary-text font-medium flex items-center justify-center gap-2">
                                <i class="fa-solid fa-envelope text-cyan-500"></i> Average response time: 2 hours
                            </p>
                        </div>
                    </a>
                </div>
            </div>
        </section>"""

contact_content = re.sub(pattern, new_contact_cta, contact_content, flags=re.DOTALL)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(contact_content)
