const domain = 'http://35.225.243.133';

$(document).ready(function(){
    document.querySelector('form').addEventListener('submit', function(event){
        event.preventDefault();
        // let form_data = $('form').serializeArray();
        let form_data = new Object();
        document.querySelectorAll('form input').forEach((input) =>{
            form_data[input.getAttribute('name')] = input.value;
        });
        document.querySelectorAll('form small').forEach((small_tag) => {
            small_tag.innerHTML = '';
        })
        $.ajax({
            url: `${domain}/accounts/api/register/`,
            data: form_data,
            method: 'POST',
            success: function(response){
                
                alert('Istifadeci yaradildi');
                window.location = 'login.html';
                // $.ajax({
                //     url: 'login_small.html',
                //     success: function(html_page){
                //         document.querySelector('form').innerHTML = html_page;
                //     }
                // })
            },
            error: function(error_response){
                let error_messages = error_response.responseJSON;
                for(let message_name in error_messages){
                    let input = document.querySelector(`[name="${message_name}"`);
                    let small_tag = input.parentElement.querySelector('small');
                    small_tag.innerText = error_messages[message_name];
                }
            }
        })
    })
});