# My First Web Scraping Project with Python: UN Job List 

## Introduction

Embarking on my journey into web scraping, I recently took on the challenge of extracting valuable job information from a dynamic webpage using Python. In this article, I'll walk you through my first web scraping project, where I utilized the powerful combination of the `requests`, `BeautifulSoup`, and `pandas` libraries to gather data from the UN Job List website and saved it into a dataframe.

## Setting the Stage

The target website for this project is the 'UN Job List' ([https://unjoblist.org/lists/NewJobs](https://unjoblist.org/lists/NewJobs)), a platform that regularly updates job opportunities with the United Nations. To automate the process of extracting job details, I turned to Python and its versatile web scraping tools.

## The Code Breakdown

Let's dive into the code that made this project come to life:

### 1. Making an HTTP GET Request:
```python 
url = 'https://unjoblist.org/lists/NewJobs'
response = requests.get(url).text
```
The requests.get(url) function is used to make an HTTP GET request to the specified URL (https://unjoblist.org/lists/NewJobs). The .text attribute is then used to retrieve the HTML content of the response.

### 2. Creating a BeautifulSoup Object:
```python
soup = BeautifulSoup(response, 'lxml')
```
The HTML content obtained from the HTTP response is passed to BeautifulSoup for parsing. The 'lxml' argument specifies the parser to be used.

### 3. Finding all Table Rows:
```python
tr_elements = soup.find_all('tr')
```
The find_all method is employed to locate all table rows ('tr') in the HTML document.

### 4. Iterating Through Table Rows and Extracting Data:
```python
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
```
The code iterates through each table row, finds all table cells (<td>) within that row, and extracts specific data from different columns of the row. The extracted data is then appended to the job_list for further processing.



### 5. Create a DataFrame from the list
```python 
columns = ['Organisation', 'Duty Station', 'Post Title', 'Closing Date', 'More Info']
df = pd.DataFrame(job_list, columns=columns)

# Save the DataFrame to a CSV file
csv_file_path = 'posts/un_job_list.csv'
df.to_csv(csv_file_path, index=False)

print(f"DataFrame created and saved to: {csv_file_path}")
```
The code creates apprpriate column names and the `pd.DataFrame()` constructor from the `pandas` library is used to create a DataFrame (df) from the previously scraped job_list. 

# 
This project marks my first step into the world of web scraping, showcasing the potential of Python in automating data extraction from websites. The combination of `requests`, `BeautifulSoup`, and `pandas` proved to be a powerful trio for turning messy HTML into a structured and insightful dataset.
