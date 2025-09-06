let logoutbtn = document.getElementById('logout') 
logoutbtn.onclick = (e)=>{
    let bool = confirm('Are u sure?')
    if(!bool){
        e.preventDefault()
    }
}

let deletebtn = document.getElementsByTagName('')
deletebtn.onclick = (e) =>{
    let bool = confirm('delete the product ?')
    if(!bool){
        e.preventDefault()
    }
}