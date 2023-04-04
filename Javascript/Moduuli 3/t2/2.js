const list = document.getElementById('target');

const firstItem = document.createElement('li');
firstItem.textContent = 'First item';
const secondItem = document.createElement('li');
secondItem.textContent = 'Second item';
const thirdItem = document.createElement('li');
thirdItem.textContent = 'Third item';

list.appendChild(firstItem);
list.appendChild(secondItem);
list.appendChild(thirdItem);

secondItem.classList.add('my-item');