'use strict';

async function getJoke() {
    try {
        const response = await fetch('https://api.chucknorris.io/jokes/random');
        if (!response.ok) {
            console.log(response.status)
        }
        const jokeData = await response.json();
        console.log(jokeData.value);
    } catch (error) {
        console.error(error.message);
    }
}

getJoke();