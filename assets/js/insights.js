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
