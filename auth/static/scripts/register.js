const formEl = document.querySelector('.form');
const errorMessageEl = document.querySelector('.error-message');

formEl.addEventListener('submit', event => {
    event.preventDefault();
    
    const formData = new FormData(formEl);
    const data = Object.fromEntries(formData.entries());

    fetch('http://127.0.0.1:8000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json() )
    .then(data => {
        const token = data.token;
        console.log(token);
        console.log(data);
    })
});
