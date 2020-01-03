"""
Links:
https://www.canadacomputers.com/search/results_details.php?language=en&keywords=graphics+card
https://www.youtube.com/watch?v=XQgXKtPSzUI&feature=emb_logo

Todo:
Actually read normal price when on sale
"""
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

#Use in terminal when debugging a single container
#container = containers[1]

print("\n") #Makes new line before output for neatness

#Loop to read info for all products
for container in containers:
	#Product name
	product_name = container.a.div.img["alt"]

	#Product sale price
	price_sale_container = container.findAll("span", {"class":"text-danger d-block mb-0 pq-hdr-product_price line-height"})

	if price_sale_container == [] : price_sale = "Not on sale"
	else: price_sale = price_sale_container[0].strong.text

	#Product normal price (when not on sale)
	price_normal_container = container.findAll("span", {"class":"d-block mb-0 pq-hdr-product_price line-height"})

	if price_normal_container == [] : price_normal = "On sale" #Todo: make it actually read normal price
	else: price_normal = price_normal_container[0].strong.text

	#Product normal price (when on sale)
	
	price_normal_container_actual = container.div.findAll("div", {"class":"px-0 col-12 productInfoSearch pt-2"})
	price_normal_container_actual_2 = price_normal_container_actual[0].findAll("span", {"class":"line-height"})
	price_normal_actual = price_normal_container_actual_2[0].strong.text

	#Discount amount

	#Product brand
	brand_container = container.div.findAll("div", {"class":"pq-img-manu_logo_box"})
	if brand_container == [] : brand = "N\A"
	else: brand = brand_container[0].img["alt"]


	print("product_name: " + product_name)
	print("price_sale:  " + price_sale)
	print("price_normal:  " + price_normal)
	print("brand:  " + brand)	
	print("\n") #Adds a new line to make output neater



"""
	data_list_container = container.findAll("div", {"class":"d-inline pl-0_5"})
	data_list = data_list_container[0]

	data_list.findAll("ul", {"class":"&quot"})
"""

#To get more products, triggerScroll() will be needed?
print("product_name: " + product_name)
print("brand:  " + brand) #Not implemented yet
print("price_sale:  " + price_sale)
print("price:  " + price) #Not implemented yet