# import requests

# response = requests.get('https://www.python.org/static/opengraph-icon-200x200.png')

# with open('python.png', 'wb') as f:
#     f.write(response.content)

import requests

response = requests.get('https://www.python.org/')

with open('python.html', 'wb') as f:
    f.write(response.content)