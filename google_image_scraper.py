# @author : @rxmi_bkd

from selenium import webdriver
from selenium.webdriver.common.by import By
from scroll_to_bottom import scroll_to_bottom

import os
import urllib
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--number-of-images", required=True, help="number of images to download")
ap.add_argument("-k", "--keyword", required=True, help="keyword to search")
ap.add_argument("-d", "--directory", required=True, help="directory to save images")
args = vars(ap.parse_args())

keyword = args['keyword']
n = int(args['number_of_images'])
d = args['directory']

# create a new Chrome session
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
site = "https://images.google.com/"
driver.get(site)

# searching for the keyword
driver.find_element(By.ID, "L2AGLb").click()
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys(keyword)
search_bar.submit()

scroll_to_bottom(driver)

# get the images
images = driver.find_elements(By.CLASS_NAME, "rg_i")
images_urls = [image.get_attribute("src") for image in images]

if len(images_urls) < n:
    print(f"Only found {len(images_urls)} images")
    n = len(images_urls)
else:
    print(f"Found {len(images_urls)} images")
    choice = input("Do you want to download more images? (y/n)")
    if choice == "n":
        n = len(images_urls)
    else:
        n = int(input("How many images do you want to download? "))
        if n > len(images_urls):
            n = len(images_urls)

# download the images
print("Downloading images...")

if not os.path.exists(d):
    os.mkdir(d)
os.chdir(d)

error_count = 0
for i in range(n):
    image_url = images_urls.pop()
    image_name = keyword + str(i) + ".jpg"
    try:
        urllib.request.urlretrieve(image_url, image_name)
    except:
        error_count += 1

print(f"{error_count} images could not be downloaded")
print(f"Downloaded {n - error_count} / {n} images")
print("Done")
driver.close()
