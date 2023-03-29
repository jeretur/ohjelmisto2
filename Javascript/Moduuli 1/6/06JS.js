const check = confirm('Should I calculate the square root?');

if (check === true) {
    const number = Number(prompt('Enter a number: '));
    if (number >= 0) {
        const root = Math.sqrt(number);
        document.querySelector('#Nimi').innerHTML = 'The square root of ' + number + " is " + root;
    } else {
        document.querySelector('#Nimi').innerHTML = "The square root of a negative number is not defined.";
    }
} else {
    document.querySelector('#Nimi').innerHTML = "The square root is not calculated."
}

