from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1?crid=2ZGZI18YSMDAF&dib=eyJ2IjoiMSJ9.f_Pv7MmNHnEG85kBFJCsOmvA-Z3Usasg38ESVGOPIeBA22BjLeWcdp-nNagBIVqKjQ-MgE9YBs7n3_fQD7UWwSLxMz-6MaNzCb2ANcD5ruLCd_44s-Z9tmlhJyFTlD3V4VIJCeMG6WSzgQH8_rFQ1hG5e8EDjq4MOD-ulkfpipyaJDFRgWsZ_ZrnFm6D9nd4nedA2Vyc0RAva-44pSVYCAg2hBN6yOef6tbf0ZR1Hy4.ecJvaMOe_bGeBRz9teMhr6kY1wdWpq5Q5U9PQi6Ia00&dib_tag=se&keywords=instant%2Bpot%2Bduo%2Bplus&qid=1759134220&sprefix=instaant%2Bpot%2Bduo%2Caps%2C2471&sr=8-1&th=1")

dollar_price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
cent_price = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

whole_price = f"{dollar_price.text}.{cent_price.text}"
print(whole_price)

driver.quit()




# import requests, bs4

#day 46
# song_list = []
# throwback_year = input("What year music do you want to throwback to [YYYY-MM-DD]: ")
# header = {'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}

# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{throwback_year}", headers=header)
# soup = bs4.BeautifulSoup(response.text, 'html.parser')

# song_names_spans = soup.select("li ul li h3")
# for song in song_names_spans:
#     song_list.append(song.getText().strip())

# print(song_list)
# print(len(song_list))

#day 47
# website = "https://appbrewery.github.io/instant_pot/"
# response = requests.get(url=website, headers=header)
# soup = bs4.BeautifulSoup(response.text, 'html.parser')
# price = soup.find_all("span", class_="aok-offscreen")
# price_string = price[0].getText()
# price_cooker = float(price_string.split("$")[1])
# print(type(price_cooker))

