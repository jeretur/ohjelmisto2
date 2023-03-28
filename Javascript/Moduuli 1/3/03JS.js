'use strict';
const i = parseInt(prompt('Syötä luku: '));
const ii = parseInt(prompt('Syötä toinen luku: '));
const iii = parseInt(prompt('Syötä kolmas luku: '));

document.querySelector('#Nimi').innerHTML = "Summa = " + (i + ii + iii);
document.querySelector('#Nimi1').innerHTML = "Kerto = " + (i * ii * iii);
document.querySelector('#Nimi2').innerHTML = "Jako = " + ((i + ii + iii)/3);