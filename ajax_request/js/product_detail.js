$(document).ready(function(){
    const product_id = window.location.href.split("id=")[1];
    console.log(product_id);
    
    $.ajax({
        url: `http://35.225.243.133/api/products/${product_id}/`,
        method: 'GET',
        success: function(product_detail){

            $('.card-img-top').attr('src', product_detail.main_image);
            $('.card-title').text(product_detail.title);
            $('.card-text:eq(0)').text(product_detail.description);
            let user_id = parseInt(localStorage.getItem('user_id'));
            if(user_id === product_detail.owner.id){
                document.querySelectorAll('.col-lg-3 a').forEach((btn)=>{
                    btn.classList.remove('d-none');
                });
            }
            
        },
        error: function(error_response){
            alert('Sehvlik bas verdi');
        }
    });
    
    document.querySelectorAll('.col-lg-3 a').forEach((btn)=>{
        btn.setAttribute('href', btn.getAttribute('href') + '?id='+ product_id);
    })
});