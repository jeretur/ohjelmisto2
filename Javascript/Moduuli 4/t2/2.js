'use strict';

const searchForm = document.querySelector('#search-form')

searchForm.addEventListener('q', async function (evt) {
    evt.preventDefault();

    const code = document.querySelector('input[name=q]').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);
        const jsonData = await response.json();
        console.log(jsonData.q, jsonData.name)
    } catch (error) {
        console.log(error.message)
    }
});
