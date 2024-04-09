import requests
from bs4 import BeautifulSoup
import csv


# to get content from web page
# url="https://www.w3schools.com/python/default.asp"
# r=requests.get(url)
# content=r.content
# # print(r.content)
# # parse the html content
# content_1=BeautifulSoup(content,'html.parser')
# print(content_1)



url="https://www.amazon.in/b/?_encoding=UTF8&node=1389401031&ref_=sv_top_elec_mega_1"
# Send a GET request to the URL
r = requests.get(url)
content=r.content
# print(r.content)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')
# Find all mobile phone containers
mobiles = soup.find_all('div')

    # Initialize a list to store scraped data
mobile_data = []
for mobile in mobiles:
        # Extract price
        price_tag = mobile.find('span', {'class': 'a-size-base a-color-base a-text-bold'})
        price = price_tag.text.strip() if price_tag else 'Not available'

        # Extract amount
        amount_tag = mobile.find('ul', {'class': 'a-unordered-list a-nostyle a-vertical a-spacing-medium'})
        amount = amount_tag.text.strip() if amount_tag else 'Not available'

        # Extract description
        description_tag = mobile.find('div', {'class': 'a-section a-spacing-small'})
        description = description_tag.text.strip() if description_tag else 'Not available'

        # Append data to the list
        if price != 'Not available' or amount != 'Not available' or description != 'Not available':
            mobile_data.append([price, amount, description])

print( mobile_data)

# def save_to_csv(data, filename):
#     # Write data to a CSV file
#     with open(filename, 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Price', 'Amount', 'Description'])
#         writer.writerows(data)

# # URL of the Amazon page with mobile phones
# url = 'https://www.amazon.com/s?k=mobile+phones'



# # Save scraped data to a CSV file
# save_to_csv(mobile_data, 'amazon_mobiles.csv')

# print("Data scraped and saved to 'amazon_mobiles.csv'")




# url="https://www.w3schools.com/sql/default.asp"
# r=requests.get(url)
# content=r.content
# print(content)
# content_1=BeautifulSoup(content,'html.parser')
# print(content_1)
# title=content_1.title
# print(title)
# print(title.text)
# para=content_1.find('p')
# print(para)
# anchor=content_1.find_all('a')
# for i in anchor:
#     print(i)
# tag= content_1.find_all('div')
# count=0
# for i in tag:
#     # print(i)
#     count+=1
# print(count)
# print(content_1.find('div')['id'])
# list=[]
# count=0
# anchor=content_1.find_all('a')
# for link in anchor:
#     link=link.get('href')
#     count+=1
#     list.append(link)
    
# print(list)
# print(count)



# url="https://www.w3schools.com/sql/sql_select.asp"
# r=requests.get(url)
# content=r.content
# content_1=BeautifulSoup(content,'html.parser')
# title=content_1.title
# print(title)
# print(type(title.string))
# print(title.string)


