'use strict';
const lista = []
let syöte = 1;
while (syöte != 0) {
    syöte = +prompt('Anna numero, 0 lopettaa.')
    if (syöte != 0) {
        lista.push(syöte)
    }
}

lista.sort((a, b) => b - a);
for (let i of lista) {
    console.log(i)
}