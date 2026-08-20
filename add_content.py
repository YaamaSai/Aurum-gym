import re

with open("AURUM_Gym_Website.html", "r", encoding="utf-8") as f:
    content = f.read()

features_addon = """
        <article class="feature-card" role="listitem">
          <div class="feature-icon" aria-hidden="true">⚡</div>
          <h3 class="feature-title">Recovery Zones</h3>
          <p class="feature-desc">Dedicated massage therapy, cryotherapy chambers, and stretching areas for peak muscle recovery.</p>
        </article>
        <article class="feature-card" role="listitem">
          <div class="feature-icon" aria-hidden="true">🌍</div>
          <h3 class="feature-title">Global Access</h3>
          <p class="feature-desc">Members get passport access to partner elite gyms in 50+ major cities worldwide.</p>
        </article>
"""

classes_addon = """
        <article class="class-card" data-cat="cardio">
          <div class="class-img">
            <img src="https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=600&q=100" alt="Spin class at AURUM" loading="lazy" />
          </div>
          <div class="class-body">
            <p class="class-level">Cardio · Intermediate</p>
            <h3 class="class-name">Endurance Spin</h3>
            <p class="class-trainer">with Coach Priya Reddy</p>
            <div class="class-meta">
              <span>🕒 45 Min</span>
              <span>🔥 600 kcal</span>
              <span>🗓 Tue / Thu / Sat</span>
            </div>
          </div>
        </article>
        <article class="class-card" data-cat="mind">
          <div class="class-img">
            <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600&q=100" alt="Advanced Yoga class" loading="lazy" />
          </div>
          <div class="class-body">
            <p class="class-level">Mind & Body · All Levels</p>
            <h3 class="class-name">Vinyasa Flow</h3>
            <p class="class-trainer">with Coach Meera Nair</p>
            <div class="class-meta">
              <span>🕒 60 Min</span>
              <span>🔥 300 kcal</span>
              <span>🗓 Mon / Wed</span>
            </div>
          </div>
        </article>
"""

trainers_addon = """
        <article class="trainer-card">
          <div class="trainer-img">
            <img src="https://images.unsplash.com/photo-1599058945522-28d584b6f0ff?w=400&q=100" alt="David Lee - Endurance Coach" loading="lazy" />
          </div>
          <div class="trainer-body">
            <h3 class="trainer-name">David Lee</h3>
            <p class="trainer-spec">Endurance & Marathon</p>
            <p class="trainer-desc">Multiple Ironman finisher. Expert in aerobic conditioning and race preparation.</p>
            <div class="trainer-socials" aria-label="Social links for David Lee">
              <a href="#" class="social-btn" aria-label="Instagram">📸</a>
              <a href="#" class="social-btn" aria-label="LinkedIn">💼</a>
            </div>
          </div>
        </article>
        <article class="trainer-card">
          <div class="trainer-img">
            <img src="https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?w=400&q=100" alt="Sarah Jenkins - Mobility" loading="lazy" />
          </div>
          <div class="trainer-body">
            <h3 class="trainer-name">Sarah Jenkins</h3>
            <p class="trainer-spec">Mobility & Rehab</p>
            <p class="trainer-desc">Doctor of Physical Therapy. Focuses on movement quality and injury prevention.</p>
            <div class="trainer-socials" aria-label="Social links for Sarah Jenkins">
              <a href="#" class="social-btn" aria-label="Instagram">📸</a>
              <a href="#" class="social-btn" aria-label="LinkedIn">💼</a>
            </div>
          </div>
        </article>
"""

testimonials_addon = """
        <article class="testimonial-card">
          <div class="testimonial-stars" aria-label="5 stars">★★★★★</div>
          <blockquote class="testimonial-text">"I joined for the equipment, but I stayed for the community. The trainers truly care about your well-being, both physically and mentally."</blockquote>
          <div class="testimonial-author">
            <div class="author-avatar" aria-hidden="true">JD</div>
            <div>
              <div class="author-name">John D'Souza</div>
              <div class="author-since">Member since 2023</div>
            </div>
          </div>
        </article>
        <article class="testimonial-card">
          <div class="testimonial-stars" aria-label="5 stars">★★★★★</div>
          <blockquote class="testimonial-text">"The yoga classes here are transcendent. It's the perfect balance to my intense strength training regimen."</blockquote>
          <div class="testimonial-author">
            <div class="author-avatar" aria-hidden="true">KP</div>
            <div>
              <div class="author-name">Kiran Patel</div>
              <div class="author-since">Gold Member · 1 year</div>
            </div>
          </div>
        </article>
"""

content = re.sub(r'(<div class="features-grid" role="list">.*?)(      </div>)', r'\1' + features_addon.strip('\n') + r'\n\2', content, flags=re.DOTALL)
content = re.sub(r'(<div class="classes-grid" id="classesGrid">.*?)(      </div>)', r'\1' + classes_addon.strip('\n') + r'\n\2', content, flags=re.DOTALL)
content = re.sub(r'(<div class="trainers-grid">.*?)(      </div>)', r'\1' + trainers_addon.strip('\n') + r'\n\2', content, flags=re.DOTALL)
content = re.sub(r'(<div class="testimonials-grid">.*?)(      </div>)', r'\1' + testimonials_addon.strip('\n') + r'\n\2', content, flags=re.DOTALL)

with open("AURUM_Gym_Website.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done replacing.")
