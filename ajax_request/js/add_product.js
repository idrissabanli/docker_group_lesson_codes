const domain = 'http://35.225.243.133';

$(document).ready(function(){
    if (!localStorage.getItem('token')){
        window.location = 'login.html';
        return
    }
    $.ajax({
        url: `${domain}/api/categories/`,
        method: 'GET',
        success: function(response){
            let select_element = document.querySelector('select[name="category"]');
            for(let category_data of response){
                
                let option = document.createElement('option');
                option.value = category_data.id;
                option.innerText = category_data.title;
                select_element.appendChild(option);
            }
        },
        error: function(error_response){
            alert('Error bas verdi');
        }
    })




    document.querySelector('form').addEventListener('submit', function(event){
        event.preventDefault();

        let formData = new FormData(this);

        document.querySelectorAll('form small').forEach((small_tag) => {
            small_tag.innerHTML = '';
        })
        $.ajax({
            url: `${domain}/api/products/`,
            method: 'POST',
            data:formData,
            cache:false,
            contentType: false,
            processData: false,
            headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`,
            },
            success: function(response){
                alert('Mehsul yaradildi');
                window.location = 'own_products.html';
            },
            error: function(error_response){
                if(error_response.status == 401){
                    localStorage.removeItem('token');
                    window.location = 'login.html';
                    return
                }
                let error_messages = error_response.responseJSON;
                for(let message_name in error_messages){
                    let input = document.querySelector(`[name="${message_name}"`);
                    if(input){
                        let small_tag = input.parentElement.querySelector('small');
                        small_tag.innerText = error_messages[message_name];
                    }
                }
            }
        })
    })
});