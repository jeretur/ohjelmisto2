'use strict';

const osallistujienLkm = +prompt('Syötä osallistujien lukumäärä. ');

const osallistujat = [];

for (let i = 0; i < osallistujienLkm; i++) {
    const nimi = prompt('Syötä osallistujan nimi: ')
    osallistujat.push(nimi);
}

osallistujat.sort();

const kohde = document.querySelector('#kohde');
for (let osallistuja of osallistujat) {
    kohde.innerHTML += `<li>${osallistuja}</li>`;
}
