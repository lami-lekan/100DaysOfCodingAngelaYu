import requests, bs4

#day 46
# song_list = []
# throwback_year = input("What year music do you want to throwback to [YYYY-MM-DD]: ")
header = {'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}

# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{throwback_year}", headers=header)
# soup = bs4.BeautifulSoup(response.text, 'html.parser')

# song_names_spans = soup.select("li ul li h3")
# for song in song_names_spans:
#     song_list.append(song.getText().strip())

# print(song_list)
# print(len(song_list))

#day 47
website = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url=website, headers=header)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
price = soup.find_all("span", class_="aok-offscreen")
price_string = price[0].getText()
price_cooker = float(price_string.split("$")[1])
print(type(price_cooker))

