/*

*/ 

const chatGroupPk = document.getElementById("chatGroupPk").value

// 
const socketUrl = `ws://${window.location.host}/chat_group/${chatGroupPk}`

// 
const socket = new WebSocket(socketUrl)

// 
const form = document.getElementById("messageForm")
// 
const messages = document.querySelector('#messages')

const datesAndTimes = document.querySelectorAll('.date-time')
for (let dt of datesAndTimes){
    let dateAndTime = new Date(dt.textContent)
    let dateAndTimeLocal = dateAndTime.toLocaleString()
    dt.textContent = dateAndTimeLocal
}
// 
form.addEventListener("submit", (event) => {
    // 
    // const username = document.querySelector('#usernameInput').value
    // 
    event.preventDefault()
    // 
    let message = document.getElementById("id_message").value
    // 
    socket.send(JSON.stringify({"message": message}))
    // 
    form.reset()
})

// 
socket.addEventListener("message", function(event){
    // 
    const messageObject  = JSON.parse(event.data)
    // 
    const messageElem = document.createElement('p')
    // const username = document.querySelector('#usernameInput').value
    // usernameInput messageObject['username']
    let dateTime = new Date(messageObject['date_time'])
    let dateTimeLocal = dateTime.toLocaleString()
    
    messageElem.innerHTML = `${messageObject['username']}: <b>${messageObject['message']}</b> (${dateTimeLocal})`
    // 
    messages.append(messageElem)
})
