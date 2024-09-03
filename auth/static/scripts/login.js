// Select the form and error message elements
const formEl = document.querySelector('.form');

formEl.addEventListener('submit', (event) => {
  event.preventDefault();  // Prevents the default form submission and page reload
  
  const formData = new FormData(formEl);
  const data = Object.fromEntries(formData.entries());

  fetch('http://127.0.0.1:8000/login', {
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
      alert("Successfully authenticated")
  })
  .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
      alert("Invalid credentials!");
  });
});

