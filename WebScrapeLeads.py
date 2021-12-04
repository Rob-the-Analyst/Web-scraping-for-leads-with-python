from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options

# Create driver chrome driver element and pass url
options = Options()
options.headless = True
driver = webdriver.Chrome(options = options)
driver.get('<Url goes here>')

# Find all links on search page. These are the buttons to click to access the page with the information.
links = driver.find_elements(By.XPATH, '//*[@id="wpv-view-layout-179599"]/div[1]/div[4]/a')

# Loop number is based on number of records found by applying len(links). This was found to 5064.
infos_list = []

for i in range(1,5065):

    # This creates the unique xpath for each link on every iteration.
    xpath = '//*[@id="wpv-view-layout-179599"]/div['
    xpath += str(i)
    xpath += "]/div[4]/a"
    web_elem = driver.find_element(By.XPATH, xpath)

    # This accesses each link by clicking it.
    driver.execute_script("arguments[0].click();", web_elem)

    # This scrapes all of the text elements on the page.
    info = driver.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/div').text

    # This splits each element using '\n' as the delimiter.
    info = info.split('\n')

    # These variables are used to select only the elements we want to grab.
    name = info.index('Nome e Cognome')
    dob = info.index('Data di nascita')
    codice = info.index('Codice fiscale')
    questa = info.index('In questa sede dal:')
    indirizzo = info.index('Indirizzo')
    tel = info.index('Telefono')
    email = info.index('Email')
    dis = info.index('Distretto')
    com = info.index('Comune')
    cap = info.index('CAP')

    # This grabs only the relevant information from the text we scraped. We are grabbing the text inside/after each box title.
    new_list = info[name+1], info[dob+1], info[codice+1], info[questa+1], info[indirizzo+1], info[tel+1], info[email+1], info[dis+1], info[com+1], info[cap+1]

    # Append to new list which will contain data for all the records.
    infos_list.append(new_list)

    # Go back to search page once the data has been scraped
    driver.back()


# Transform data into dataframe and save to csv
df=pd.DataFrame(infos_list,columns=['Nome e Cognome','Data di nascita','Codice fiscale','In questa sede dal:','Indirizzo','Telefono','Email','Distretto','Comune','CAP'])
df.to_csv('data.csv')
