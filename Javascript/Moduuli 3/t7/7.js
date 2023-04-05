'use strict';

const target = document.querySelector('#target')
const trigger = document.querySelector('#trigger')

trigger.addEventListener('mouseover', function () {
    target.src = 'img/picB.jpg';
})

trigger.addEventListener('mouseout', function () {
    target.src = 'img/picA.jpg';
})