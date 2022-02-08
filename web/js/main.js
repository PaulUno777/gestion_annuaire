let navbar = document.querySelector('.navbar')
let loginForm = document.querySelector('.login-form')

document.querySelector('#menu-btn').onclick = () => {
  navbar.classList.toggle('active');
  loginForm.classList.remove('active')
}

document.querySelector('#login-btn').onclick = () => {
  loginForm.classList.toggle('active');
  navbar.classList.remove('active');
}

document.querySelector('#signup-link').onclick = () => {
  loginForm.classList.toggle('active');
}

window.onscroll = () => {
  navbar.classList.remove('active');
  loginForm.classList.remove('active')
}
