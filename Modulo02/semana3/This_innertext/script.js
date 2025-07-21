// Seleccionamos el botón por su id 
let boton = document.getElementById("CambiarTexto");
let encabezado = document.querySelector("h1");
let parrafo = document.querySelectorAll("textoCambiar");



// Agregamos un evento "click" al botón
boton.addEventListener("click", function() {
    // Cambia el texto del botón usanbdo "this"
    this.innerText = "¡Texto cambiado!";
    encabezado.textContent = "Título nuevo";

    for (let index = 0; index < parrafo.length; index++) {
        parrafo[index].textContent = "Texto cambiado";
        }
        alert("Has hecho click!");
});

encabezado.addEventListener("mouseover", function() {
    // Cambia el color del encabezado al pasar el mouse
    this.textContent = "Nuevo Título";

});
