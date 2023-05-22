from datetime import datetime
import requests
import time
import re

from bs4 import BeautifulSoup

def get_time():
  now = datetime.now()
  return now.strftime("%Y-%m-%d %H:%M")

def check_jobs():
    url = 'https://www.beta.team/careers/'
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    job_titles = soup.find_all('h4', class_='job-title')
    
    for title in job_titles:
        if re.search(r'human factors', title.text, re.IGNORECASE):
            return True
    
    now = datetime.now()

    return False

def send_notification():
    # Add your notification mechanism here (e.g., email, SMS, push notification)
    print(get_time(), " --- New job(s) with 'human factors' found!")

def print_job_not_found():
    print(get_time(), " --- Did not find the HF job...")

# Run the scraper every hour
while True:
    if check_jobs():
        send_notification()
    else:
        print_job_not_found()
    
    # Wait for one hour before checking again
    time.sleep(3600)
