'use strict';
const lista = []

function heitto() {
    return Math.floor(Math.random() * 6) + 1;
}

let heitot = 0;
do {
    heitot = heitto();
    lista.push(heitot)
}
while (heitot !== 6)

const noppa1 = document.querySelector('#noppa');
for (let noppa of lista) {
    noppa1.innerHTML += `<li>${noppa}</li>`;
}
