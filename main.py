import requests
from bs4 import BeautifulSoup

# 要爬取的網站 URL
url = 'https://github.com/trending/developers'

# 發送請求並取得網頁內容
response = requests.get(url)

# 解析網頁內容
soup = BeautifulSoup(response.content, 'html.parser')

# 找到包含所有開發者的 HTML 元素
developers = soup.find_all('article', class_='Box-row')

# 建立一個空列表，用於存儲每個開發者的名稱和 GitHub 連結
github_links = []

# 迭代每個開發者元素，獲取其名稱和 GitHub 連結
for developer in developers:
    name = developer.find('h1', class_='h3 lh-condensed').text.strip()
    develope_id = developer.find_all('a')[1].get('href')
    # 確認開發者是否有 GitHub 連結
    github_link = 'https://github.com' + develope_id
    github_links.append((name, github_link))

# 輸出每個開發者的名稱和 GitHub 連結 並計算開發者的數量
print('---------------------------------')
print('各別Github連結')
for name, link in github_links:
    print(f'{name}: {link}')
print(f'Total developers: {len(github_links)}')

# 訪問每個開發者的 GitHub 頁面
# 查詢有沒有網頁元素包含開發者的位置個人網站
# 如果有，則輸出開發者的名稱和位置網站
print('---------------------------------')
print('開發者的個人網站')
for name, link in github_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    # 判斷有無個人網站 並取得個人網站連結
    try:
        personal_link = soup.select_one('li[itemprop="url"] a').text.strip()
    except:
        personal_link = None
    print(f'{name}: {personal_link}')
