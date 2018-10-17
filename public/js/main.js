
const numberInput = document.getElementById('number');
const textInput = document.getElementById('msg');
const button = document.getElementById('button');
const response = document.querySelector('.response');

button.addEventListener('click', send, false);

const socket = io();
socket.on('smsStatus', (data) => {
    response.innerHTML = `<h5>Text message sent to ${data.number} with id : ${data.id}</h5>`;
});

function send() {
    const number = numberInput.value.replace(/\D/g, '');
    const text = textInput.value;

    fetch('/', {
        method: 'post',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({number, text})
    })
    .then((res) => {
        console.log('res', res);
    })
    .catch((err) => {
        console.log('err', err);
    });
}
