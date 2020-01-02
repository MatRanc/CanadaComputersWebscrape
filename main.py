from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.canadacomputers.com/search/results_details.php?language=en&keywords=graphics+card'

#Opens connection, grabs page, then closes
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#Html parsing
page_soup = soup(page_html, "html.parser")

#Grabs each product
containers = page_soup.findAll("div", {"class":"row mx-0"})

#Loop to read info for all products
for container in containers:
	#Read product title
	product_name = container.a.div.img["alt"]

	#Read brand name from image title
	brand_container = container.findAll("div", {"class":"pq-img-manu_logo_box"})
	brand = brand_container[0].img["alt"]

#Below needs to be reworked as not all products have sale prices, throwing errors. If else statements are ideal (I think...)

	#Price only if sale
	price_sale_container = container.findAll("span", {"class":"text-danger d-block mb-0 pq-hdr-product_price line-height"})
	price_sale = price_sale_container[0].strong.text

	#Price normal
	price_container = container.findAll("span", {"class":"d-block mb-0 pq-hdr-product_price line-height"})
	price = price_container[0].strong.text

	""" Classes for sale price vs normal price
	sale price class = text-danger d-block mb-0 pq-hdr-product_price line-height
	normal price class = d-block mb-0 pq-hdr-product_price line-height
	notice text-danger, if else statements are needed
	"""


print("product_name: " + product_name)
print("brand:  " + brand)
print("price_sale:  " + price_sale)
print("price:  " + price)