document.addEventListener('DOMContentLoaded', () => {

    /* -----------------------------------------------------------
     *  Filtered Grid Logic
     * ----------------------------------------------------------- */
    const filterButtons = document.querySelectorAll('.filter-btn');
    const articlesGrid = document.getElementById('articles-grid');
    const cards = document.querySelectorAll('.insight-card');
    const showingTextSpan = document.querySelector('.showing-text .current-category');

    if (filterButtons.length && articlesGrid) {

        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // 1. Update Active State
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                // 2. Get Filter Value
                const filterValue = btn.getAttribute('data-filter');

                // 3. Filter Cards
                let visibleCount = 0;
                cards.forEach(card => {
                    const cardCategory = card.getAttribute('data-category');

                    if (filterValue === 'all' || cardCategory === filterValue) {
                        card.style.display = 'flex'; // Restore display
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, 50);
                        visibleCount++;
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 300); // Wait for transition
                    }
                });

                // 4. Update Header Text
                if (showingTextSpan) {
                    const categoryName = btn.textContent.trim(); // "Strategy", "Trends" etc.
                    showingTextSpan.textContent = categoryName;

                    // Simple animation for text change
                    showingTextSpan.style.opacity = 0;
                    setTimeout(() => {
                        showingTextSpan.style.opacity = 1;
                    }, 200);
                }

                // Optional: Scroll to grid top if user is far down
                // articlesGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });

            });
        });
    }

});

/* -----------------------------------------------------------
 *  Newsletter Integration (Mailchimp)
 * ----------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('.newsletter-form');

    if (forms.length > 0) {
        console.log('Nusa & North: Initializing ' + forms.length + ' newsletter forms');

        const mcAction = "https://nusaandnorth.us12.list-manage.com/subscribe/post?u=466a0a76c281807e8ba35cb92&id=1801094036&f_id=000082e3f0";
        const honeypotName = "b_466a0a76c281807e8ba35cb92_1801094036";

        forms.forEach(form => {
            // 1. Remove dummy handlers
            form.removeAttribute('onsubmit');

            // 2. Set Mailchimp Properties
            form.action = mcAction;
            form.method = "POST";
            form.target = "_blank"; // Open in new tab for standard double-opt-in flow

            // 3. Ensure Email Input has correct name
            const emailInput = form.querySelector('input[type="email"]');
            if (emailInput) {
                emailInput.name = "EMAIL";
            }

            // 4. Inject Honeypot (Anti-Bot)
            // Only add if it doesn't exist yet
            if (!form.querySelector(`input[name="${honeypotName}"]`)) {
                const honeyDiv = document.createElement('div');
                honeyDiv.style.position = 'absolute';
                honeyDiv.style.left = '-5000px';
                honeyDiv.ariaHidden = 'true';
                honeyDiv.innerHTML = `<input type="text" name="${honeypotName}" tabindex="-1" value="">`;
                form.appendChild(honeyDiv);
            }
        });
    }
});
