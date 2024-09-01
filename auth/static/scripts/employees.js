//jquery and data table script

$(document).ready( function () {
    $('#myTable').DataTable();
} );


//form script

const addBtn = document.querySelector('.fa-plus');
const createForm = document.querySelector('.create-form');
const background = document.querySelector('.in-body');
const x = document.querySelector('.fa-xmark');

addBtn.addEventListener('click', () => {
    createForm.style.display = 'block';
    background.style.filter = 'blur(5px)';
    background.style.pointerEvents = 'none';
});

x.addEventListener('click', () => {
    createForm.style.display = 'none';
    background.style.filter = 'none';
    background.style.pointerEvents = 'auto';
});


//fetch script

const formEl = document.querySelector('#cform');

formEl.addEventListener('submit', (event) => {
    event.preventDefault();  // Prevents the default form submission and page reload
    
    const formData = new FormData(formEl);
    const data = Object.fromEntries(formData.entries());

    fetch('http://127.0.0.1:8000/api/employees/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        alert("Employee successfully created!");
        window.location.reload();
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert("There was a problem creating the employee.");
    });
});


//update script

const updateBtns = document.querySelectorAll('.edit-btn');
const editForm = document.querySelector('.edit-form');
const editx = document.querySelector('.editx');
const ename = document.querySelector('#name');
const email = document.querySelector('#email');
const ocontact = document.querySelector('#ocontact');
const pocontact = document.querySelector('#pocontact');
let empID;

updateBtns.forEach(btn => {
    btn.addEventListener('click', () => {

        empID = btn.getAttribute('data-id');

        editForm.style.display = 'block';
        background.style.filter = 'blur(5px)';
        background.style.pointerEvents = 'none';
        console.log('data-id:', empID);

        fetch(`http://127.0.0.1:8000/api/employees/${empID}`)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            ename.value = data.employee_name || ''; // Use empty string if no data
            email.value = data.employee_email || '';
            ocontact.value = data.office_contact || '';
            pocontact.value = data.personal_contact || '';
        })
    });
})

editx.addEventListener('click', () => {
    editForm.style.display = 'none';
    background.style.filter = 'none';
    background.style.pointerEvents = 'auto';
});

const eForm = document.querySelector('#eform');

eForm.addEventListener('submit', (event) => {
    event.preventDefault();  // Prevents the default form submission and page reload
    
    const formData = new FormData(eForm);
    const data = Object.fromEntries(formData.entries());

    fetch(`http://127.0.0.1:8000/api/employees/${empID}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        alert("Employee successfully updated!");
        window.location.reload();
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert("There was a problem updating the employee.");
    });
});


//Delete script

const delBtns = document.querySelectorAll('.delete-btn');
const delForm = document.querySelector('#dform');
const delX = document.querySelector('.delx');
const cancel = document.querySelector('.cancel');
const empName = document.querySelector('.empname')

delBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        empID = btn.getAttribute('data-id');
        delForm.style.display = 'block';
        background.style.filter = 'blur(5px)';
        background.style.pointerEvents = 'none';
        console.log('data-id:', empID);

        fetch(`http://127.0.0.1:8000/api/employees/${empID}`)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            empName.innerHTML = data.employee_name;
        })

})})

delX.addEventListener('click', () => {
    delForm.style.display = 'none';
    background.style.filter = 'none';
    background.style.pointerEvents = 'auto';
});

cancel.addEventListener('click', () => {
    delForm.style.display = 'none';
    background.style.filter = 'none';
    background.style.pointerEvents = 'auto';
});

delForm.addEventListener('submit', (event) => {
    // Optional: You can remove this if you don't need to prevent the default behavior.
    event.preventDefault();

    fetch(`http://127.0.0.1:8000/api/employees/${empID}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        
        // Check if the response body is not empty before parsing it as JSON
        return response.text().then(text => text ? JSON.parse(text) : {});
    })
    .then(data => {
        alert("Employee successfully deleted!");
        window.location.reload();  // Reloads the page after successful deletion
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert("There was a problem deleting the employee.");
    });
});
