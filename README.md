# PCPPScraper
A simple scraper to get the components in a PCPartPicker URL, using requests and BeautifulSoup

### Github Link:
https://github.com/A1phyte/PCPPScraper

### PyPI Link: 
https://pypi.org/project/PCPPScraper/

## To Do:
- ~~Make a Component class with type of component, name, price, and PCPP Link and return it in getComponents~~
- ~~Fetch Custom Prices~~
- ~~Make pip installable?~~
- Implement Search Method for part searching
- Suggest more in Issues

## Documentation:

### Component

`self.type` = Type of component (CPU, GPU, etc.)

`self.name` = Name of component (2200G, 2080 Ti, etc.)

`self.link` = Link of component (https://pcpartpicker.com/product/RkJtt6/amd-ryzen-3-2200g-35ghz-quad-core-processor-yd2200c5fbbox)

`self.price` = Price of component. Price is 'unknown' if there is no price or there is a custom price.

### getComponents

`getComponents(URL : str)`

Returns a list of class Component.
