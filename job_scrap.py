import chromedriver_autoinstaller
from selenium import webdriver
import time
import datetime

import requests
from bs4 import BeautifulSoup


try:
    # Your web scraping code here


    # Send a GET request to the URL and get the page content
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()

    page = 1
    page_total = 72
    page_loop = page_total + 1

    while page != page_loop:
        print("Should be going good")
        driver.get(f'https://careers.google.com/jobs/results/?company=Fitbit&company=GFiber&company=Google&company=YouTube&company=Verily%20Life%20Sciences&company=Waymo&company=Wing&company=X&distance=50&employment_type=FULL_TIME&employment_type=INTERN&hl=en_US&jlo=en_US&page={page}&q=&sort_by=relevance')
        time.sleep(5)
        print("Tell me")
        html = driver.page_source
        print("Good")
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Find all job listings on the page
        jobs = soup.find_all('h2', {'class':'gc-card__title'})
        addr_locality = soup.find_all('span', {'itemprop':'addressLocality'})
        addr_region = soup.find_all('span', {'itemprop':'addressRegion'})
        addr_country = soup.find_all('span', {'itemprop':'addressCountry'})
        qualifications = soup.find_all('div', {'itemprop':'qualifications'})
        time_posted = soup.find_all('meta', {'itemprop':'datePosted'})
        print("Not good")
        # Store the job titles in a text file
        with open('google_jobs.txt', 'a') as f:
            for (title, locality, region, country, qualif, time) in zip(jobs, addr_locality, addr_region, addr_country, qualifications, time_posted):
                job_title = title.text
                job_locality = locality.txt
                job_region = region.text
                job_country = country.text
                job_qualifications = qualif.text
                job_time = time['content']

                print("Hey")

                f.write('Title: ' + str(title.get_text()) + '\n')
                f.write('Address: ' + str(job_locality) + ', ' + str(job_region) + ', ' + str(job_country) + '\n')
                f.write('Qualifications:\n\t' + str(job_qualifications) + '\n')
                f.write('Time Posted: ' + str(job_time) + '\n')
                f.write('\n\n\n\n\n')

            f.write('\n\n\n\n\n')
            f.write('----------------------------------------------------\n')
            f.write('End of Page: ' + str(page) + '\t' + str(datetime.datetime.today()) + '\n')
            f.write('----------------------------------------------------\n')
            f.write('\n\n\n\n\n')

        print("Going good")
        page = page + 1
        print("Still going good?")

except Exception as e:
    print('Error:', e)
