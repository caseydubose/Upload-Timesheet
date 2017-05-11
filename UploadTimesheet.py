from splinter import Browser
import time
import csv

#define variables
timeentry = str('https://na31.salesforce.com/a0M/e')
signin = str('https://login.salesforce.com/')


#Prompt for sign in and database
# print('What is your Username?')
# UserName = input()
# print('What is your Password?')
# Password = input()


#import csv
exampleFile = open('C:\\Users\\U0127576\Dropbox\Programming\Python\Salesforce Timesheet\TimeEntries.csv')
reader = csv.DictReader(exampleFile)
credFile = open('C:\\Users\\U0127576\Dropbox\Programming\Python\Credentials\sfcreds.txt')
cred_lines = credFile.readlines()

#initialize browser
browser = Browser('chrome')

#login
browser.visit('https://login.salesforce.com/')
browser.find_by_id('password').first.fill(cred_lines[1])
browser.find_by_id('username').first.fill(cred_lines[0])
#browser.find_by_id('Login').first.click()

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
    time.sleep(3)
    with open("C:\\Users\\U0127576\Dropbox\Programming\Python\Salesforce Timesheet\TimesheetLog.txt", "a") as myfile:
        myfile.write(row['Project'] + " | " + row['Description'] + " | " + row['Date'])
        myfile.write("\n")


