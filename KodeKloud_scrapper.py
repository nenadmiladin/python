from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

def row_number():
    # Counts the number of rows in the table
    global rows
    rows = 0
    table_rows = driver.find_elements_by_xpath('//*[@id="main-wrapper"]/div[3]/div/div/div[1]/div[3]/div/div/div[4]/table/tbody/tr')
    for row in table_rows:
        rows += 1
    rows = rows - 1 # REAL NUMBER OF ROWS
    

def dataframe(rows):
    global df
    for i in range(2, rows + 2):
        data = driver.find_elements_by_xpath('//*[@id="main-wrapper"]/div[3]/div/div/div[1]/div[3]/div/div/div[4]/table/tbody/tr[' + str(i) + ']/td')
        table_data = [element.text for element in data]
        series = pd.Series(table_data, index=df.columns)
        df = df.append(series, ignore_index=True)
    df.loc[df.Status == "Failed\nView Details", "Status"] = "Failed"
    df.loc[df.Status == "Go", "Status"] = "Pending"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # HEADLESS BROWSER
chrome_options.add_argument("--log-level=3") # DON'T SHOW LOGS IN CLI
chrome_driver_binary = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_binary, options=chrome_options)

driver.get('https://www.kodekloud-engineer.com')
driver.implicitly_wait(30)

username = driver.find_element_by_id("inputEmail").send_keys("nenadmiladin@yahoo.com")
password = driver.find_element_by_id("inputPassword").send_keys("kodekloud4life")

sign_in_button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div/form[1]/button[1]").click()
sleep(2)

dropdown = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[2]/button").click()
sleep(0.5)

dropdown_100 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[2]/div/a[5]").click()
sleep(4.5)

# Scroll to the bottom of the page by executing JS
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# ---------------- Second Part of the Script ------------------------------------------------------------------
# Get the Table Header
header = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div/div/div[1]/div[3]/div/div/div[4]/table/thead/tr').text.split(' ')
table_header = header[:2] + [header[2] + " " + header[3]] + header[-2:]

# DATAFRAME CREATION FIRST PAGE
df = pd.DataFrame(columns = table_header)

row_number()
dataframe(rows)

# CLICK ON NEXT BUTTON
next = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div/div/div[1]/div[3]/div/div/div[6]/a[2]')
next.click()
sleep(4)

# CHECK IF THERE ARE MORE THAT 100 TASKS
# task_number = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div/div/div[1]/div[3]/div/div/div[6]')
# task_number.text.split(' of ')[1].split(' entries ')[0]

# SECOND PAGE
row_number()
dataframe(rows)
print(driver.title)
driver.quit()

# JOIN BASIC AND BONUS EXPERIENCE
for i in range(len(df)):
    if len(df.loc[i, 'Experience'].split(' ')) > 1:
        df.loc[i, 'Experience' ] = int(df.loc[i, 'Experience' ].split(" ")[0]) + int(df.loc[i, 'Experience' ].split(" ")[1])  
    else:
        pass

print(df.to_string(), '\n')
# ---------------- Third Part of the Script ------------------------------------------------------------------
# df.loc[ 0 , 'Experience' ]
# print(len(df.columns))
# print(df.loc[df['A'] == 'foo'])
# df['Position'].str.contains("PG") 
# df['Status'].str.count("Failed").sum()
# df['Status'].str.count("Success").sum()
# VISUALIZATION 2
# GIT
# ANSIBLE
# PUPPET
# DOCKER
# browser.save_screenshot('C:\\Users\\grayson\\Downloads\\headless_chrome_test.png')

# SHOW DevOps TOOLS TASKS
for i in ['Ansible' , 'Docker', 'Puppet', 'Git']:
    print(i, df["Name"].str.count(i).sum(), '\n', df[df["Name"].str.contains(i)], '\n')


# CREATE PIE CHART 
labels = "Completed", "Failed", "Pending"
sizes = [df['Status'].str.count("Success").sum(), df['Status'].str.count("Failed").sum(), df['Status'].str.count("Pending").sum()]
colors = ['green', 'red', 'lightskyblue']
explode = (0, 0.15, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=30)
plt.axis('equal')
plt.title('Kode Kloud Enginer Tasks Statistics') 
plt.show()

