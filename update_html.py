import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero section
hero_html = """
        <section id="slide-1" class="slide slide--hero">
            <div class="slide__inner">
                <h1 class="hero__title split-text">Комплексна упаковка</h1>
                <h2 class="hero__subtitle reveal-up">активів та бізнес-одиниць:<br>правове оформлення,<br>бухгалтерський та управлінський облік</h2>
                <p class="hero__description reveal-up">Прозора структура, захист і капіталізація вашого бізнесу для подальшого масштабування або продажу.</p>
            </div>
        </section>
"""
html = re.sub(r'<section id="slide-1".*?</section>', hero_html.strip(), html, flags=re.DOTALL)

# 2. Update Overview cards (Slide 2)
cards_html = """
        <section id="slide-2" class="slide slide--overview">
            <div class="slide__inner">
                <div class="section-header reveal-up">
                    <h2 class="section-title">Чотири напрямки упаковки активів</h2>
                    <p class="section-desc">Щоб ваш бізнес перетворився на структуровану екосистему, робота ведеться паралельно в чотирьох ключових блоках:</p>
                </div>
                <div class="cards-grid">
                    <article class="card card--glass reveal-up">
                        <div class="card__icon">⚖️</div>
                        <h2 class="card__title">Юридичний блок</h2>
                        <p class="card__text">правове оформлення структури, реєстрація прав/активів, підготовка договірної бази</p>
                    </article>
                    <article class="card card--glass reveal-up">
                        <div class="card__icon">📊</div>
                        <h2 class="card__title">Бухгалтерський блок</h2>
                        <p class="card__text">постановка активів на баланс, визначення амортизації, мінімізація податкових ризиків</p>
                    </article>
                    <article class="card card--glass reveal-up">
                        <div class="card__icon">📈</div>
                        <h2 class="card__title">Управлінський блок</h2>
                        <p class="card__text">відображення активів в управлінському балансі для оцінки реальної вартості бізнес-одиниці</p>
                    </article>
                    <article class="card card--glass reveal-up">
                        <div class="card__icon">💰</div>
                        <h2 class="card__title">Оцінка та капіталізація</h2>
                        <p class="card__text">оцінка ринкової вартості, монетизація цифрових активів, інвестиційна модель</p>
                    </article>
                </div>
            </div>
        </section>
"""
html = re.sub(r'<section id="slide-2".*?</section>', cards_html.strip(), html, flags=re.DOTALL)

# 3. Update Slide 4: Legal Block
legal_html = """
        <section id="slide-4" class="slide slide--detail">
            <div class="slide__inner">
                <h2 class="section-title split-text">Юридичний блок</h2>

                <div class="detail-block detail-block--single reveal-up">
                    <p class="detail-block__desc" style="font-size: var(--text-body); color: var(--color-text-muted); margin-bottom: var(--space-md); line-height: 1.6; border-left: 2px solid var(--color-accent); padding-left: var(--space-md);">
                        Оскільки дочірні бізнес-одиниці є підприємцями ФОП, то сам ФОП як юридична форма зазвичай не продається як окремий актив, оскільки ФОП не відокремлений від особи власника. Оскільки ФОП продати неможливо, зазвичай продаються активи бізнесу: обладнання та техніка, товари на складі, СRM-система, база підписників, клієнтська база, сайти, домени, рекламні кабінети, торговельні марки, авторські права, навчальні матеріали, акаунти в соцмережах, патенти, банківські депозити, акції, дебіторська заборгованість тощо.
                    </p>
                    <ul class="detail-list">
                        <li class="detail-list__item stagger">Надати повний перелік всіх наявних активів компанії/бізнес-одиниці.</li>
                        <li class="detail-list__item stagger">Зібрати та систематизувати первинні документи, що підтверджують право власності або користування, зокрема: договори на розробку сайтів, договори підряду/надання послуг, акти прийому-передачі, інші підтверджуючі документи.</li>
                        <li class="detail-list__item stagger">Провести юридичний аналіз належності кожного активу.</li>
                        <li class="detail-list__item stagger">Встановити фактичних та юридичних правовласників.</li>
                        <li class="detail-list__item stagger">Визначити ризики відсутності або неповного оформлення прав.</li>
                        <li class="detail-list__item stagger">Забезпечити належне оформлення переходу прав інтелектуальної власності (за необхідності – з актами передачі).</li>
                        <li class="detail-list__item stagger">Уніфікувати структуру договорів для всіх типів цифрових активів (сайти, домени, контент, бази даних тощо).</li>
                        <li class="detail-list__item stagger">Розробити дорожню карту капіталізації активів з детальним описом етапів, термінів та механізмів реалізації.</li>
                        <li class="detail-list__item stagger">Залучення зовнішніх оцінювачів бізнесу та активів.</li>
                    </ul>
                </div>
            </div>
        </section>
"""
html = re.sub(r'<section id="slide-4".*?</section>', legal_html.strip(), html, flags=re.DOTALL)

