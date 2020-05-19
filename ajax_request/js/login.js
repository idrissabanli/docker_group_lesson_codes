const domain = 'http://35.225.243.133';

$(document).ready(function(){
    document.querySelector('form').addEventListener('submit', function(event){
        event.preventDefault();
        let form_data = new Object();
        document.querySelectorAll('form input').forEach((input) =>{
            form_data[input.getAttribute('name')] = input.value;
        });
        document.querySelectorAll('form small').forEach((small_tag) => {
            small_tag.innerHTML = '';
        })
        $.ajax({
            url: `${domain}/accounts/api/login/`,
            method: 'POST',
            data: form_data,
            success: function(response){
                console.log(response);
                localStorage.setItem('user_id', response.id);
                localStorage.setItem('token', response.token);

                window.location = 'own_products.html';
                alert('Istifadeci daxil oldu');
            },
            error: function(error_response){
                alert('Sehvlik var');
                console.log('error_response', error_response)
                let error_messages = error_response.responseJSON;
                if(error_messages.hasOwnProperty('non_field_errors')){
                    document.querySelector('#non_field_errors').innerText = error_messages['non_field_errors'];
                }
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
})