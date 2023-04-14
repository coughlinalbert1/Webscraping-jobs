# pip install requests | pip install lxml | pip install beautifulsoup4 | 
from bs4 import BeautifulSoup
import requests
import time


# get skills to filter out job postings
unfamiliar_skill = []
print('Put some skill you are not familiar with\nType "exit" to search for jobs')
while True:
    response = input('>').lower()
    if response == "exit":
        break
    unfamiliar_skill.append(response)




def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')


    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = "sim-posted").span.text.replace(" ", "")

        if 'few' in published_date:
            skills = str.replace(job.find('span', class_ = "srp-skills").text, " ", "").lower()
            company_name = str.replace(str.replace(job.find('h3', class_ = "joblist-comp-name").text, "(More Jobs)", ""), " ", "")
            more_info = job.header.h2.a['href']
            # checks if an funfamiliar skill is in the job posting
            boolean = True
            for item in unfamiliar_skill:
                if item in skills:
                    boolean = False
                    break
            
            if boolean:    
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"link: {more_info}\n")   
                print(f'file saved: {index}')  
 

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)