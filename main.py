#https://www.canadacomputers.com/search/results_details.php?language=en&keywords=graphics+card
#https://www.youtube.com/watch?v=XQgXKtPSzUI&feature=emb_logo

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
	#Product name
	product_name = container.a.div.img["alt"]

	#Product sale price
	price_sale_container = container.findAll("span", {"class":"text-danger d-block mb-0 pq-hdr-product_price line-height"})

	if price_sale_container == [] : price_sale = "Not on sale"
	else: price_sale = price_sale_container[0].strong.text

	print("product_name: " + product_name)
	print("sale_price:  " + price_sale)

	#Product normal price

	#Product brand


	""" Classes for sale price vs normal price
	sale price class = text-danger d-block mb-0 pq-hdr-product_price line-height
	normal price class = d-block mb-0 pq-hdr-product_price line-height
	notice text-danger, if else statements are needed
	"""


#To get more products, triggerScroll() will be needed?
print("product_name: " + product_name)
print("brand:  " + brand) #Not implemented yet
print("price_sale:  " + price_sale)
print("price:  " + price) #Not implemented yet