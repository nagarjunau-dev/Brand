let logoutbtn = document.getElementById('logout') 
logoutbtn.onclick = (e)=>{
    let bool = confirm('Are u sure?')
    if(!bool){
        e.preventDefault()
    }
}

let cartdelbtn = document.getElementsByClassName('dele-btn')
for (let i of cartdelbtn) {
    i.onclick = (e) =>{
        let bool = confirm('delete a product ?')
        if(!bool){
            e.preventDefault()
        }
    }
    
}

function showFields() {
    const selected = document.getElementById('paymentMethod').value;

    // Hide all sections first
    document.getElementById('creditFields').style.display = 'none';
    document.getElementById('paypalFields').style.display = 'none';
    document.getElementById('upiFields').style.display = 'none';

    // Show selected one
    if (selected === 'credit') {
        document.getElementById('creditFields').style.display = 'block';
    } else if (selected === 'paypal') {
        document.getElementById('paypalFields').style.display = 'block';
    } else if (selected === 'upi') {
        document.getElementById('upiFields').style.display = 'block';
    }
}

function showFields(method) {
    // Hide all fields first
    document.getElementById('homefield').style.display = 'none';
    document.getElementById('paypalFields').style.display = 'none';

    // Show selected method's fields
    if (method === 'credit') {
        document.getElementById('creditFields').style.display = 'block';
    } else if (method === 'paypal') {
        document.getElementById('paypalFields').style.display = 'block';
    }
}