const popupForm = document.querySelector(".popup");
const closeForm = document.getElementById("closePopup");
const avatar = document.getElementById('avatar');


avatar.addEventListener('click', ()=>{
    popupForm.classList.remove('hidden');
})

closeForm.addEventListener('click', ()=>{
    popupForm.classList.add('hidden');
})