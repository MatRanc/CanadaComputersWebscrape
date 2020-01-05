"""
Links:
https://www.canadacomputers.com/search/results_details.php?language=en&keywords=graphics+card
https://www.youtube.com/watch?v=XQgXKtPSzUI&feature=emb_logo

Implement infinate scroll
https://stackoverflow.com/questions/37207959/how-to-scrape-all-contents-from-infinite-scroll-website-scrapy

Todo:
Export to csv
Add percent discount
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.canadacomputers.com/search/results_details.php?language=en&keywords=gaming+laptop"

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

	#Product normal price (when on sale)
	price_normal_on_sale_container = container.div.findAll("div", {"class":"px-0 col-12 productInfoSearch pt-2"})
	price_normal_on_sale_container_2 = price_normal_on_sale_container[0].findAll("span", {"class":"line-height"})
	price_normal_on_sale = price_normal_on_sale_container_2[0].strong.text

	#Allows normal price to be listed even when on sale
	if price_normal_container == [] : price_normal = price_normal_on_sale
	else: price_normal = price_normal_container[0].strong.text

	#Discount amount
	if price_sale_container == [] : discount_amount = 0
														#Replaces commas and dollar signs with nothing so it can be converted to a float
	else: discount_amount = float(price_normal_on_sale.replace(",", "").replace("$", "")) - float(price_sale.replace(",", "").replace("$", "")) 

	#Product brand
	brand_container = container.div.findAll("div", {"class":"pq-img-manu_logo_box"})
	if brand_container == [] : brand = "N\A"
	else: brand = brand_container[0].img["alt"]

	print("brand:  " + brand)
	print("product_name: " + product_name)
	print("price_sale:  " + price_sale)
	print("price_normal:  " + price_normal)
	print("discount_amount:  $" + str(discount_amount))
	print("\n") #Adds a new line to make output neater

#To get more products, triggerScroll() will be needed?