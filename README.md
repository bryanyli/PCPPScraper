# PCPPScraper
A simple scraper to get the components in a PCPartPicker URL, using requests and BeautifulSoup

## To Do:
- Make a Component class with type of component, name, price, and PCPP Link and return it in getComponents

## Documentation:

Currently only one function:
### getComponents

`getComponents(URL : str)`

Returns a dict of the component names and PCPP links.

Ex. 
```
{
'AMD - Ryzen 3 2200G 3.5 GHz Quad-Core Processor' : https://pcpartpicker.com/product/RkJtt6/amd-ryzen-3-2200g-35ghz-quad-core-processor-yd2200c5fbbox',
'Gigabyte - B450M DS3H Micro ATX AM4 Motherboard' : 'https://pcpartpicker.com/product/hpRzK8/gigabyte-b450m-ds3h-micro-atx-am4-motherboard-b450m-ds3h'
}
