const i = +prompt('Syötä vuosiluku')
if (i % 4 == 0 && i % 100 == 0 && i % 400 == 0) {
    document.querySelector('#Nimi').innerHTML = "Year " + i + " is a leap year"
} else {
    document.querySelector('#Nimi').innerHTML = "Year " + i + " is not a leap year"
}