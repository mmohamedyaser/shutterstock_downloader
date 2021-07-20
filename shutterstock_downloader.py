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

# driver = webdriver.Firefox()
read_username("userpass.csv")

userdetails = userdetails0[0].split("|||", 1)
username = userdetails[0]
userpass = userdetails[1]

path = os.getcwd()
shutterstock_download_folder = f"{path}\Shutterstock"

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : shutterstock_download_folder}
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://accounts.shutterstock.com/login")
assert "Shutterstock" in driver.title

elem = WebDriverWait(driver,100).until(
    EC.element_to_be_clickable((By.XPATH, '//input[contains(@id, "login-username")]' ))
    ).send_keys(username)

elem3 = WebDriverWait(driver,100).until(
    EC.element_to_be_clickable((By.XPATH, '//input[contains(@id, "login-password")]' ))
    ).send_keys(userpass)

elem2 = WebDriverWait(driver,100).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(@id, "login")]' ))
    ).click()

login_success = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Profile')]"))).get_attribute("innerHTML")

if login_success == "Profile":
    print(f"Login Successful")
else:
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

subs = 'image-illustration'
res = [i for i in urls if subs in i]
subs2 = 'image-photo'
res2 = [i for i in urls if subs2 in i]
if urls.index(res[0]) < urls.index(res2[0]):
    first_image = res[0]
else:
    first_image = res2[0]

for i in urls:
    driver.get(i)

    if ("image-illustration" in i) or ("image-photo" in i):
        elem4 = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-automation, 'ImageDetailsPage_conversion_edit')]"))).get_attribute("href")
        driver.get(elem4)
        elem6 = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH, "//div/p[contains(text(), 'Current size')]"))).click()
        if i == first_image:
            elem41 = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/button/span"))).click()
        try:
            close_buttons = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".icon-close")))
            visible_buttons = [close_button for close_button in close_buttons if close_button.is_displayed()]
            visible_buttons_len = len(visible_buttons)
            # print(f"visible_buttons_len: {visible_buttons_len}")
            visible_buttons[visible_buttons_len - 1].click()
        except:
            pass
        elem7 = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH, "//h4[contains(text(), 'Canvas size')]"))).click()
        lock = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/button"))).click()
        pixchange = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[5]/div/div"))).click()
        pixtocm = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[4]'))).click()
        width = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/input'))).get_attribute("value")
        height = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[4]/input'))).get_attribute("value")
        if float(width) >= float(height):
            print (f"Width >= Height : {width} >= {height}")
            elem12 = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/input')))
            elem12.send_keys(Keys.CONTROL + "a")
            elem12.send_keys(Keys.DELETE)
            elem12.send_keys("100")
            elem12.send_keys(Keys.ENTER)
            # WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/input'))).send_keys("100")
            # WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/input'))).send_keys(Keys.ENTER)
            WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-automation, "download")]'))).click()
            try:
                # if len(editoral23) >= 31:
                #     tick =  WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//input[contains(@data-automation, "EditorialCheckbox")]' ))).click()
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
            elem11 = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[4]/input')))
            elem11.send_keys(Keys.CONTROL + "a")
            elem11.send_keys(Keys.DELETE)
            elem11.send_keys("100")
            elem11.send_keys(Keys.ENTER)
            WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-automation, "download")]'))).click()
            try:
                WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button/span[contains(text(), "License and download")]'))).click()
                success = WebDriverWait(driver,100).until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "Download successful!")]' ))).text
                downloads_num += 1
                index = urls.index(i)
                print(f"Downloading Shutterstock Image: {downloads_num}/{len(urls)}")
            except:
                nondownloads.append(urls.index(i)+1)
                print(f"Image Has Priveously been downloaded: {i}")
    elif "image-vector" in i:
        elem234 = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-automation, "ActivationButton_Download_button")]' ))).click()
        try:
            download = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-automation, "ImageLicenseDrawer_confirmNow_button")]' ))).click()
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
time.sleep(5)
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