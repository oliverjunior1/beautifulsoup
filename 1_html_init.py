# from bs4 import BeautifulSoup
#
# html_doc = '''
# <html>
#     <head>
#         <title>Test Page</title>
#     </head>
#     <body>
#         <h1>Jesus is the light</h1>
#     </body>
# </html>
# '''
#
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# header = soup.find('h1')
# print(header.text)

# from bs4 import BeautifulSoup
#
# html_doc = '''
# <html>
#     <head>
#     </head>
#     <body>
#         <ul>
#             <li>Item 1</li>
#             <li>Item 2</li>
#             <li>Item 3</li>
#         </ul>
#     </body>
# </html>
# '''
#
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# items = soup.find_all('li')
# for item in items:
#     print(item.text)

# from bs4 import BeautifulSoup
#
# html_doc = '''
# <html>
#     <head>
#     </head>
#     <body>
#         <div class="container">
#             <h1>Title</h1>
#             <p>Paragraph content</p>
#         </div>
#     </body>
# </html>
# '''
#
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# container = soup.find('div', class_='container')
# print('Parent tag:', container.parent.name)

from bs4 import BeautifulSoup

html_doc = '''
<html>
<head>
</head>
<body>
    <div id="main">
        <p class="info">Info Paragraph 1</p>
        <p class="info">Info Paragraph 2</p>
    </div>
</body>
</html>
'''

soup = BeautifulSoup(html_doc, 'html.parser')

elements = soup.select('div#main p.info')
for element in elements:
    print(element.get_text())