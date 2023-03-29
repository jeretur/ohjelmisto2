'use strict';
const lista = [];

for (let i = 0; i < 6; i++) {
    const promppi = prompt("Syötä koirulin nimi :)")
    lista.push(promppi)

}

const kohde = document.querySelector('#kohde');
for (let koira of lista.sort().reverse()) {
    kohde.innerHTML += `<ul>${koira}</ul>`;
}