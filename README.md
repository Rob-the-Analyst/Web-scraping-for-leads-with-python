# Web scraping for leads with Python

# 1. Project Overview
### 1.1 Description
This was a freelance job which involved web scraping a website for potential leads for a client. The clients request for the data is as follows. A webpage containing >5,000 records were to be clicked to reveal a page of data for that person. The relevant fields of data were to then be collected from each page and transferred into a readable and useable excel sheet.

Please note: Due to the sensitive nature of the data, no images which expose the data will be shown. 


### 1.2 Key Information Needed
* Name
* Dat of Birth
* Fiscal Code
* Here Since
* Address
* Telephone Number
* Email
* District
* Common
* CAP

### 1.3 Tools Used
* **Python**
* **Excel**

# 2. Project Execution

### 2.1 Scraping data using selenium packages from Python
The WebScrapeLEads.py file was used to interact with a headless web browser which ran in the background. Firstly, it looped through each link on the search page. Then, it accessed the relevant elements of the webpage and appended them to a list. After this, some formatting of the collected data was require to remove html tags, and split into appropriate elements etc. Finally, the script transformed the collected information to a pandas dataframe and saved it as a csv file. 

### 2.2 Cleaning data in Excel

