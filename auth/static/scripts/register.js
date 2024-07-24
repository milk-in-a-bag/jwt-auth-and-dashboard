const formEl = document.querySelector('.form');
const errorMessageEl = document.querySelector('.error-message');

formEl.addEventListener('submit', event => {
    event.preventDefault();
    
    const formData = new FormData(formEl);
    const data = Object.fromEntries(formData);

    fetch('http://127.0.0.1:8000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }).then(res => res.json())
      .then(data => {
          if (data.success) {
              // Clear any previous error messages
              errorMessageEl.innerHTML = '';
              // Handle successful response
              console.log(data);
              window.location.href = 'http://127.0.0.1:8000/signin';
          } else {
              // Display error messages
              errorMessageEl.innerHTML = ''; // Clear any existing error messages
              for (const [field, messages] of Object.entries(data)) {
                  if (Array.isArray(messages)) {
                      messages.forEach(message => {
                          const errorItem = document.createElement('p');
                          errorItem.textContent = `${message}`;
                          errorMessageEl.appendChild(errorItem);
                      });
                  }
              }
          }
      })
      .catch(err => {
          // Display error messages
          errorMessageEl.textContent = 'An error occurred. Please try again later.';
          console.error(err);
      });
});
