'use strict';
const lista = []
let syöte = 1;
while (syöte != 0) {
    syöte = +prompt('Anna numeroita, sama lopettaa.')
    if (lista.includes(syöte)) {
        window.alert("Numero " + syöte + " on jo syötetty.")
        break;
    } else {
        lista.push(syöte)
    }
}

lista.sort((a, b) => a - b);
for (let i of lista) {
    console.log(i)
}