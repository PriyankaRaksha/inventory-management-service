function renderInventory(items) {
    document.getElementById("inventory").innerHTML =
        items.map(item =>
            `<div>${item.name}</div>`
        ).join("");
}

function renderSupplier(data) {
    document.getElementById("supplier").innerHTML =
        `<p>${data.name}</p>`;
}

function renderInventorySummary(summary) {
    const container = document.getElementById("summary");

    container.innerHTML = summary.map(item => `
        <div class="summary-card">
            <h3>${item.category}</h3>
            <p>Total Stock: ${item.total_stock}</p>
        </div>
    `).join("");
}