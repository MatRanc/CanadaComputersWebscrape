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

	print("product_name: " + product_name)