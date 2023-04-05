'use strict';
const names = ['John', 'Paul', 'Jones'];

const list = document.getElementById('target')

list.innerHTML =
    '<li>' + names[0] + '</li>\n' +
    '<li>' + names[1] + '</li>\n' +
    '<li>' + names[2] + '</li>';