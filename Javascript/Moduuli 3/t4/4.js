'use strict';
const students = [
    {
        name: 'John',
        id: '2345768',
    },
    {
        name: 'Paul',
        id: '2134657',
    },
    {
        name: 'Jones',
        id: '5423679',
    },
];

const target = document.querySelector('#target')

const option = document.createElement("option");
option.innerText = 'Pekka';
option.value = 2342344;

target.appendChild(option);