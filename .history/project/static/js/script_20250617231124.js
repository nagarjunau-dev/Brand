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

// function showFields() {
//     const selected = document.getElementById('paymentMethod').value;

//     // Hide all sections first
//     document.getElementById('creditFields').style.display = 'none';
//     document.getElementById('paypalFields').style.display = 'none';
//     document.getElementById('upiFields').style.display = 'none';

//     // Show selected one
//     if (selected === 'credit') {
//         document.getElementById('creditFields').style.display = 'block';
//     } else if (selected === 'paypal') {
//         document.getElementById('paypalFields').style.display = 'block';
//     } else if (selected === 'upi') {
//         document.getElementById('upiFields').style.display = 'block';
//     }
// }

function showFields(method) {
    // Hide all fields first
    document.getElementById('homefield').style.display = 'none';
    document.getElementById('officefield').style.display = 'none';

    // Show selected method's fields
    if (method === 'home') {
        document.getElementById('homefield').style.display = 'block';
    } else if (method === 'office') {
        document.getElementById('officefield').style.display = 'block';
    }
}
/* payment */
function showDetails() {
    // Hide all details first
    document.querySelectorAll('.payment-details').forEach(function(el) {
        el.style.display = 'none';
    });

    // Show the selected one
    const selected = document.querySelector('input[name="payment_method"]:checked').value;
    const detailBox = document.getElementById(selected + '-details');
    if (detailBox) {
        detailBox.style.display = 'block';
    }
    }