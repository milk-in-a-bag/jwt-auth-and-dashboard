// Select the form and error message elements
const formEl = document.querySelector('.form');
const errorMessageEl = document.querySelector('.error-message');

// Add an event listener to the form submission
formEl.addEventListener('submit', handleSubmit);

// Define the handleSubmit function
function handleSubmit(event) {
  event.preventDefault();

  // Get the form data
  const formData = new FormData(formEl);
  const data = Object.fromEntries(formData.entries());

  // Make a POST request to the login endpoint
  fetch('http://127.0.0.1:8000/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
    const token = data.jwt;
    console.log(token);
    console.log(data);

    // Store the token in local storage
    localStorage.setItem('token', token);

    // Make a GET request to the user endpoint with the token
    fetchUser(token);
  })
  .catch(error => {
    console.error(error);
    // Display an error message to the user
    errorMessageEl.textContent = 'Invalid credentials';
  });
}

// Define the fetchUser function

/*
function fetchUser(token) {
  fetch('http://127.0.0.1:8000/user', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // You can also update the UI with the user data here
  })
  .catch(error => {
    console.error(error);
  });
}
*/

fetch('http://127.0.0.1:8000/', {
  headers: {
    'Authorization': `Bearer ${token}`,
  },
});