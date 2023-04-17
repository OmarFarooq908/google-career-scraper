import re
import mysql.connector
import numpy as np


# Change the variables below to suit your MySQL server configurations
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "jobs",
)

mycursor = mydb.cursor()

# Variable declartions
titles = []         # Includes titles of all the jobs
locality = []       # Includes localities of all the jobs
region = []         # Includes regions of all the jobs
country = []        # Includes countries of all the jobs
qualifications = [] # Includes qualifications of all the jobs
time_posted = []    # Includes the time of post of all the jobs

job_all = []
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

# Find all the countries between the words ',,' and 'Qualifications:'
country = re.findall(r"(?<=,,)(.*?)(?=Qualifications:)", file_content, flags=re.S)

# Find all the qualifications between the words 'Qualifications:' and 'Time Posted:'
qualifications = re.findall(r"(?<=Qualifications:)(.*?)(?=Time Posted:)", file_content, flags=re.S)

# Find all the time of posting between the words 'Time Posted:' and 'Title:'
time_posted = re.findall(r"(?<=Time Posted:)(.*?)(?=\n)", file_content, flags=re.S)

'''Without the use of re
start = 'Title:'
end = 'Address:'
title = file_content[file_content.find(start) + len(start):file_content.rfind(end)]
'''

# Cleaning the titles of the new line characters
if (len(titles)==len(localities)==len(regions)==len(country)==len(qualifications)==len(time_posted)):
    for i in range(0,len(titles)):
        titles[i] = titles[i].strip()
        localities[i] = localities[i].strip()

        # Split the string to get the region only and discard the locality
        regions[i] = regions[i].split("\n",1)[1]

        # Remove the new lines from the splitted string
        regions[i] = regions[i].strip()

        # Remove the new lines from the string
        country[i] = country[i].strip()

        # Remove all the new lines and tabs in the string
        qualifications[i] = re.sub('\s+', ' ', qualifications[i])
        # Remove white spaces from the string
        qualifications[i] = qualifications[i].strip()

        # Remove all the new lines and tabs in the string
        time_posted[i] = re.sub('\s+', ' ', time_posted[i])
        # Remove white spaces from the string
        time_posted[i] = time_posted[i].strip()
        # Remove the miliseconds from the string (We have to do that in order to conform to the MySQL 'datetime' data type requirement
        time_posted[i] = time_posted[i].rsplit('.')[0]
        # Remove the T from the string and replace it with ' ' (We have to do that in order to conform to the MySQL 'datetime' data type requirement
        time_posted[i] = time_posted[i].replace('T', ' ')

        temp = []

        temp.extend([titles[i], localities[i], regions[i], country[i], qualifications[i], time_posted[i]])
        job_all.append(temp)

else:
    print(" >> There was some 'Error' encountered. Ending the program...........")
    exit()

sql = "INSERT INTO jobs_google VALUES(%s, %s, %s, %s, %s, %s)"
val = job_all

mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "was inserted.")
