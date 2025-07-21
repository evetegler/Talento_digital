let perro = {
    nombre: "Firulais",
    raza: "Labrador",
    edad: 5,    
    gustos: ["jugar", "comer", "dormir"],
    infoAnimal: function() {
        console.log("Nombre: " + this.nombre);
        console.log("Raza: " + this.raza);
        console.log("Edad: " + this.edad + " años");    
        console.log("Gustos: " + this.gustos.join(", "));
    }
};

perro.infoAnimal();

let gato = {
    nombre: "Michi",
    raza: "Siames",
    edad: 3,    
    gustos: ["dormir", "cazar", "jugar"],
    infoAnimal: function() {    
        console.log("Nombre: " + this.nombre);
        console.log("Raza: " + this.raza);
        console.log("Edad: " + this.edad + " años");    
        console.log("Gustos: " + this.gustos.join(", "));
    }
};
gato.infoAnimal();
let loro = {
    nombre: "Polly",
    raza: "Loro Gris",
    edad: 2,    
    gustos: ["hablar", "jugar", "comer"],
    infoAnimal: function() {    
        console.log("Nombre: " + this.nombre);
        console.log("Raza: " + this.raza);
        console.log("Edad: " + this.edad + " años");    
        console.log("Gustos: " + this.gustos.join(", "));
    }
};
loro.infoAnimal();
let tortuga = {
    nombre: "Tuga",
    raza: "Tortuga de Tierra",
    edad: 10,    
    gustos: ["nadar", "comer lechuga", "tomar el sol"],
    infoAnimal: function() {    
        console.log("Nombre: " + this.nombre);
        console.log("Raza: " + this.raza);
        console.log("Edad: " + this.edad + " años");    
        console.log("Gustos: " + this.gustos.join(", "));
    }
};




           
        