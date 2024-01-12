import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

# URL of the webpage to scrape
url = 'https://unjoblist.org/lists/NewJobs'

# Make an HTTP GET request to the URL
response = requests.get(url).text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response, 'lxml')

# Find all table rows in the HTML
tr_elements = soup.find_all('tr')

# Lists to store scraped data
job_list = []

# Iterate through each table row
for index, tr in enumerate(tr_elements):
    # Find all table cells (td) in the current row
    td_elements = tr.find_all('td')

    # Check if there is at least one table cell in the row
    if len(td_elements) > 0:
        # Update variables with data from specific positions (columns) in the row
        organisation = td_elements[0].text.strip()   # Column 1: Organisation
        duty_station = td_elements[1].text.strip()    # Column 2: Duty Station
        post_title = td_elements[4].text.strip()      # Column 5: Post Title
        closing_date = td_elements[5].text.strip()    # Column 6: Closing Date
        more_info = td_elements[4].a['href']

        # Append the data to the list
        job_list.append([organisation, duty_station, post_title, closing_date, more_info])

# Create a DataFrame from the list
columns = ['Organisation', 'Duty Station', 'Post Title', 'Closing Date', 'More Info']
df = pd.DataFrame(job_list, columns=columns)

# Save the DataFrame to a CSV file
csv_file_path = 'posts/un_job_list.csv'
df.to_csv(csv_file_path, index=False)

print(f"DataFrame created and saved to: {csv_file_path}")
