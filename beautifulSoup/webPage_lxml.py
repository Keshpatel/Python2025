from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text
    skills = job.find('div', class_='more-skills-sections').span.text

    print(f"Company Name : {company_name.strip()}")
    print(f"Required skills  : {skills.strip()}")

