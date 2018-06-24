
from bs4 import BeautifulSoup as bs
import urllib.request as req
import os


print("Images will be saved to 'facets.la' folder")
print("Downloading...")
path = os.getcwd()
if not os.path.exists(path + "\\facets.la"):
	os.makedirs(path + "\\facets.la")
	os.chdir(path + "\\facets.la")

for i in range(316):
	if i % 63 == 0:
		page_url = "http://www.facets.la/offset/{}/" .format(i)
		page_src = req.urlopen(page_url).read()
		page_soup = bs(page_src, "html.parser")

		for div in page_soup.find_all("div", attrs = {"class": "thumb-image"}):
			preview_url = div.find("a")["href"]
			preview_src = req.urlopen(preview_url).read()
			preview_soup = bs(preview_src, "html.parser")
			name = str(preview_soup.find("h1"))[4:-5]
			if "/" in name:
				name = name.replace("/", "-")
			for preview_div in preview_soup.find_all("div", attrs = {"class": "size13"}):
				if "Download Wallpaper" in str(preview_div):
					image_url = preview_div.find("a")["href"]
					image_src = req.urlopen(image_url).read()
					image = open(name + ".jpg", "ab")
					image.write(image_src)
					image.close()
					print("Downloaded {}" .format(name))

