import requests
from bs4 import BeautifulSoup
from time import sleep

for page_number in range(1, 3):
    url = "https://www.timesjobs.com/jobs-in-canada/&sequence=1&startPage="+str(page_number)
    print("Url->:", url)
    sleep(1)
    # Receive full response of page 
    response = requests.get(url, headers={"Accept": "text/html"})
    soup = BeautifulSoup(response.text, 'lxml')
    #parse full response to DOM 
    parsed_response = BeautifulSoup(response.text, "html.parser")
    jobs = parsed_response.find_all("li", class_="clearfix joblistli")
    title_elements = parsed_response.find_all("h3", class_="joblist-comp-name") 
    job_descriptions = parsed_response.find_all("li", class_="job-description__")      
    # print("Jobs :", list(map(lambda x: x.text.strip(), jobs)))
    print(f"Company's name Captured  : ",list(map(lambda x: x.text.strip(), title_elements)), "\n")
    print(f"job description : ", list(map(lambda x: x.text.strip(), job_descriptions)), "\n")  
    sleep(1)