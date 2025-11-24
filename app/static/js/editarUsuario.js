document.addEventListener('DOMContentLoaded', function () {
    const createUserForm = document.getElementById('createUserForm');
    const saveUserBtn = document.getElementById('saveUserBtn');

    createUserForm.addEventListener('submit', function() {
        saveUserBtn.disabled = true;
        saveUserBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Guardando...';
    });

//Reinicio a página create
window.addEventListener('pageshow', function(event) {            
    if (event.persisted) {
        window.location.reload();
    }
}); 
});