let logoutbtn = document.getElementById('logout') 
logoutbtn.onclick = (e)=>{
    let bool = confirm('Are u sure?')
    if(!bool){
        e.preventDefault()
    }
}

let cartdelbtn = document.getElementsByClassName('del-btn')
for (let i of cartdelbtn) {
    i.onclick = (e) =>{
        let bool = confirm('delete a product ?')
        if(!bool){
            e.preventDefault()
        }
    }
    
}