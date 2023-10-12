
let user_icon = document.createElement('i');
user_icon.classList.add('fa-solid' , 'fa-user' ,'auth-icon')
let user = document.getElementById('username');
user.append(user_icon);

let pass_icon = document.createElement('i');
pass_icon.classList.add('fa-solid' , 'fa-lock' , 'auth-icon')
let password = document.getElementById('password');
password.append(pass_icon);

console.log(user , password);