# 4. Update Slide 5: Accounting Block
acc_html = """
        <section id="slide-5" class="slide slide--detail">
            <div class="slide__inner">
                <h2 class="section-title split-text">Бухгалтерський блок</h2>

                <div class="detail-block detail-block--single reveal-up">
                    <ul class="detail-list">
                        <li class="detail-list__item stagger">Первинні документи: договори, акти виконаних робіт, акти прийому-передачі.</li>
                        <li class="detail-list__item stagger">Реєстри (облікові таблиці активів) ОЗ, НМА, ФІ, ДЗ.</li>
                        <li class="detail-list__item stagger">Бухгалтерські звіти (ключові форми): Баланс ф-1, Звіт про фінансові результати ф-2 (прибуток/збиток), Cash Flow, Звіт про зміни в капіталі.</li>
                        <li class="detail-list__item stagger">Облік амортизації.</li>
                    </ul>
                </div>
            </div>
        </section>
"""
html = re.sub(r'<section id="slide-5".*?</section>', acc_html.strip(), html, flags=re.DOTALL)

# 5. Update Slide 6: Management Block
mgmt_html = """
        <section id="slide-6" class="slide slide--detail">
            <div class="slide__inner">
                <h2 class="section-title split-text">Управлінський блок</h2>

                <div class="detail-block detail-block--single reveal-up">
                    <ul class="detail-list">
                        <li class="detail-list__item stagger">Додати в QUINCEFIN актуальні сегменти бізнес-одиниць.</li>
                        <li class="detail-list__item stagger">Розподілити витрати за сегментами за 2026 рік.</li>
                        <li class="detail-list__item stagger">Налаштувати логіку та послідовність впровадження обліку PnL, Cash Flow, Balance Sheet у всіх сегментах бізнесу.</li>
                    </ul>
                </div>
            </div>
        </section>
"""
html = re.sub(r'<section id="slide-6".*?</section>', mgmt_html.strip(), html, flags=re.DOTALL)

# 6. Update Slide 8 -> Slide 7 (Results) - wait, slide-7 is Evaluation, slide-8 is Results.
# Let's check existing slide-7:
eval_html = """
        <section id="slide-7" class="slide slide--detail slide--evaluation">
            <div class="slide__inner">
                <h2 class="section-title split-text">Оцінка та капіталізація активів</h2>
                <div class="detail-block detail-block--single reveal-up">
                    <ul class="detail-list">
                        <li class="detail-list__item stagger">залучення незалежних оцінювачів;</li>
                        <li class="detail-list__item stagger">оцінка ринкової вартості активів;</li>
                        <li class="detail-list__item stagger">визначення можливості капіталізації активів;</li>
                        <li class="detail-list__item stagger">аналіз потенціалу монетизації нематеріальних та цифрових активів;</li>
                        <li class="detail-list__item stagger">підготовка активів до інвестиційних та M&A-процесів;</li>
                        <li class="detail-list__item stagger">підготовка інвестиційної моделі бізнесу;</li>
                        <li class="detail-list__item stagger">формування рекомендацій щодо підвищення вартості бізнесу;</li>
                        <li class="detail-list__item stagger">розробка сценаріїв реструктуризації та відчуження активів.</li>
                    </ul>
                </div>
            </div>
        </section>
"""
html = re.sub(r'<section id="slide-7".*?</section>', eval_html.strip(), html, flags=re.DOTALL)

# Let's replace Slide-8 Results block text to Ukrainian if any is Russian
# Wait, existing slide-8 was already mostly Ukrainian, but let's ensure it's exact.
res_html = """
        <section id="slide-8" class="slide slide--results">
            <div class="slide__inner">
                <div class="results-block reveal-up">
                    <h2 class="section-title split-text">Результат проєкту</h2>
                    <ul class="results-list">
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> реєстр активів;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> матриця прав власності;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> реєстр об'єктів інтелектуальної власності;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> карта юридичних, корпоративних та податкових ризиків;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> юридично оформлена структура володіння активами;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> бухгалтерська та управлінська модель обліку;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> управлінський баланс бізнес-одиниць;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> консолідована фінансова модель групи;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> дорожня карта капіталізації та реструктуризації;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> пакет рекомендацій щодо подальшого розвитку та підвищення вартості бізнесу;</li>
                        <li class="results-list__item stagger"><span class="check-icon" aria-hidden="true">✓</span> план подальшого управління та захисту ключових активів.</li>
                    </ul>
                </div>
                <div class="results-block reveal-up">
                    <h2 class="section-title section-title--sm split-text">Узагальнений перелік груп активів, сформований на підставі НП(С)БО 1 «Загальні вимоги до фінансової звітності»:</h2>
                    <ul class="results-list results-list--assets">
                        <li class="results-list__item stagger">нематеріальні активи;</li>
                        <li class="results-list__item stagger">незавершені капітальні інвестиції;</li>
                        <li class="results-list__item stagger">основні засоби;</li>
                        <li class="results-list__item stagger">інвестиційна нерухомість;</li>
                        <li class="results-list__item stagger">біологічні активи;</li>
                        <li class="results-list__item stagger">фінансові активи;</li>
                        <li class="results-list__item stagger">дебіторська заборгованість;</li>
                        <li class="results-list__item stagger">відстрочені податкові активи;</li>
                        <li class="results-list__item stagger">запаси;</li>
                        <li class="results-list__item stagger">грошові кошти та їх еквіваленти;</li>
                        <li class="results-list__item stagger">витрати майбутніх періодів;</li>
                        <li class="results-list__item stagger">інші активи;</li>
                        <li class="results-list__item stagger">необоротні активи, утримувані для продажу, та групи вибуття.</li>
                    </ul>
                </div>
            </div>
        </section>
"""
html = re.sub(r'<section id="slide-8".*?</section>', res_html.strip(), html, flags=re.DOTALL)

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
