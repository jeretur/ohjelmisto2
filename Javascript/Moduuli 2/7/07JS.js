'use strict';
const lista = []

const nopanSivujenLkm = +prompt('Anna nopan sivujen lukumäärä: ')

function heitto() {
    return Math.floor(Math.random() * nopanSivujenLkm) + 1;
}

let heitot = 0;
do {
    heitot = heitto();
    lista.push(heitot)
}
while (heitot !== nopanSivujenLkm)

const noppa1 = document.querySelector('#noppa');
for (let noppa of lista) {
    noppa1.innerHTML += `<li>${noppa}</li>`;
}