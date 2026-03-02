// Dynamic children management
document.addEventListener('DOMContentLoaded', function() {
    const childrenContainer = document.getElementById('children-container');
    const addChildBtn = document.getElementById('addChildBtn');
    const hiddenChildrenField = document.querySelector('[name="children"]');
    
    if (!childrenContainer || !addChildBtn || !hiddenChildrenField) {
        console.error('Children elements not found!');
        return;
    }
    
    // Initialize children array from existing data or empty
    let childrenData = [];
    try {
        if (hiddenChildrenField && hiddenChildrenField.value) {
            const parsed = JSON.parse(hiddenChildrenField.value);
            childrenData = Array.isArray(parsed) ? parsed : [];
        }
    } catch (e) {
        console.log('No existing children data or invalid JSON');
        childrenData = [];
    }

    // Function to create a child row
    function createChildRow(index, data = {}) {
        const row = document.createElement('div');
        row.className = 'child-entry';
        row.dataset.index = index;
        
        row.innerHTML = `
            <div class="child-row-header">
                <h5><i class="fas fa-child" style="margin-right: 8px;"></i>Child #${index + 1}</h5>
                <button type="button" class="btn-remove-child">
                    <i class="fas fa-trash-alt"></i> Remove
                </button>
            </div>
            <div class="form-grid">
                <div class="form-group">
                    <label class="form-label">Child Name <span class="required-badge">Required</span></label>
                    <input type="text" class="form-control child-name" value="${data.name || ''}" placeholder="Full name">
                </div>
                <div class="form-group">
                    <label class="form-label">Age/DOB</label>
                    <input type="text" class="form-control child-age" value="${data.age || ''}" placeholder="Age or Date of birth">
                </div>
            </div>
            <div class="form-grid">
                <div class="form-group">
                    <label class="form-label">Child's Iqraa Number</label>
                    <input type="text" class="form-control child-iqraa" value="${data.iqraa || ''}" placeholder="If available">
                </div>
                <div class="form-group">
                    <label class="form-label">Child's Address</label>
                    <textarea class="form-control child-address" rows="2" placeholder="Complete address if no Iqraa number">${data.address || ''}</textarea>
                </div>
            </div>
            <div class="child-status-message"></div>
        `;
        
        // Attach remove event
        const removeBtn = row.querySelector('.btn-remove-child');
        removeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const idx = parseInt(row.dataset.index);
            removeChild(idx);
        });
        
        return row;
    }

    // Add new child
    function addChild() {
        const index = childrenData.length;
        const row = createChildRow(index, {});
        childrenContainer.appendChild(row);
        childrenData.push({ name: '', age: '', iqraa: '', address: '' });
        attachChildListeners(row);
        updateHiddenField();
    }

    // Remove child
    function removeChild(index) {
        const row = document.querySelector(`.child-entry[data-index="${index}"]`);
        if (row) {
            row.remove();
            childrenData.splice(index, 1);
            reindexChildren();
            updateHiddenField();
        }
    }

    // Reindex after removal
    function reindexChildren() {
        const rows = document.querySelectorAll('.child-entry');
        rows.forEach((row, newIndex) => {
            row.dataset.index = newIndex;
            const header = row.querySelector('h5');
            if (header) {
                header.innerHTML = `<i class="fas fa-child" style="margin-right: 8px;"></i>Child #${newIndex + 1}`;
            }
        });
    }

    // Attach input listeners
    function attachChildListeners(row) {
        const nameInput = row.querySelector('.child-name');
        const ageInput = row.querySelector('.child-age');
        const iqraaInput = row.querySelector('.child-iqraa');
        const addressInput = row.querySelector('.child-address');
        const statusMsg = row.querySelector('.child-status-message');
        
        function validateAndUpdate() {
            const idx = parseInt(row.dataset.index);
            childrenData[idx] = {
                name: nameInput.value,
                age: ageInput.value,
                iqraa: iqraaInput.value,
                address: addressInput.value
            };
            
            if (nameInput.value.trim()) {
                if (!iqraaInput.value.trim() && !addressInput.value.trim()) {
                    statusMsg.innerHTML = '<span style="color:#dc3545"><i class="fas fa-exclamation-circle"></i> Please provide either Iqraa number or address</span>';
                    row.classList.add('has-error');
                } else {
                    statusMsg.innerHTML = '<span style="color:#28a745"><i class="fas fa-check-circle"></i> Complete</span>';
                    row.classList.remove('has-error');
                }
            } else {
                statusMsg.innerHTML = '<span style="color:#ffc107"><i class="fas fa-info-circle"></i> Child name is required</span>';
                row.classList.add('has-error');
            }
            
            updateHiddenField();
        }
        
        nameInput.addEventListener('input', validateAndUpdate);
        ageInput.addEventListener('input', validateAndUpdate);
        iqraaInput.addEventListener('input', validateAndUpdate);
        addressInput.addEventListener('input', validateAndUpdate);
        nameInput.addEventListener('blur', validateAndUpdate);
        iqraaInput.addEventListener('blur', validateAndUpdate);
        addressInput.addEventListener('blur', validateAndUpdate);
        
        validateAndUpdate();
    }

    // Update hidden JSON field
    function updateHiddenField() {
        const validChildren = childrenData.filter(child => child.name && (child.iqraa || child.address));
        hiddenChildrenField.value = JSON.stringify(validChildren);
    }

    // Load existing children
    if (childrenData.length > 0) {
        childrenData.forEach((child, index) => {
            const row = createChildRow(index, child);
            childrenContainer.appendChild(row);
            attachChildListeners(row);
        });
    } else {
        // Add one default child
        addChild();
    }

    // Add child button event
    if (addChildBtn) {
        addChildBtn.addEventListener('click', addChild);
    }
});