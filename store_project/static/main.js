console.log("Just checking the connection! :)")

const addToCart = (product_id) => {
    axios.put(`/update-cart/${product_id}/`).then((response) => console.log(response))
}

const deleteItem = (product_id) => {
    axios.post(`/remove-cart-item/`, {
        product_id: product_id
    }).then((response) => {
        console.log(response)
        item = document.getElementById(`${product_id}`)
        item.style.display = 'None';
        window.location.reload()
    })
}
