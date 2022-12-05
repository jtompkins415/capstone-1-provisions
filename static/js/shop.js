
    const cart = [];
    
    const addBtn = document.querySelectorAll('.add-button')
    
    addBtn.forEach((btn) => {
        btn.addEventListener('click', (evt) => {
        evt.preventDefault()
    
        let name = evt.target.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.textContent
        
        let brewery = evt.target.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.textContent
    
        let price = evt.target.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.textContent.slice(7)
    
        let quantity = evt.target.previousElementSibling.firstElementChild.nextElementSibling.value
    
        let total = Number(price) * Number(quantity)
        
        let item = {}
        item.name = name
        item.price = Number(price)
        item.quantity = Number(quantity)
        item.total = total
        console.log(item)
    
        cart.push(item)
        console.log(cart)
        sessionStorage.setItem('shoppingCart', JSON.stringify(cart))
        })
    
        
    });