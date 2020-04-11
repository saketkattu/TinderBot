from selenium import webdriver
from time import sleep

#Enter your phone number here 
phone="9108672547"
class TinderBot:
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="/home/saket/Desktop/projects/TinderBot/chromedriver_linux64/chromedriver")
        
 
    
    def getOTP(self):
        otp=input("Enter you OTP")
        ar=[int(x) for x in str(otp)]
        return ar
    
    def login(self):
        self.driver.get("https://tinder.com")

        phone_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/button')
        phone_btn.click()

        phone_txt=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        phone_txt.send_keys(phone)

        

        
        for i in range(0,5):
            o=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{}]'.format(i+1))
            ar1=self.getOTP()
            o.send_keys(ar1[i])

        cont=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        cont.click()

        sleep(3)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
    
    def right(self):
        like=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()
    
    def left(self):
        dislike=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike.click()

    
    def autoswipe(self):
        while True:
            sleep(0.5)
            try:
                self.right()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
    
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()




        






        








        
    

  


