let hamburguesaClasica = {
    pan: "pan con semillas de sésamo",
    carne: "carne de res 100%",
    queso: "queso cheddar",
    extras: ["lechuga", "tomate", "cebolla", "salsa especial"],
    infoHamburguesa: function() {
        console.log("Pan: " + this.pan);
        console.log("Carne: " + this.carne);
        console.log("Queso: " + this.queso);
        console.log("Extras: " + this.extras.join(", "));
    }
}

hamburguesaClasica.infoHamburguesa();
