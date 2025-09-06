let logoutbtn = document.getElementById('logout') 
logoutbtn.onclick = (e)=>{
    let bool = confirm('Are u sure?')
    if(!bool){
        e.preventDefault()
    }
}

let deletebtn = document.getElementByc('del-btn')
for (let i of cartbtns) {
    i.onclick = (e) =>{
        let bool = confirm('delete a product ?')
        if(!bool){
            e.preventDefault()
        }
    }
    
}