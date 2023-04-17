import re

# Variable declartions
titles = []         # Includes titles of all the jobs
locality = []       # Includes localities of all the jobs
region = []         # Includes regions of all the jobs
country = []        # Includes countries of all the jobs
qualifications = [] # Includes qualifications of all the jobs
time_posted = []    # Includes the time of post of all the jobs

# Read the file created by jobs_google.py
f = open('google_jobs.txt', 'r')
file_content = f.read()
# Find all the titles between the words 'Title:' and 'Address:'
    # flags=re.S allows the . metacharacter to match newline characters as well
titles = re.findall(r"(?<=Title:)(.*?)(?=Address:)", file_content, flags=re.S)

# Find all the localities between the words 'Address:' and ','
localities = re.findall(r"(?<=Address:)(.*?)(?=,)", file_content, flags=re.S)

# Find all the regions between the words 'Address:' and ',,'
regions = re.findall(r"(?<=Address:)(.*?)(?=,,)", file_content, flags=re.S)

'''Without the use of re
start = 'Title:'
end = 'Address:'
title = file_content[file_content.find(start) + len(start):file_content.rfind(end)]
'''

# Cleaning the titles of the new line characters
if (len(titles)==len(localities)):
    for i in range(0,len(titles)):
        titles[i] = titles[i].strip()
        localities[i] = localities[i].strip()

        # Split the string to get the region only and discard the locality
        regions[i] = regions[i].split("\n",1)[1]

        # Remove the new lines from the splitted string
        regions[i] = regions[i].strip()

print(regions)
# Printing the titles
#print(titles)
