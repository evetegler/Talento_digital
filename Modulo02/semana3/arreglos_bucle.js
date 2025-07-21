let númeroDeCompras = [1000, 2000, 1500, 3000, 2500, 4000, 3500];
let comprasSemana = [];
for (let i = 0; i < númeroDeCompras.length; i++) {
  if (númeroDeCompras[i] > 2000) {
    comprasSemana.push(númeroDeCompras[i]);
  }
}

let total = 0;
for (let i = 0; i < comprasSemana.length; i++) {
  total += comprasSemana[i];
}
console.log("El gasto total fue: $" + total);   