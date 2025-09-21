import requests, bs4
throwback_year = input("What year music do you want to throwback to [YYYY-MM-DD]: ")
header = {'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{throwback_year}/", headers=header)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

print(soup.title)
# div_soup = soup.find_all("h3", id="title-of-a-story")
# for text in div_soup:
#     print(text.getText())