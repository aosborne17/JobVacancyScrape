import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
import requests
from send_email import send_Email


def extract(page):
    url = f'https://www.indeed.co.uk/jobs?q=Junior+DevOps+Engineer&l=London,+Greater+London&start={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'company').text.strip()
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = ''
        summary = item.find('div', class_ = 'summary').text.strip().replace('\n', '') # At the end we are replacing the newline with nothing
        # summary = item.find('div', {'class' : 'summary'}).text.strip()

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return

joblist = []

# go from 0 to 40 and in steps of 10, this will take the indeed search through first 3 pages
for i in range(0,40,10):
    c = extract(0)
    transform(c)

# Creating a dataframe of our Python Dictionary
df = pd.DataFrame(joblist)

# Turning our pandas dataframe to a CSV file
df.to_csv('JuniorDevOpsJobs.csv')

mail = send_Email()