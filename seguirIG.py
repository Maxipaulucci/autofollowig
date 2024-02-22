from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

"""
To use this code you have to install one python framework: selenium. To install it you have to write in the terminal the word "pip" (without the ""), then the word "install" (again without the "") and finally the name of the framework, so you have to write in the terminal: pip install selenium.
"""

#--------------------------------------------------------------------------------------------------------------
# Inicialización de variables
#--------------------------------------------------------------------------------------------------------------
pathDatos = "(path of the file with the username, the password and the name of the person you want to follow, inside these "")"
pathNavegador = "(path of your navigator web inside these "", in my case the path is: C:/Program Files/Google/Chrome/Application/chrome.exe)"

#--------------------------------------------------------------------------------------------------------------
# Codigo
#--------------------------------------------------------------------------------------------------------------

options = Options()
options.add_argument("--incognito")  # Buscador se corre en incognito

#Cargar opciones al driver
driver = webdriver.Chrome(options=options)

#Acceder a instagram
driver.get("https://www.instagram.com")
sleep(2)

#Buscamos los campos para iniciar sesion
usernameInput = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
passswordInput = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

#Buscar datos para el inicio de sesion
try:
    datos = open(pathDatos, mode = "r", encoding = "utf-8")

    lineas = datos.readlines()

    if len(lineas) == 3:
        usuario = lineas[0].strip("\n").split(" ")[1]
        password = lineas[1].strip("\n").split(" ")[1]
    else:
        print("Error: El archivo no tiene la estructura esperada.")

except (OSError, FileNotFoundError) as detalle:
    print(f"Error: {detalle}")
finally:
    try:
        datos.close()
    except:
        pass

#Insertar datos en los campos correspondientes para iniciar sesion
usernameInput.send_keys(usuario)
passswordInput.send_keys(password)
sleep(1)

#Tocar boton
loginButton = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
loginButton.click()
sleep(5)

#Tocar ahora no del guardado de informacion
notNow_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
notNow_button.click()

#Tocar ahora no de activar notificaciones
notNow_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
notNow_button.click()

#Tocar busqueda
searchUser_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div')
searchUser_button.click()

#Buscar en el archivo de texto el nombre de usuario de la persona que desea seguir
seguir = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
try:
    datos = open(pathDatos, mode = "r", encoding = "utf-8")

    lineas = datos.readlines()

    if len(lineas) == 3:
        persona = lineas[2].strip("\n").split(" ")[1]
    else:
        print("Error: El archivo no tiene la estructura esperada.")

except (OSError, FileNotFoundError) as detalle:
    print(f"Error: {detalle}")
finally:
    try:
        datos.close()
    except:
        pass

#Cargar en la busqueda la persona que desea seguir
seguir.send_keys(persona)
sleep(2)

#Tocar la persona buscada
personButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div')
personButton.click()
sleep(4)

#Seguir a la persona en caso de tener una cuenta publica
try:
    followButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
    followButton.click()
    sleep(5)
#Si la cuenta es privada tendra un boton diferente en el codigo
except NoSuchElementException:
    followButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button')
    followButton.click()
    sleep(5)