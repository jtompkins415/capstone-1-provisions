
//add items to cart

(function(){

const shoppingCartTableBody = document.querySelector('#cartTableBody')
let sessionCart = JSON.parse(sessionStorage['shoppingCart'])

for (let i = 0; i < sessionCart.length; i++){
    console.log(sessionCart[i])
    const shoppingCartRow = document.createElement('tr')
    shoppingCartRow.className = 'cartTableRow'
    const deleteBtn = document.createElement('button')
    deleteBtn.className = 'btnDelete'
    shoppingCartTableBody.appendChild(shoppingCartRow)
    for (let k = 0; k < Object.values(sessionCart[i]).length; k++){
        const shoppingCartAllRow = document.querySelectorAll('.cartTableRow')
        const shoppingCartCell = document.createElement('td')
        shoppingCartCell.className = 'cartTableCell'
        shoppingCartCell.innerHTML = Object.values(sessionCart[i])[k]
        shoppingCartAllRow[i].appendChild(shoppingCartCell)
    }

  }

let itemVal = 0;
let sumVal = 0
for( let i = 0; i < shoppingCartTableBody.rows.length; i++){
    itemVal = itemVal + parseFloat(shoppingCartTableBody.rows[i].cells[2].innerHTML)
}

const cartItemTotal = document.getElementById('itemCount')
cartItemTotal.innerHTML = "total Items : " + itemVal
console.log(itemVal)

for(let x = 0; x < shoppingCartTableBody.rows.length; x++){
    sumVal = sumVal + parseFloat(shoppingCartTableBody.rows[x].cells[3].innerHTML);
}


const cartPriceTotal = document.getElementById('totalAmount');
cartPriceTotal.innerHTML = 'Sub-Total : ' + sumVal

const btnDelete = document.getElementById('btnDelete')
btnDelete.addEventListener('click', () => {
    if (sessionStorage.getItem('shoppingCart')) {
		// Clear JavaScript sessionStorage by index
		sessionStorage.removeItem('shoppingCart');
	}
})

})();