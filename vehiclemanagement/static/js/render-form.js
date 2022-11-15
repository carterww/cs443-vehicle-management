function renderForm(type) {
    if (type == 'Customer') {
        document.getElementById('employeeform').style.display = 'none';
    }
    else if (type == 'Employee') {
        document.getElementById('employeeform').style.display = 'block';
    }
}