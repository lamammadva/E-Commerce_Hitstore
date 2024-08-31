function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function getWishlist() {
    const wishlists = document.querySelectorAll('.wishlist');
    wishlists.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/wishlist/`, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                })
            })
            .then((response) => response.json()).then((data) => {
                    console.log(data);
                    alert('Added to Wishlist')
            })
        })
    })
}
getWishlist()


function getBasket() {
    const baskets = document.querySelectorAll('.basket');
    baskets.forEach((element) => {
        element.addEventListener('click', (element) => {
            console.log(element);
            return fetch(`${location.origin}/api/basket/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.target.dataset.id,
                    'quantity':1,
                })
            })
            .then((response) => {
                if (response.status === 200){
                    alert('Added to Basket')
                }
            
        })
        })
    })
}
getBasket()


function getRemovewishlist() {
    const removewishlist = document.querySelectorAll('.sop-icon');
    removewishlist.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/wishlist/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                })
            })
                .then((response) => {
                    if (response.status === 200) {
                        console.log(response.status);
                        fetch(`${location.origin}/api/wishlist/`).then(response => response.json()).then(data => {
                            document.getElementById("shopping_wishlist").innerHTML = ''
                            data['product'].forEach((element) => {
                                document.getElementById('shopping_wishlist').innerHTML += `
                            <tr>
                                <td  data-id="${element['id']}" class="sop-icon">
                                    <i class="fa fa-times"></i>
                                </td>
                                <td class="sop-cart">
                                    <a href="${element['detail_url']}"><img width="150px" class="primary-image" alt="" src="${element['cover_image']}"></a>
                                </td>
                                <td class="sop-cart"><a href="${element['detail_url']}">${element['product']['title']}  ${element['color']['name']}</a></td>
                                <td class="sop"><a href="#">Edit</a></td>
                                <td class="sop-cart">${element['product']['price']}${'$'}</td>
                                <td><input class="input-text qty" type="text" name="qty" maxlength="12" value="1" title="Qty"></td>
                                <td data-id="${element['id']}"><button class="button2  notice elit" title="" type="button">
                                    Add to cart
                                    </button>
                                </td>
                            </tr>
                        `
                            })
                            getRemovewishlist()
                        })

                    }
                })
        })
    })
}

getRemovewishlist()



function getRemoveBasket() {
    const removebasket = document.querySelectorAll('.sop-icon');
    removebasket.forEach((element) => {
        element.addEventListener('click', () => {
            
            return fetch(`${location.origin}/api/basket/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                })
            })
                .then((response) => {
                    if (response.status === 200) {
                        fetch(`${location.origin}/api/basket/`).then(response => response.json()).then(data => {
                            console.log(data);
                            document.getElementById("shopping_basket").innerHTML = ''
                            data['items'].forEach((element) => {
                                document.getElementById('shopping_basket').innerHTML += `
                                <tr>
                                    <td data-id="${element.product.id}" class="sop-icon">
                                        <i style="cursor: pointer;" data-id="${element.product.id}" class="fa fa-times"></i>
                                    </td>
                                    <td class="sop-cart">
                                        <a href="${element['detail_url']}"><img width="150px" class="primary-image" alt="" src="${element['product']['cover_image']}"></a>
                                    </td>
                                    <td class="sop-cart"><a href="${element.detail_url}">${element.product.product.title}</a></td>
                                    ${(element.product.product.sale ? `<td class="sop-cart">$${element.product.product.old_price}</td>`:
                                    `<td class="sop-cart">$${element.product.product.price}${'$'}</td>`)}
                                    <td><input class="input-text qty" type="text" name="qty" maxlength="12" value="${element.quantity}" title="Qty"></td>
                                    <td class="sop-cart">$${element.subtotal}</td>
                                </tr>
                        `
                            })
                            getRemoveBasket()
                        })

                    }
                })
        })
    })
}

getRemoveBasket()



// const likeButton = document.getElementById('fa-heart');
// // Beğen düğmesine tıklama olay dinleyici ekleyin
// likeButton.addEventListener('click', function() {
//     if (likeButton.classList.contains('liked')) {
//         // Beğenildiyse, "liked" sınıfını kaldırın
//         likeButton.classList.remove('liked');
//     } else {
//         // Beğenilmediyse, "liked" sınıfını ekleyin
//         likeButton.classList.add('liked');
//     }
// });