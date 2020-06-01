import requests


def test_blog():
    post_data = {
        "title": "Python nece oyrenek?",
        "short_description": "sldlfsdlkfb ",
        "content": "sdnfosndfodsnf",
        "blogger_full_name": "Idris Sha"
    }
    response = requests.post('http://35.225.243.133/blogs/', data=post_data)
    expected_status_code = 201
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()
    
    expected_title = post_data['title']
    actual_title =  data['title']

    assert expected_title == actual_title

    assert 'id' in data

    blog_id = data['id']

    response = requests.get(f'http://35.225.243.133/blogs/{blog_id}/')
    expected_status_code = 200
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()
    
    expected_title = post_data['title']
    actual_title =  data['title']

    assert expected_title == actual_title

    put_data = {
        "title": "Python oyrenmeye haradan baslamali?",
        "short_description": "sldlfsdlkfb ",
        "content": "sdnfosndfodsnf",
        "blogger_full_name": "Idris Sha"
    }
    response = requests.put(f'http://35.225.243.133/blogs/{blog_id}/', data=put_data)
    expected_status_code = 200
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()
    
    expected_title = put_data['title']
    actual_title =  data['title']

    assert expected_title == actual_title
    patch_data = {
        "title": "Python öyrənməyə haradan başlamalı?",
    }
    response = requests.patch(f'http://35.225.243.133/blogs/{blog_id}/', data=patch_data)
    expected_status_code = 200
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code

    data = response.json()
    
    expected_title = patch_data['title']
    actual_title =  data['title']

    assert expected_title == actual_title

    response = requests.delete(f'http://35.225.243.133/blogs/{blog_id}/')

    expected_status_code = 204
    actual_status_code = response.status_code

    assert expected_status_code == actual_status_code

