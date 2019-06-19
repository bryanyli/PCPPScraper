from requests import get
from re import compile
from bs4 import BeautifulSoup 

def getAllComponents(URL : str):
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    components = soup.find_all(attrs= {'class' : 'td__name'})
    componentdict = dict()
    for component in components:
        for link in component.find_all('a'):
            name = link.get_text()
        #    print(link.get_text())
            componentlink = 'https://pcpartpicker.com' + link.get('href')
        #    print('https://pcpartpicker.com' + link.get('href'))
            componentdict[name] = componentlink

    return componentdict
        
    

print(getAllComponents('https://pcpartpicker.com/list/sdM2hy'))

componentdict = getAllComponents('https://pcpartpicker.com/list/sdM2hy')
for component in componentdict:
    print(f'{component} : {componentdict[component]}')