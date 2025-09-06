let logoutbtn = document.getElementById('logout') 
logoutbtn.onclick = (e)=>{
    let bool = confirm('Are u sure?')
    if(!bool){
        e.preventDefault()
    }
}

let deletebtn = document.getElementById('del-btn')
for (let i of cartbtns) {
    i.onclick = (e) =
    
}