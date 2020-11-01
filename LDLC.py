import sys
from selenium import webdriver

from User import User
from Card import Card

productURL = sys.argv[1:][0]

# Remplir les données pour la carte #
cardNumber = input("Saisissez votre numéro de carte : ")
cardName = input("Saisissez votre prénom et nom : ")
cardExpireDate = input("Saisissez la date d'expiration de votre carte : ")
cardCryptogram = input("Saisissez le cryptogramme situé sur la face arrière de la carte : ")
card = Card.Card(cardNumber, cardName, cardExpireDate, cardCryptogram)

# Remplir les données pour la connexion #
email = input("Saisissez votre mail :")
password = input("Saisissez votre mot de passe : ")
user = User.User(email, password, card)

driver = webdriver.Firefox(executable_path="D:\Geckodriver\geckodriver.exe")

# Connexion #
driver.get("https://secure2.ldlc.com/fr-fr/Login/Login")
driver.find_element_by_id("Email").send_keys(user.email)
driver.find_element_by_name("Password").send_keys(user.password)
driver.find_element_by_xpath("/html/body/div[3]/div/form/button").click()

# Achat du produit #
driver.get(productURL)
driver.find_element_by_class_name("add-to-cart-oneclic").click()

# URL du paiement #
driver.get("https://secure2.ldlc.com/fr-fr/DeliveryPayment")
element = driver.find_element_by_id("SelectedDeliveryModeId370001")
driver.execute_script("arguments[0].setAttribute('checked','checked')", element)
driver.find_element_by_id("deliveryModeClassicSelectionForm").submit()
driver.implicitly_wait(3)
driver.switch_to.frame(driver.find_element_by_css_selector("[id^=hipay-hosted-cardNumber]"))
driver.find_element_by_name("cardnumber").send_keys(card.cardNumber)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_css_selector("[id^=hipay-hosted-expiryDate]"))
driver.find_element_by_name("cc-exp").send_keys(card.cardExpireDate)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_css_selector("[id^=hipay-hosted-cardHolder]"))
driver.find_element_by_name("ccname").send_keys(card.cardName)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_css_selector("[id^=hipay-hosted-cvc]"))
driver.find_element_by_name("cvc").send_keys(card.cardCryptogram)
driver.switch_to.default_content()
#driver.switch_to.frame(driver.find_element_by_css_selector("[id^=hipay-hosted-cardNumber]"))
#driver.find_element_by_xpath("/html/body/div/div/div/form")

# driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[1]/div/div/form/div[9]/div/button").click() #