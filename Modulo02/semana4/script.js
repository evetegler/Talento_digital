
$(document).ready(function () {
    $('#repairForm').on('submit', function (e) {
        e.preventDefault();
        alert('¡Solicitud enviada correctamente! Nos pondremos en contacto contigo.');
        this.reset();
    });
});
