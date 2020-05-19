$(document).ready(function(){
    if (localStorage.getItem('token')){
        $.ajax({
            url: 'http://35.225.243.133/api/own-products/',
            method: 'GET',
            headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`,
            },
            success: function(response){

                for(let product of response){
                    $('#products').append(` 
                    <div class="col-lg-3 mb-4">
                        <div class="card">
                            <img src="${product.main_image}" class="card-img-top" alt="...">
                            <div class="card-body">
                            <h5 class="card-title">${product.title}</h5>
                            <p class="card-text">${product.description} <br> Category: ${product.category.title} <br> Price: ${product.price} <br> Owner: ${product.owner.username}</p>
                            <a href="product_detail.html?id=${product.id}" class="btn btn-primary">Go somewhere</a>
                            </div>
                        </div>
                    </div>
                    `);
                }
                
            },
            error: function(error_response){
                if(error_response.status == 401){
                    localStorage.removeItem('token');
                    window.location = 'login.html';
                }
                alert('Sehvlik bas verdi');
            }
        })
    }
    else{
        window.location = 'login.html';
    }
});