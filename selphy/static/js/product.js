const color_detail = document.querySelectorAll('.color-filter-detail')
// const productTitle = document.getElementById('product_detail_title')
color_detail.forEach((element) => {
    element.addEventListener('click', () => {
        let url = `${location.origin}/api/product_version/`
        console.log(url);
        url += `?color=${element.getAttribute('id')}`
        fetch(url).then(response => response.json()).then(data => {
            console.log(data);
            // productTitle.innerHTML = `<h1>${data.product.title} ${data.color.name}</h1>`;
            document.getElementById('detail_color').innerHTML = `
            <div class="s_big">
                <div>
                    <div class="tab-content jump">
                        <div id="${data['cover_image']}" class="tab-pane fade show active">
                            <div class="simpleLens-big-image-container">
                                <a class="simpleLens-lens-image" data-lens-image="${data['color_url']}">
                                <img  style="width:359px;height:359px" src="${data['cover_image']}" class="simpleLens-big-image">
                            </a>
                        </div>
                    </div>
                    <div  class="thumnail-image fix" >
                        <ul  class="tab-menu nav" >
                            ${data.image.map(element => `
                                <li class=""><a data-bs-toggle="tab" href="${element.image}"><img style="height:100px;" alt="" src="${element.image}"></a>
                            `).join('')}       
                          </ul>
                    </div>
                </div>
            </div>
            
            `;
            document.getElementById('wishlist').innerHTML = `
                <li data-id="${data['id']}" class="wishlist"><i style="cursor:pointer;" data-id="${data['id']}" class="fa fa-heart"></i></li>
            `
            document.getElementById('basket').innerHTML = `
                <button id="basket-detail" data-id="${data['id']}" class="button2 btn-cart " title="" type="button"><span data-id="${data['id']}">Add to Cart</span></button>
            `
            getWishlist()
            getBasketdetail()
        })
    })
})



function getBasketdetail() {
    const basketdetail = document.querySelector('#basket-detail');
    const quantity = document.querySelector('#qty')
    basketdetail.addEventListener('click', (element) => {

        console.log(element.target);

        return fetch(`${location.origin}/api/basket/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'product': element.target.dataset.id,
                'quantity': parseInt(quantity.value),

            })

        })
            .then((response) => {
                if (response.status === 200) {
                    alert('Added to Basket')
                }
            })
    })
}

getBasketdetail()

// $("#qty").on('input',function(){
//     const qty = parseInt($(this).val());
//     $("#qty").attr("value",qty);
// });




























