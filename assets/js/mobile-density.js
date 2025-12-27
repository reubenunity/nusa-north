(function () {
    // Strictly Mobile Only Run
    if (window.innerWidth > 768) return;

    console.log("Mobile Safe Mode: Increasing Grid Density");

    const grid = document.querySelector('.floating-grid');
    if (!grid) return;

    // 1. DIVERSIFY COLUMNS
    // Current: 3 columns. Goal: 5+ columns for "wall" effect.
    const columns = Array.from(grid.querySelectorAll('.grid-column'));

    // We will clone existing columns to add more width/content
    // Clone the first and last column to make 5 total
    if (columns.length > 0) {
        const col1Clone = columns[0].cloneNode(true);
        const col2Clone = columns[1].cloneNode(true);

        // Append to end
        grid.appendChild(col1Clone);
        grid.appendChild(col2Clone);
    }

    // 2. DIVERSIFY ITEMS (VERTICAL DENSITY)
    // For every column, duplicate its items 3x to create a long scroll
    const allColumns = grid.querySelectorAll('.grid-column');
    allColumns.forEach(col => {
        const items = Array.from(col.querySelectorAll('.grid-item'));
        if (items.length === 0) return;

        // Create a fragment to minimize reflows
        const fragment = document.createDocumentFragment();

        // Duplicate existing items 4 times
        for (let i = 0; i < 4; i++) {
            items.forEach(item => {
                fragment.appendChild(item.cloneNode(true));
            });
        }

        col.appendChild(fragment);
    });

})();
