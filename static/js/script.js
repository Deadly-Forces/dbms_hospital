// This file contains JavaScript code for client-side functionality, such as form validation and dynamic content updates.

document.addEventListener('DOMContentLoaded', function() {
    const patientForm = document.getElementById('patientForm');
    
    if (patientForm) {
        patientForm.addEventListener('submit', function(event) {
            const age = document.getElementById('age').value;
            const name = document.getElementById('name').value;
            const bloodGroup = document.getElementById('blood_group').value;
            const diseaseType = document.getElementById('disease').value;

            if (!age || !name || !bloodGroup || !diseaseType) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }
});