let req_divs = {
  username: ["fa-solid", "fa-signature"],
  first_name: ["fa-solid", "fa-user"],
  last_name: ["fa-regular", "fa-user"],
  email: ["fa-solid", "fa-at"],
  password: ["fa-solid", "fa-lock"],
  confirm_password: ["fa-regular", "fa-square-check"],
};

for (const [key, val] of Object.entries(req_divs)) {
    let req_div = document.getElementById(String(key))
    let icon = document.createElement('i')
    for(cls of val){
        icon.classList.add(cls) 
    }
    icon.classList.add('auth-icon') 
    req_div.append(icon)
    console.log(icon);
}
