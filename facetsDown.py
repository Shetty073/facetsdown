from bs4 import BeautifulSoup as coco
import urllib.request as simba

for i in range(316):
	if i % 63 == 0:
		page_url = "http://www.facets.la/offset/{}/" .format(i)
		page_src = simba.urlopen(page_url).read()
		page_soup = coco(page_src, "html.parser")

		for div in page_soup.find_all("div", attrs = {"class": "thumb-image"}):
			preview_url = div.find("a")["href"]
			preview_src = simba.urlopen(preview_url).read()
			preview_soup = coco(preview_src, "html.parser")
			name = str(preview_soup.find("h1"))[4:-5]
			if "/" in name:
				name = name.replace("/", "-")
			for preview_div in preview_soup.find_all("div", attrs = {"class": "size13"}):
				if "Download Wallpaper" in str(preview_div):
					image_url = preview_div.find("a")["href"]
					image_src = simba.urlopen(image_url).read()
					image = open(name + ".jpg", "ab")
					image.write(image_src)
					image.close()
					print("Downloaded {}" .format(name))
