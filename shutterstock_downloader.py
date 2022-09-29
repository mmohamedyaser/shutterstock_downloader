from posixpath import split
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import os
from http.cookies import SimpleCookie
from termcolor import colored
from os import system

text = "@mmohamedyaser"
target = "https://twitter.com/mmohamedyaser"
print(colored("Shutterstock Downloader","red"))
print(colored("Code By: ","green") + colored("Mohamed Yaser", "blue"))
twitter = colored("Twitter: ","blue")
print(f"{twitter}\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\")

userdetails0 = []

def read_username(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            userdetails0.append(row[0])

read_username("profile.csv")

profile_location = userdetails0[0].split("|||",1)
profile_name = profile_location[1].replace('"',"")

path = os.getcwd()
shutterstock_download_folder = f"{path}\Shutterstock"

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : shutterstock_download_folder}
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument(f'--user-data-dir={profile_location[0]}')
chrome_options.add_argument(f'--profile-directory={profile_name}')
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.shutterstock.com/home")
assert "Shutterstock" in driver.title

login_success = WebDriverWait(driver, 500).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), ', pick up')]"))).get_attribute("innerHTML")

print(f"{login_success} Login Successful")

try:
    if len(login_success) > 1:
        print(f"Login Successful")
except:
    driver.close()
    system.exit()

urls = []

def read_csv_urls(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            urls.append(row[0])


read_csv_urls("urls.csv")

downloads_num = 1
nondownloads = []

for i in urls:
    driver.get(i)

    if ("image-illustration" in i) or ("image-photo" in i):
        id = i.split("-")[-1]
        elem4 = f"https://www.shutterstock.com/editor/image/{id}"
        isPresent = None
        
        try:
            isPresent = driver.find_element_by_xpath("//strong[contains(text(), 'Editorial Use Only.')]").is_displayed()
        except:
            pass

        driver.get(elem4)
        elem6 = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'Get started')]"))).click()
        try:
            close_buttons = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".icon-close")))
            visible_buttons = [close_button for close_button in close_buttons if close_button.is_displayed()]
            visible_buttons_len = len(visible_buttons)
            print(f"visible_buttons_len: {visible_buttons_len}")
            # visible_buttons_len = visible_buttons_len - 1 
            for i in range(0,visible_buttons_len):
                visible_buttons[i].click()
            try:
                close_buttons_2 = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".icon-close")))
                visible_buttons_2 = [close_buttons_2 for close_buttons_2 in close_buttons_2 if close_buttons_2.is_displayed()]
                visible_buttons_len_2 = len(visible_buttons_2)
                print(f"visible_buttons_len: {visible_buttons_len_2}")
                for i in range(0,visible_buttons_len_2):
                    visible_buttons_2[i].click()
            except:
                pass
        except:
            pass
        elem7 = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH, "//h4[contains(text(), 'Canvas size')]"))).click()
        lock = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeSmall"))).click()
        pixchange = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Pixels"]'))).click()
        pixtocm = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[4]'))).click()
        width_cd = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'width')]")))
        width = width_cd.get_attribute("value")
        height_cd = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'height')]")))
        height = height_cd.get_attribute("value")
        if float(width) >= float(height):
            print (f"Width >= Height : {width} >= {height}")
            width_cd.send_keys(Keys.CONTROL + "a")
            width_cd.send_keys(Keys.DELETE)
            width_cd.send_keys("101")
            width_cd.send_keys(Keys.ENTER)
            WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-automation, "download")]'))).click()
            if isPresent != None:
                time.sleep(5)
                box = driver.find_element_by_xpath("//span/span/input[contains(@name, 'EditorialUseOnly')]")
                driver.execute_script("arguments[0].click();", box)
            else:
                pass
            try:
                WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button//span[contains(text(), "License and download")]'))).click()
                success = WebDriverWait(driver,100).until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "Download successful!")]' ))).text
                downloads_num += 1
                index = urls.index(i)
                print(f"Downloading Shutterstock Image: {downloads_num}/{len(urls)}")
            except:
                nondownloads.append(urls.index(i)+1)
                print(f"Image Has Priveously been downloaded: {i}")
        else:
            print (f"Width < Height : {width} < {height}")
            height_cd.send_keys(Keys.CONTROL + "a")
            height_cd.send_keys(Keys.DELETE)
            height_cd.send_keys("100")
            height_cd.send_keys(Keys.ENTER)
            WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-automation, "download")]'))).click()
            time.sleep(5)
            if isPresent != None:
                time.sleep(5)
                box = driver.find_element_by_xpath("//span/span/input[contains(@name, 'EditorialUseOnly')]")
                driver.execute_script("arguments[0].click();", box)
            else:
                pass
            try:
                WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button//span[contains(text(), "License and download")]'))).click()
                success = WebDriverWait(driver,100).until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "Download successful!")]' ))).text
                downloads_num += 1
                index = urls.index(i)
                print(f"Downloading Shutterstock Image: {downloads_num}/{len(urls)}")
            except:
                nondownloads.append(urls.index(i)+1)
                print(f"Image Has Priveously been downloaded: {i}")
    elif "image-vector" in i:
        elem234 = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Download")]' ))).click()
        try:
            download = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-automation, "LicenseDrawer_DownloadButton")]' ))).click()
            success = WebDriverWait(driver,100).until(EC.visibility_of_element_located((By.XPATH, '//p[contains(@data-automation, "LicenseNowAlert_success_alert")]' ))).text
            downloads_num += 1
            index = urls.index(i)
            print(f"Downloading Shutterstock Image: {downloads_num}/{len(urls)}")
        except:
            nondownloads.append(urls.index(i)+1)
            print(f"Image Has Priveously been downloaded: {i}")


print("Images that have been download previously:")
for i in nondownloads:
    print(f"{i}/{len(nondownloads)}")

# wait for download complete
time.sleep(20)
wait = True
while(wait==True):
    for fname in os.listdir(shutterstock_download_folder):
        if ('crdownload') in fname:
            print('downloading files ...')
            time.sleep(10)
        else:
            wait=False
print('finished downloading all files ...')

driver.close()