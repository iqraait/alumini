// Main initialization and shared functions
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize searchable department dropdown
    if (typeof $ !== 'undefined' && $.fn.select2) {
        $('#id_iqraa_department').select2({
            placeholder: '🔍 Search for a department...',
            allowClear: true,
            width: '100%',
            language: {
                noResults: function() {
                    return "No departments found. Try another search.";
                }
            }
        });
    }
    
    // Auto-expand textareas
    document.querySelectorAll('textarea:not(.child-address)').forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    });
    
    // Mobile optimizations
    if ('ontouchstart' in window) {
        document.querySelectorAll('input, select, textarea').forEach(input => {
            input.style.minHeight = '44px';
        });
    }
    
    // Form submission validation
    const form = document.getElementById('registrationForm');
    const submitBtn = document.getElementById('submitBtn');
    const successMessage = document.getElementById('successMessage');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            let isValid = true;
            let firstError = null;
            
            document.querySelectorAll('.error').forEach(el => el.classList.remove('error'));
            document.querySelectorAll('.error-message.show').forEach(el => el.classList.remove('show'));
            
            const requiredFields = [
                'full_name', 'whatsapp_number', 'email', 'indian_address',
                'father_name', 'mother_name', 'tenure_from', 'tenure_to',
                'country', 'current_city', 'professional_field', 'alumni_activities_interest',
                'hear_about_us'
            ];
            
            requiredFields.forEach(fieldName => {
                const field = document.querySelector(`[name="${fieldName}"]`);
                if (field && !field.value.trim()) {
                    showError(field, 'This field is required');
                    if (!firstError) firstError = field;
                    isValid = false;
                }
            });
            
            // Date validation
            const tenureFrom = document.querySelector('[name="tenure_from"]');
            const tenureTo = document.querySelector('[name="tenure_to"]');
            if (tenureFrom && tenureTo && tenureFrom.value && tenureTo.value && 
                new Date(tenureFrom.value) > new Date(tenureTo.value)) {
                showError(tenureTo, '"To" date must be after "From" date');
                if (!firstError) firstError = tenureTo;
                isValid = false;
            }
            
            // WhatsApp format
            const whatsapp = document.querySelector('[name="whatsapp_number"]');
            if (whatsapp && whatsapp.value && !whatsapp.value.startsWith('+')) {
                showError(whatsapp, 'Please include country code (e.g., +966501234567)');
                if (!firstError) firstError = whatsapp;
                isValid = false;
            }
            
            if (!isValid) {
                e.preventDefault();
                if (firstError) firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
                setTimeout(() => {
                    submitBtn.classList.remove('loading');
                    submitBtn.disabled = false;
                }, 2000);
            } else {
                submitBtn.classList.add('loading');
                if (successMessage) successMessage.style.display = 'block';
            }
        });
    }
});

// Global helper functions
function showError(field, message) {
    field.classList.add('error');
    let errorDiv = field.parentNode.querySelector('.error-message');
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        field.parentNode.appendChild(errorDiv);
    }
    errorDiv.textContent = message;
    errorDiv.classList.add('show');
}


