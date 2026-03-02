    // Conditional address fields for Father, Mother, Spouse
    document.addEventListener('DOMContentLoaded', function() {
        const familyConfig = [
            { name: 'father', iqraaField: 'father_iqraa_num', addressGroup: '.father-address-group', addressField: 'father_address', nameField: null },
            { name: 'mother', iqraaField: 'mother_iqraa_num', addressGroup: '.mother-address-group', addressField: 'mother_address', nameField: null },
            { name: 'spouse', iqraaField: 'spouse_iqraa_num', addressGroup: '.spouse-address-group', addressField: 'spouse_address', nameField: 'spouse_name' }
        ];
        
        familyConfig.forEach(member => {
            const iqraaInput = document.querySelector(`[name="${member.iqraaField}"]`);
            const addressGroup = document.querySelector(member.addressGroup);
            const addressField = document.querySelector(`[name="${member.addressField}"]`);
            const nameField = member.nameField ? document.querySelector(`[name="${member.nameField}"]`) : null;
            
            if (iqraaInput && addressGroup && addressField) {
                function checkCondition() {
                    if (member.name === 'spouse' && nameField && !nameField.value.trim()) {
                        addressGroup.style.display = 'none';
                        addressField.removeAttribute('required');
                        addressField.value = '';
                        addressGroup.classList.remove('required-active');
                        return;
                    }
                    if (!iqraaInput.value.trim()) {
                        addressGroup.style.display = 'block';
                        addressField.setAttribute('required', 'required');
                        addressGroup.classList.add('required-active');
                        const helper = addressGroup.querySelector('.address-helper');
                        if (helper) helper.innerHTML = '<i class="fas fa-exclamation-circle" style="color:#dc3545"></i> Required: Please provide complete address';
                    } else {
                        addressGroup.style.display = 'none';
                        addressField.removeAttribute('required');
                        addressField.value = '';
                        addressGroup.classList.remove('required-active');
                        const helper = addressGroup.querySelector('.address-helper');
                        if (helper) helper.innerHTML = '<i class="fas fa-map-marker-alt"></i> Complete address with city, state, pincode';
                    }
                }
                
                iqraaInput.addEventListener('input', checkCondition);
                iqraaInput.addEventListener('blur', checkCondition);
                if (nameField) {
                    nameField.addEventListener('input', checkCondition);
                    nameField.addEventListener('blur', checkCondition);
                }
                checkCondition();
            }
        });
    });