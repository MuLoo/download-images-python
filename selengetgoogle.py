
#能够打开预览页 但不能下载
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# import time
# import requests
# import os
# import re

# def valid_filename(name):
#     return re.sub(r'[\\/*?:"<>|]', "", name)[:150]

# def download_image(url, name, folder="images"):
#     try:
#         response = requests.get(url, stream=True)
#         if response.status_code == 200:
#             file_path = os.path.join(folder, name)
#             if not os.path.exists(folder):
#                 os.makedirs(folder)
#             with open(file_path, 'wb') as f:
#                 for chunk in response.iter_content(1024):
#                     f.write(chunk)
#             print(f"Downloaded {name}")
#         else:
#             print(f"Failed to download {url}")
#     except Exception as e:
#         print(f"Error downloading {url}: {e}")

# def fetch_images(search_query, max_images=8):
#     driver = webdriver.Chrome()
#     print("Opened Chrome browser")
#     driver.get("https://images.google.com/")
#     print("Navigated to Google Images")
#     search_box = driver.find_element(By.NAME, "q")
#     print("Found search box")
#     search_box.send_keys(search_query + Keys.RETURN)
#     print(f"Searched for '{search_query}'")

#     try:
#         WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "#dimg_1")))
#     except TimeoutException:
#         print("Timed out waiting for image elements to load. Proceeding with available elements.")

#     image_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/imgres?']")
#     print(f"Found {len(image_links)} image links")

#     for i, link in enumerate(image_links[:max_images], start=1):
#         try:
#             link.click()
#             WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-ved] img")))
#             large_img_element = driver.find_element(By.CSS_SELECTOR, 'a[data-ved] img:first-child')
#             large_img_src = large_img_element.get_attribute('src')
#             if large_img_src:
#                 filename = valid_filename(f"image_{i}") + '.' + large_img_src.split('.')[-1].split('?')[0]
#                 download_image(large_img_src, filename)
#                 print(f"Downloaded {i}/{max_images} images.")
#                 time.sleep(7.5)
#             else:
#                 print(f"Skipping image {i}/{max_images} due to missing large image source.")
#         except TimeoutException:
#             print(f"Timed out waiting for large image to load for image {i}/{max_images}.")
#         except Exception as e:
#             print(f"Error downloading image {i}/{max_images}: {e}")

#     driver.quit()
#     print("Closed Chrome browser")

# if __name__ == "__main__":
#     query = input("Enter your search query: ")
#     max_images = int(input("Enter the maximum number of images to download (default is 8): ") or 8)
#     fetch_images(query, max_images)

#错误没有点击
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# import time
# import requests
# import os
# import re

# def valid_filename(name):
#     """
#     Sanitize a string to be a valid filename by removing illegal characters
#     and truncating it to 150 characters.
#     """
#     return re.sub(r'[\\/*?:"<>|]', "", name)[:150]

# def download_image(url, name, folder="images"):
#     """
#     Download an image from a URL and save it to a specified folder with a specific name.
#     """
#     try:
#         response = requests.get(url, stream=True)
#         if response.status_code == 200:
#             file_path = os.path.join(folder, name)
#             if not os.path.exists(folder):
#                 os.makedirs(folder)
#             with open(file_path, 'wb') as f:
#                 for chunk in response.iter_content(1024):
#                     f.write(chunk)
#             print(f"Downloaded {name}")
#         else:
#             print(f"Failed to download {url}")
#     except Exception as e:
#         print(f"Error downloading {url}: {e}")

# def fetch_images(search_query, max_images=8):
#     """
#     Fetch and download images from Google Images based on a search query.
#     """
#     driver = webdriver.Chrome()
#     driver.get("https://images.google.com/")
#     search_box = driver.find_element(By.NAME, "q")
#     search_box.send_keys(search_query + Keys.RETURN)

#     try:
#         WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.rg_i")))
#     except TimeoutException:
#         print("Timed out waiting for image elements to load. Proceeding with available elements.")

#     image_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/imgres?']")

#     for i, link in enumerate(image_links[:max_images], start=1):
#         try:
#             # Click the link to attempt to open the image
#             driver.execute_script("arguments[0].click();", link)
#             # Wait for the large image to be visible
#             WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'n3VNCb')]")))
#             large_img_element = driver.find_element(By.XPATH, "//img[contains(@class, 'n3VNCb')]")
#             large_img_src = large_img_element.get_attribute('src')
#             if large_img_src:
#                 # Extract the image file extension and download the image
#                 filename = valid_filename(f"image_{i}") + '.' + large_img_src.split('.')[-1].split('?')[0]
#                 download_image(large_img_src, filename)
#                 print(f"Downloaded {i}/{max_images} images.")
#                 time.sleep(7.5)  # Sleep to mitigate rapid request blocking
#             else:
#                 print(f"Skipping image {i}/{max_images} due to missing large image source.")
#         except TimeoutException:
#             print(f"Timed out waiting for large image to load for image {i}/{max_images}.")
#         except Exception as e:
#             print(f"Error downloading image {i}/{max_images}: {e}")

#     driver.quit()

# if __name__ == "__main__":
#     query = input("Enter your search query: ")
#     max_images = int(input("Enter the maximum number of images to download (default is 8): ") or 8)
#     fetch_images(query, max_images)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import requests
import os
import re

def valid_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)[:150]

def download_image(url, name, folder="images"):
    try:
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7mZ7QB_mDT1zdPdDnc4-RXzomp4MIpGmCMJ9RX602Qw&s"
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(folder, name)
            if not os.path.exists(folder):
                os.makedirs(folder)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Successfully downloaded {name}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Exception occurred while downloading {url}: {e}")

def fetch_images(search_query, max_images=8):
    driver = webdriver.Chrome()
    driver.get("https://images.google.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query + Keys.RETURN)

    try:
        # This wait is for the search results to be loaded.
        WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.rg_i")))
        # WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img[id^="dimg_"]')))
        # WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img.id')))
        print("Search results loaded.")
    except TimeoutException:
        print("Timed out waiting for image results to load.")

    image_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/imgres?']")
    print(f"Found {len(image_links)} clickable image links.")

    for i, link in enumerate(image_links[:max_images], start=1):
        try:
            # Ensure each link is interacted with correctly.
            # action = webdriver.common.action_chains.ActionChains(driver)
            # action.move_to_element_with_offset(link, 5, 5)  # Moving to the element and clicking might help.
            # action.click()
            # action.perform()
            link.click()
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-ved] img')))
            large_img_element = driver.find_element(By.CSS_SELECTOR, 'a[data-ved] img:first-child')
            large_img_src = large_img_element.get_attribute('src')
            print(f"Large image source: {large_img_src}")
            # if large_img_src.startswith('http'):
            #     filename = valid_filename(f"image_{i}") + '.' + large_img_src.split('.')[-1].split('?')[0]
            #     download_image(large_img_src, filename)
            if large_img_src:
                print("图片src {large_img_src}")
                filename = valid_filename(f"image_{i}") + '.' + large_img_src.split('.')[-1].split('?')[0]
                download_image(large_img_src, filename)
            else:
                print(f"Skipping image {i}/{max_images}: Large image src did not start with 'http'")
        except TimeoutException:
            print(f"Timed out waiting for large image to load for image {i}/{max_images}.")
        except Exception as e:
            print(f"Error processing image {i}/{max_images}: {e}")

    driver.quit()
    print("Browser closed.")

if __name__ == "__main__":
    query = input("Enter your search query: ")
    max_images = int(input("Enter the maximum number of images to download (default is 8): ") or 8)
    fetch_images(query, max_images)
