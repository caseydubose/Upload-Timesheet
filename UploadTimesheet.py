from splinter import Browser
import time
import csv

# You'll need to install Splinter and Chromium's pack to be able to run Chrome
# However, this should be able to run with Splinter's IE process
# I haven't bothered with relative paths to the files yet so that'll need updates
# as well as you'll need to create a cred file and define the absolute path.

'''
The TimeEntries.csv file that you will use to load your time entries must have the following columns
Project, Date, Time (as a decimal, e.g. 1.2), User, Description, 
Task (must be populated for Non-Billable and Operations items), 
and Service Category (Billable, Non-Billable, Operations)
'''

#define variables
#sfcreds.txt is a two line fine containing UN and Password.
timeentry = str('https://na31.salesforce.com/a0M/e')

signin = str('https://login.salesforce.com/')

exampleFile = open('C:\\Users\\U0127576\Dropbox\Programming\Python\Salesforce Timesheet\TimeEntries.csv')
reader = csv.DictReader(exampleFile)

with open('C:\\Users\\U0127576\Dropbox\Programming\Python\Credentials\sfcreds.txt') as credFile:
    cred_lines = list(credFile)

#initialize browser
browser = Browser('chrome')

#login
browser.visit('https://login.salesforce.com/')
browser.find_by_id('password').first.fill(cred_lines[1])
browser.find_by_id('username').first.fill(cred_lines[0])

#go to timeentry
for row in reader:
    browser.visit(timeentry)
    browser.find_by_id("CF00N37000006A1dD").first.fill(row['Project'])
    browser.find_by_id('00N37000006A1dI').first.fill(row['Date'])
    browser.find_by_id('00N37000006A1dN').first.fill(row['Time'])
    browser.find_by_id('CF00N37000006ADRZ').first.click()
    browser.find_by_id('CF00N37000006ADRZ').first.fill(row['User'])
    browser.find_by_id('00N37000006A1dc').first.fill(row['Description'])
    browser.find_by_id('00N37000006A1dS').first.click()
    ServiceCat = row['Service Category']
    Billable = str('Billable')
    if ServiceCat != Billable:
        browser.find_by_id('00N37000006A1dS').select(ServiceCat)
        browser.find_by_id('00N37000006A1dX').select(row['Task'])
        browser.find_by_name('save').first.click()
    else:
        browser.find_by_id('00N37000006A1dS').select(row['Service Category'])
        browser.find_by_name('save').first.click()
    time.sleep(1)
    with open("C:\\Users\\U0127576\Dropbox\Programming\Python\Salesforce Timesheet\TimesheetLog.txt", "a") as myfile:
        myfile.write('Row #' + str(reader.line_num) + " | " + row['Project'] + " | " + row['Description'] + " | " + row['Date'])
        myfile.write("\n")


