'use strict';
const lomake = document.querySelector('form');
const apiUrl = lomake.action;


// HYÖDYLLINEN FUNKTIO //
async function fetchJson(url, options = {}) {
    const vastaus = await fetch(url, options);
    if (!vastaus.ok) {
        throw new Error(vastaus.statusText);
    }
    return await vastaus.json();
}

//
lomake.addEventListener('submit', async function (evt) {
    try {
        evt.preventDefault();
        const hakusana = document.querySelector('#query').value;
        const sarjat = await fetchJson(apiUrl + '?q=' + hakusana)

        document.querySelectorAll('.series').forEach(e => e.remove()); //empties the website after a search is done, making sure old search results don't show up after doing a new one
        console.log(sarjat)


        for (let x = 0; x <= sarjat.length; x++) {

            // create a div element and give it a series class
            const ul_list = document.createElement("div");
            ul_list.classList.add('series')


            // create html elements
            const titleItem = document.createElement('h2');
            //titleItem.setAttribute('id', `series${x}_name`)
            const genresItem = document.createElement('p');
            genresItem.classList.add('my-genres')
            // genresItem.setAttribute('id', `series${x}_genres`)
            const imgItem = document.createElement('img');
            imgItem.classList.add('my-image')
            //  imgItem.setAttribute('id', `series${x}_img`)
            const descItem = document.createElement('p');
            descItem.classList.add('my-desc')
            // descItem.setAttribute('id', `series${x}_desc`)
            const linkItem = document.createElement('a');
            // descItem.setAttribute('id', `series${x}_link`)


            // add content inside that list element
            titleItem.insertAdjacentHTML('beforeend', `${sarjat[x].show.name}`);
            genresItem.insertAdjacentHTML('beforeend', (`${sarjat[x].show.genres.join(' | ')}`));
            descItem.insertAdjacentHTML('beforeend', `${sarjat[x].show.summary}`);
            linkItem.insertAdjacentHTML('beforeend', `${sarjat[x].show.url}`);
            linkItem.setAttribute('href', `${sarjat[x].show.url}`)
            //imgItem.insertAdjacentHTML('beforeend',`${sarjat[x].show.image.medium}`);
            if (sarjat[x].show.image !== null) {
                imgItem.setAttribute('src', `${sarjat[x].show.image.medium}`)
            } else {
                imgItem.setAttribute('src', 'https://via.placeholder.com/100x200?text=text+here')
            }
            // add the list element with data to the ul element
            ul_list.appendChild(titleItem);
            ul_list.appendChild(imgItem);
            ul_list.appendChild(genresItem);
            ul_list.appendChild(descItem);
            ul_list.appendChild(linkItem);


            //modal WIP ei ehdi ennen palautusta

            //const btn = document.createElement('button')
            //btn.setAttribute('id', 'myBtn')
            //const modalItem = document.createElement('div')
            //modalItem.setAttribute('id', 'myModal')
            //modalItem.classList.add('modal')

            const currentDiv = document.getElementById("div1");
            document.body.insertBefore(ul_list, currentDiv);


            // palauttaa nimen
            //console.log(sarjat[x].show.name);
            //document.getElementById(`series${x}_name`).innerHTML = `${sarjat[x].show.name}`

            // palauttaa url
            //console.log(sarjat[x].show.url);
            //document.getElementById(`series${x}_link`).innerHTML = `${sarjat[x].show.url}`

            // palauttaa summaryn
            //console.log(sarjat[x].show.summary);
            //document.getElementById(`series${x}_desc`).innerHTML = `${sarjat[x].show.summary}`

            // palauttaa genren
            //console.log(sarjat[x].show.genres);
            //document.getElementById(`series${x}_genres`).innerHTML = sarjat[x].show.genres.join(' | ');

            // palauttaa kuvan (medium)
            //console.log(sarjat[x].show.image.medium);
            //const series0image = document.getElementById(`series${x}_img`)
            //series0image.src = sarjat[x].show.image.medium;               // set src attribute
            // series0image.alt = `${sarjat[x].show.name}`;                       // set alt attribute
        }

    } catch (e) {
        console.error(e.message);

    }
});