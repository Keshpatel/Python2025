import requests
from bs4 import BeautifulSoup

# Navigating to the URL and 
url = "https://naveenautomationlabs.com/"
response = requests.get(url, headers={"Accept": "text/html"})
parsed_response = BeautifulSoup(response.text, "html.parser")
print(parsed_response.prettify())
titles = parsed_response.find_all("title")
for title in titles:
    print(title.text)

# #<variable> = pased_response.find_all("<Tag_Name>", Attribute_="Attribute's Value") 
# #<span class="post-date"> All Dates in DOM </span>
post_dates = parsed_response.find_all("span", class_="post-date")
for date in post_dates:
    print(date.text)