const lista = []
let a = 0

while (a < 5) {
    const i = +prompt('Syötä numero: ')
    lista[a] = i;
    a++
}
console.log(lista)

for (a = lista.length - 1; a >= 0; a--) {
    console.log(lista[a])
}