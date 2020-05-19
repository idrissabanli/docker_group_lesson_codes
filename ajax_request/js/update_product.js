const domain = 'http://35.225.243.133';

$(document).ready(function(){
    if (!localStorage.getItem('token')){
        window.location = 'login.html';
        return
    }
    const product_id = window.location.href.split("id=")[1];
    console.log(product_id);


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
            $.ajax({
                url: `http://35.225.243.133/api/products/${product_id}/`,
                method: 'GET',
                success: function(product_detail){
                    document.querySelectorAll('form input:not([type="file"]), form textarea').forEach((input)=>{
                        let input_name = input.getAttribute('name');
                        if(product_detail.hasOwnProperty(input_name)){
                            if(product_detail[input_name] !== null)
                                input.value = product_detail[input_name];
                        }
                    });
        
                    let product_category_id  = product_detail.category.id;
                    let selected_option = select_element.querySelector(`option[value="${product_category_id}"`);
                    selected_option.selected = true;
                    
                },
                error: function(error_response){
                    alert('Sehvlik bas verdi');
                }
            });
        },
        error: function(error_response){
            alert('Error bas verdi');
        }
    })


    var dataURLToBlob = function(dataURL) {
        var BASE64_MARKER = ';base64,';
        if (dataURL.indexOf(BASE64_MARKER) == -1) {
          var parts = dataURL.split(',');
          var contentType = parts[0].split(':')[1];
          var raw = decodeURIComponent(parts[1]);
    
          return new Blob([raw], {type: contentType});
        }
    
        var parts = dataURL.split(BASE64_MARKER);
        var contentType = parts[0].split(':')[1];
        var raw = window.atob(parts[1]);
        var rawLength = raw.length;
    
        var uInt8Array = new Uint8Array(rawLength);
    
        for (var i = 0; i < rawLength; ++i) {
          uInt8Array[i] = raw.charCodeAt(i);
        }
    
        return new Blob([uInt8Array], {type: contentType});
    }

    document.querySelector('form').addEventListener('submit', function(event){
        event.preventDefault();

        let formData = new FormData();
        // console.log(formData.entries());
        let blob = dataURLToBlob('http://35.225.243.133/media/product-images/3_2_2000x750x220dpi_2gmOo75.jpg');
        formData.append('main_image', new File([blob], 'image.jpg'))
        // for(var field of formData.entries()){
        //     console.log(field[1])
        //     if (field[0] === 'main_image' && field[1].size === 0){
                
        //     }
        // }
        // return false;

        document.querySelectorAll('form small').forEach((small_tag) => {
            small_tag.innerHTML = '';
        })
        $.ajax({
            url: `${domain}/api/products/${product_id}/`,
            method: 'PUT',
            data:formData,
            dataType: 'json', //return response as json
            mimeType: "multipart/form-data",
            cache:false,
            contentType: false,
            processData: false,

            headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`,
            },
            success: function(response){
                alert('Mehsul yaradildi');
                window.location = `product_detail.html?id=${product_id}`;
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