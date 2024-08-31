const categories = document.querySelectorAll('.category-filter')
categories.forEach((element) => {

    element.addEventListener('click', () => {
        let url = `${location.origin}/api/product/`
        url += `?category=${element.getAttribute('data-id')}`
        fetch(url).then(response => response.json()).then(data => {
            document.getElementById('shop-product').innerHTML = ''
            console.log(data);
            for (let i in data) {
                document.getElementById('shop-product').innerHTML += `
                <div  class="col-xl-3 col-lg-4 col-md-4">
                    <div class="single-product">
                        <span class="sale-text">Sale</span>
                        <div  class="product-img">
                            <a href="${data[i]['detail_url']}">
                                <img  class="primary-image" src="${data[i]['product_version'][0]['cover_image']}" alt="" />
                            </a>							
                        </div>
                        <div class="product-content">
                            <div class="price-box">
                            ${(data[i]['sale'] ? `<span class="special-price">${data[i]['old_price']}${'$'}</span><span class="old-price">${data[i]['price']}${'$'}</span>` : `<span class="special-price">${data[i]['price']}${'$'}</span>`)}
                                
                            </div>
                            <h2 class="product-name"><a href="">${data[i]['title']}</a></h2>
                            <div class="product-icon">
                            <ul class="d-flex">
                                        <li class="basket" data-id="${data[i]['product_version'][0]['id']}"><i style="cursor: pointer;" data-id="${data[i]['product_version'][0]['id']}" class="fa fa-shopping-cart"></i></li>
                                        <li class="wishlist" data-id="${data[i]['product_version'][0]['id']}"><i style="cursor: pointer;" data-id="${data[i]['product_version'][0]['id']}" class="fa fa-heart"></i></li>
                                     </ul>
                            </div>
                        </div>
                    </div>
                </div>
                `}


            getWishlist()
            getBasket()
        })
    })
})
const manufacturer = document.querySelectorAll('.manufacturer-filter')
manufacturer.forEach((element) => {
    element.addEventListener('click', () => {
        let url = `${location.origin}/api/product/`
        url += `?manufacturer=${element.getAttribute('id')}`
        fetch(url).then(response => response.json()).then(data => {
            document.getElementById('shop-product').innerHTML = ''
            for (let i in data) {
                document.getElementById('shop-product').innerHTML += `
                        <div  class="col-xl-3 col-lg-4 col-md-4">
                            <div class="single-product">
                                <span class="sale-text">Sale</span>
                                <div  class="product-img">
                                    <a href="${data[i]['detail_url']}">
                                        <img style="height: 120px; width: 180px;" class="primary-image" src="${data[i]['product_version'][0]['cover_image']}" alt="" />
                                    </a>							
                                </div>
                                <div class="product-content">
                                    <div class="price-box">
                        
                                    ${(data[i]['sale'] ? `<span class="special-price">${data[i]['old_price']}${'$'}</span><span class="old-price">${data[i]['price']}${'$'}</span>` : `<span class="special-price">${data[i]['price']}${'$'}</span>`)}
                                    </div>
                                    <h2 class="product-name"><a href="">${data[i]['title']}</a></h2>
                                    <div class="product-icon">
                                    <ul class="d-flex">
                                        <li class="basket" data-id="${data[i]['product_version'][0]['id']}"><i style="cursor: pointer;" data-id="${data[i]['product_version'][0]['id']}" class="fa fa-shopping-cart"></i></li>
                                        <li class="wishlist" data-id="${data[i]['product_version'][0]['id']}"><i style="cursor: pointer;" data-id="${data[i]['product_version'][0]['id']}" class="fa fa-heart"></i></li>
                                     </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
`
            }
            getWishlist()
            getBasket()
        })
    })
})


const color = document.querySelectorAll('.color-filter')
color.forEach((element) => {
    element.addEventListener('click', () => {
        let url = `${location.origin}/api/product/`
        url += `?product_version__color=${element.getAttribute('data-id')}`
        fetch(url).then(response => response.json()).then(data => {
            console.log(data);
            document.getElementById('shop-product').innerHTML = ''
            for (let i in data) {


                document.getElementById('shop-product').innerHTML += `
                <div  class="col-xl-3 col-lg-4 col-md-4">
                    <div class="single-product">
                        <span class="sale-text">Sale</span>
                        <div  class="product-img">
                            <a href="${data[i]['detail_url']}">
                                <img style="height:120px;  width:180px;" class="primary-image" src="${data[i]['cover_image']}"  alt="" />
                            </a>							
                        </div>
                        <div class="product-content">
                            <div class="price-box">
                            ${(data[i]['product']['sale'] ? `<span class="special-price">${data[i]['product']['old_price']}${'$'}</span><span class="old-price">${data[i]['product']['price']}${'$'}</span>` : `<span class="special-price">${data[i]['product']['price']}${'$'}</span>`)}
                            </div>
                            <h2 class="product-name"><a href="">${data[i]['product']['title']}</a></h2>
                            <div class="product-icon">
                            <ul class="d-flex">
                                        <li class="basket" data-id="${data[i]['id']}"><i style="cursor: pointer;" data-id="${data[i]['id']}" class="fa fa-shopping-cart"></i></li>
                                        <li class="wishlist" data-id="${data[i]['id']}"><i style="cursor: pointer;" data-id="${data[i]['id']}" class="fa fa-heart"></i></li>
                            </ul>
                            </div>
                        </div>
                    </div>
                </div>
`
            }
            getWishlist()
            getBasket()
        })
    })
})
