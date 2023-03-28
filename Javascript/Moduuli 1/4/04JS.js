'use strict';
const i = prompt('Syötä nimesi: ')
let result;
result = Math.floor(Math.random()*4)+1;

switch (result){
    case 1:
        document.querySelector('#Nimi').innerHTML = i + ', you are a Gryffindor'
        break;
    case 2:
        document.querySelector('#Nimi').innerHTML = i + ', you are a Slytherin'
        break;
    case 3:
        document.querySelector('#Nimi').innerHTML = i + ', you are a Hufflepuff'
        break;
    case 4:
        document.querySelector('#Nimi').innerHTML = i + ', you are a Ravenclaw'
}