'use strict';

const nimet = ['Johnny', 'DeeDee', 'Joey', 'Marky']

/*
    function concat(taulukko) {

    let nimiString = '';
    for (let nimi of taulukko) {
        nimiString += nimi;
    }
    return nimiString
}
*/
function concat(taulukko) {
    return taulukko.reduce(function (nimi, nimiString) {
        return nimiString + nimi;
    });
}

document.querySelector('#kohde').innerHTML = concat(nimet);