function renderInventory(items) {
    document.getElementById("inventory").innerHTML =
        items.map(item =>
            `<div>${item.name}</div>`
        ).join("");
}