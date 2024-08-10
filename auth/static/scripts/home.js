const token = localStorage.getItem('token');
console.log("Hello world!");
console.log(token);

fetch('http://127.0.0.1:8000', {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
/*
  if (!token){
    window.location.href = 'http://127.0.0.1:8000/signin';
  }
  */

  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      datasets: [{
        label: 'Revenue in millions',
        data: [12, 19, 3, 5, 2, 3, 4, 5, 6, 7, 8, 9],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });