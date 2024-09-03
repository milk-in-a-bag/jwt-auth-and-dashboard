$(document).ready( function () {
    $('#myTable').DataTable();
} );


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