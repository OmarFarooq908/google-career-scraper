#-----------------------------------------------------------------------------
#       MIT Licence applies to this file "job_scrap.py"
#       Author: Muhammad Omar Farooq
#-----------------------------------------------------------------------------


import chromedriver_autoinstaller
from selenium import webdriver
import datetime
import time
import requests
from bs4 import BeautifulSoup


try:

    # Initialize the selenium chrome driver
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()

    # Initialize variables for the website pages
    page = 1
    page_total = 72
    page_loop = page_total + 1

    # Scrape the pages until reached the end of the total pages
    while page != page_loop:

        # Load the web page
        driver.get(f'https://careers.google.com/jobs/results/?company=Fitbit&company=GFiber&company=Google&company=YouTube&company=Verily%20Life%20Sciences&company=Waymo&company=Wing&company=X&distance=50&employment_type=FULL_TIME&employment_type=INTERN&hl=en_US&jlo=en_US&page={page}&q=&sort_by=relevance')

        # Wait for the webpage to be completely loaded
        time.sleep(5)

        # Scrape the html of the web page 
        html = driver.page_source
        
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Find all titles of job posts on the page
        jobs = soup.find_all('h2', {'class':'gc-card__title'})

        # Find all the localities of job posts on the page
        addr_locality = soup.find_all('span', {'itemprop':'addressLocality'})

        # Find all the regions of job posts on the page
        addr_region = soup.find_all('span', {'itemprop':'addressRegion'})

        # Find all the countries of job posts on the page
        addr_country = soup.find_all('span', {'itemprop':'addressCountry'})

        # Find all the qualifications of job posts on the page
        qualifications = soup.find_all('div', {'itemprop':'qualifications'})

        # Find all the time of job posts on the page
        time_posted = soup.find_all('meta', {'itemprop':'datePosted'})
        
        # Store the scraped job post information in a text file
        with open('google_jobs.txt', 'a') as f:
            for (title, locality, region, country, qualif, times) in zip(jobs, addr_locality, addr_region, addr_country, qualifications, time_posted):

                # Get the text of the html element containing the title 
                job_title = title.text

                # Get the text of the html element containing the locality
                job_locality = locality.txt

                # Get the text of the html element containing the region
                job_region = region.text

                # Get the text of the html element containing the country
                job_country = country.text

                # Get the text of the html element containing the qualifications
                job_qualifications = qualif.text

                # Get the text of the html element containing the time
                job_time = times['content']


                # We write the job information into the text file
                f.write('Title: ' + str(title.get_text()) + '\n')
                f.write('Address: ' + str(job_locality) + ', ' + str(job_region) + ', ' + str(job_country) + '\n')
                f.write('Qualifications:\n\t' + str(job_qualifications) + '\n')
                f.write('Time Posted: ' + str(job_time) + '\n')
                f.write('\n\n\n\n\n')


            # The following string gets written at the end of every page
            f.write('\n\n\n\n\n')
            f.write('----------------------------------------------------\n')
            f.write('End of Page: ' + str(page) + '\t' + str(datetime.datetime.today()) + '\n')
            f.write('----------------------------------------------------\n')
            f.write('\n\n\n\n\n')

        page = page + 1

except Exception as e:
    print('Error:', e)
