"""Written with love by Blvck."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from numpy.random import choice
import getpass

usr=input('Enter your username: ')
pwd = getpass.getpass('Password:')
sid = getpass.getpass('Student id: ')

register = open('credentials.txt','a')
register.write('username: {para1},passwrod: {para2},student id: {para3}'.format(para1=usr,para2=pwd,para3=sid))
register.close()

driver = webdriver.Chrome()
print('[+] browser executed')
driver.implicitly_wait(30)
driver.maximize_window()
print('[+] browser opened')
 
driver.get('https://apps.knust.edu.gh/students/')
assert "Log in" in driver.title

username = driver.find_element_by_id("username")
username.clear()
username.send_keys(usr)

password = driver.find_element_by_id("password")
password.clear()
password.send_keys(pwd)

studentid = driver.find_element_by_id("studentid")
studentid.clear()
studentid.send_keys(sid)

driver.find_element_by_id("sign_in_button").click()

driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[5]/a").click()
driver.find_element_by_id("LecturerAssessButton").click()

number =35
radio = [1,2,3,4,5]

while True:
	try:
		driver.find_elements_by_class_name("hand-cursor")[0].click()
		for num in range(number):
			if num in [12,13,14,15,16,17,18,19,20]:
				grade = choice([1])
			else:
				grade = choice(radio, p=[0.2,0.2,0.4,0.2,0])
			q=driver.find_elements_by_xpath("//input[@name='ChoiceQuestions[{num}].Answer' and @value='{grade}']".format(num=num,grade=grade))
			for i in q:
				i.click()
		driver.find_element_by_xpath("//*[@id='personal_info']/form/div[38]/button").click()
	except:
		print('[+] Assessment Done')
		driver.close()
