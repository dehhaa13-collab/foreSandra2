import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

metrics_html = """
        <section id="slide-3" class="slide slide--metrics">
            <div class="slide__inner">
                <h2 class="section-title split-text">10 основних фінансових показників по кожному сегменту/бізнес-одиниці</h2>

                <div class="metrics-grid">
                    <!-- ПРИБИЛЬНІСТЬ -->
                    <div class="metric-category reveal-up">
                        <h3 class="metric-category__title">ПРИБУТКОВІСТЬ</h3>
                        <div class="metric-card">
                            <span class="metric-card__number">1</span>
                            <span class="metric-card__name split-letters">CONTRIBUTION MARGIN</span>
                            <span class="metric-card__desc">(МАРЖИНАЛЬНІСТЬ)</span>
                        </div>
                        <div class="metric-card">
                            <span class="metric-card__number">2</span>
                            <span class="metric-card__name split-letters">EBITDA / NET PROFIT</span>
                            <span class="metric-card__desc">(EBITDA / ЧИСТИЙ ПРИБУТОК)</span>
                        </div>
                    </div>

                    <!-- ГРОШІ -->
                    <div class="metric-category reveal-up">
                        <h3 class="metric-category__title">ГРОШІ</h3>
                        <div class="metric-card">
                            <span class="metric-card__number">3</span>
                            <span class="metric-card__name split-letters">NET CASH FLOW</span>
                            <span class="metric-card__desc">(ЧИСТИЙ ГРОШОВИЙ ПОТІК)</span>
                        </div>
                        <div class="metric-card">
                            <span class="metric-card__number">4</span>
                            <span class="metric-card__name split-letters">CASH CONVERSION CYCLE</span>
                            <span class="metric-card__desc">(ЦИКЛ ОБІГУ ГРОШОВИХ КОШТІВ)</span>
                        </div>
                        <div class="metric-card">
                            <span class="metric-card__number">5</span>
                            <span class="metric-card__name split-letters">QUICK RATIO</span>
                            <span class="metric-card__desc">(ШВИДКА ЛІКВІДНІСТЬ)</span>
                        </div>
                    </div>

                    <!-- СИСТЕМА РОСТУ -->
                    <div class="metric-category reveal-up">
                        <h3 class="metric-category__title">СИСТЕМА ЗРОСТАННЯ</h3>
                        <div class="metric-card">
                            <span class="metric-card__number">6</span>
                            <span class="metric-card__name split-letters">CAC</span>
                            <span class="metric-card__desc">(ВАРТІСТЬ ЗАЛУЧЕННЯ КЛІЄНТА)</span>
                        </div>
                    </div>

                    <!-- ЕФЕКТИВНІСТЬ -->
                    <div class="metric-category reveal-up">
                        <h3 class="metric-category__title">ЕФЕКТИВНІСТЬ</h3>
                        <div class="metric-card">
                            <span class="metric-card__number">7</span>
                            <span class="metric-card__name split-letters">ROMI</span>
                            <span class="metric-card__desc">(ЕФЕКТИВНІСТЬ МАРКЕТИНГОВИХ ІНВЕСТИЦІЙ)</span>
                        </div>
                        <div class="metric-card">
                            <span class="metric-card__number">8</span>
                            <span class="metric-card__name split-letters">UNIT ECONOMICS</span>
                            <span class="metric-card__desc">(ЮНІТ-ЕКОНОМІКА)</span>
                        </div>
                        <div class="metric-card">
                            <span class="metric-card__number">9</span>
                            <span class="metric-card__name split-letters">ROE</span>
                            <span class="metric-card__desc">(РЕНТАБЕЛЬНІСТЬ ВЛАСНОГО КАПІТАЛУ)</span>
                        </div>
                    </div>

                    <!-- ФІНАНСОВА СТІЙКІСТЬ -->
                    <div class="metric-category reveal-up">
                        <h3 class="metric-category__title">ФІНАНСОВА СТІЙКІСТЬ</h3>
                        <div class="metric-card">
                            <span class="metric-card__number">10</span>
                            <span class="metric-card__name split-letters">SAFETY MARGIN</span>
                            <span class="metric-card__desc">(ЗАПАС МІЦНОСТІ)</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
html = re.sub(r'<section id="slide-3".*?</section>', metrics_html.strip(), html, flags=re.DOTALL)

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
