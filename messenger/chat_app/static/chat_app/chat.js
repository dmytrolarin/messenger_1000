/*
Цей файл відповідає за обробку повідомлень на стороні клієнта
*/ 

// Отримуємо айді або ім'я групи, через яке ми будемо підключатися до неї (до групи)
const chatGroupPk = document.getElementById("chatGroupPk").value
// Вказуємо адресу websocket, щоб сервер розумів куди ми хочемо підключитися
const socketUrl = `ws://${window.location.host}/chat_group/${chatGroupPk}`
// Створюємо об'єкт класу "WebSocket" при його створенні відбувається надсилання запиту підключення на сервер
const socket = new WebSocket(socketUrl)

// Отримуємо форму з айді messageForm
const form = document.getElementById("messageForm")
// Отримуємо div з повідомленнями з бд
const messages = document.querySelector('#messages')

// тут ми отримуємо дати та час, який зазначено в повідомленнях завантажених з бд
const datesAndTimes = document.querySelectorAll('.date-time')
// Перебираємо отримані HTML-елементи з датами та часом
for (let dt of datesAndTimes){
    // Створюємо новий об'єкт класу "Date" з даними дати у фоматі iso
    let dateAndTime = new Date(dt.textContent)
    // переробляємо час у локальний час користувача
    let dateAndTimeLocal = dateAndTime.toLocaleString()
    // вказуємо час повідомлення
    dt.textContent = dateAndTimeLocal
}

// Вказуємо що відбуватиметься під час відправлення форми
form.addEventListener("submit", (event) => {
    // Запобігаємо надсилання форми на сервер та перезавантаження сторінки
    event.preventDefault()
    // Отримуємо текст повідомлення, який написав користувач
    let message = document.getElementById("id_message").value
    // Надсилаємо повідомлення через websocket на сервер, щоб повідомлення прийшло іншим користувачам та переробляємо об'єкт у json рядок
    socket.send(JSON.stringify({"message": message}))
    // Видаляємо усі дані, вказані у формі
    form.reset()
})

// Вказуємо що відбуватиметься коли користувач отримує повідомлення
socket.addEventListener("message", function(event){
    // Перетворюємо повідомлення з json рядка на JS-об'єкт 
    const messageObject  = JSON.parse(event.data)
    // Створюємо html елемент, у якому буде зберігатись отримане повідомлення
    const messageElem = document.createElement('p')
    // Створюємо новий об'єкт класу "Date" з даними дати у фоматі iso
    let dateTime = new Date(messageObject['date_time'])
    // Переносимо дату та час під формат та часовий пояс в залежності від налаштувань користувача
    let dateTimeLocal = dateTime.toLocaleString()
    // Вказуємо те, що буде всередині елемента з повідомленням
    messageElem.innerHTML = `${messageObject['username']}: <b>${messageObject['message']}</b> (${dateTimeLocal})`
    // Додаємо елемент повідомлення до div з повідомленнями 
    messages.append(messageElem)
})
