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