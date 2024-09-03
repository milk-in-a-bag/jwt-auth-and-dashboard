const token = localStorage.getItem('token');
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

/* graph script */

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


/* date script */

const datep = document.querySelector('.datep')
const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
const today = new Date();
const formattedDate = today.toLocaleDateString('en-GB', options);

datep.innerHTML = formattedDate

/* toggle links script */

const minilinks = document.querySelectorAll('.mini-nav a');

minilinks.forEach(minilink => {
        minilink.addEventListener('click', function() {
            minilinks.forEach(minilink => minilink.classList.remove('active'));
            this.classList.add('active');
        });
    });