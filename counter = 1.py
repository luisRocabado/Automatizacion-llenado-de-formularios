from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# Configuración de opciones de Chrome para ignorar errores SSL y abrir en modo incógnito
options = webdriver.ChromeOptions()
options.add_argument("-incognito")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')

# Inicializar el servicio y el navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Navegar a la página web deseada
try:
    driver.get('https://docs.google.com/forms/d/1i9liVf0HezKuw5vICgBWcHgUHLSSWOiSWzIjWQme4fk/viewform?ts=66e9f4f6&edit_requested=true')
except Exception as e:
    print(f"Error navegando a la página: {e}")
    driver.quit()
    exit()

# Configura WebDriverWait
wait = WebDriverWait(driver, 10)

# Función para desplazarse a un elemento y hacer clic
def scroll_and_click(element):
    try:
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    except Exception as e:
        print(f"Error interactuando con el elemento: {e}")

# Método para seleccionar una opción aleatoria de un grupo de radio buttons
def seleccionar_opcion_aleatoria(pregunta_selector):
    try:
        opciones = driver.find_elements(By.CSS_SELECTOR, pregunta_selector + ' div[role="radio"]')
        if opciones:
            opcion_aleatoria = random.choice(opciones)
            opcion_aleatoria.click()
        else:
            print(f"No se encontraron opciones para la pregunta con el selector: {pregunta_selector}")
    except Exception as e:
        print(f"Error seleccionando opción aleatoria: {e}")

# Aplicación para las preguntas que has mostrado
seleccionar_opcion_aleatoria('div[aria-labelledby="i1"]')  # Ajusta el ID según el formulario
seleccionar_opcion_aleatoria('div[aria-labelledby="i18"]') 
seleccionar_opcion_aleatoria('div[aria-labelledby="i28"]')
seleccionar_opcion_aleatoria('div[aria-labelledby="i38"]')
seleccionar_opcion_aleatoria('div[aria-labelledby="i57"]')
seleccionar_opcion_aleatoria('div[aria-labelledby="i84"]')
seleccionar_opcion_aleatoria('div[aria-labelledby="i111"]')
seleccionar_opcion_aleatoria('div[aria-labelledby="i127"]')
seleccionar_opcion_aleatoria('div[aria-labelledby="i143"]')
seleccionar_opcion_aleatoria('div[aria-labelledby="i80"]')
seleccionar_opcion_aleatoria('div[aria-labelledby="i153"]')

# Función para seleccionar varias opciones aleatorias de checkboxes
def seleccionar_opciones_aleatorias(selector_checkboxes, num_opciones=None):
    try:
        checkboxes = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector_checkboxes))
        )
        if num_opciones is None:
            num_opciones = random.randint(1, len(checkboxes))
        opciones_seleccionadas = random.sample(checkboxes, num_opciones)
        for opcion in opciones_seleccionadas:
            opcion.click()
        print(f"{num_opciones} opción(es) seleccionada(s) correctamente")
    except Exception as e:
        print(f"Error seleccionando opciones: {e}")

# Llamar a las funciones para completar el formulario
seleccionar_opciones_aleatorias(".uVccjd.aiSeRd", num_opciones=2)  # Checkboxes
seleccionar_opciones_aleatorias(".uVccjd.aiSeRd.FXLARc.wGQFbe.BJHAP", num_opciones=3)  # Checkboxes

# Método para seleccionar una opción aleatoria de cada fila en una cuadrícula
def seleccionar_opciones_cuadricula(pregunta_selector):
    try:
        grupos_filas = driver.find_elements(By.CSS_SELECTOR, pregunta_selector + ' .lLfZXe[role="radiogroup"]')
        for grupo_fila in grupos_filas:
            opciones = grupo_fila.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
            if opciones:
                opcion_aleatoria = random.choice(opciones)
                opcion_aleatoria.click()
                print(f"Seleccionada la opción: {opcion_aleatoria.get_attribute('aria-label')}")
            else:
                print("No se encontraron opciones en la fila.")
        print("Se han seleccionado opciones en todas las filas de la cuadrícula.")
    except Exception as e:
        print(f"Error seleccionando opciones en la cuadrícula: {e}")

# Aplicación para la pregunta tipo cuadrícula que has mostrado
seleccionar_opciones_cuadricula('div[aria-labelledby="i76"]')  # Ajusta el ID según el formulario

# Abre el menú desplegable
try:
    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ry3kXd .MocG8c[aria-selected="true"]')))
    dropdown.click()
    print("Menú desplegable abierto correctamente.")
    
    time.sleep(2)  # Espera para que se carguen las opciones del menú desplegable

    # Localiza todas las opciones del menú desplegable
    opciones_distrito = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ry3kXd .MocG8c[aria-selected="false"]'))
    )

    if opciones_distrito:
        print("Opciones encontradas:")
        for opcion in opciones_distrito:
            print(opcion.text)

        # Selecciona una opción aleatoria del menú desplegable
        opcion_aleatoria = random.choice(opciones_distrito)

        # Usa ActionChains para asegurarse de que el clic sea preciso
        actions = ActionChains(driver)
        actions.move_to_element(opcion_aleatoria).click().perform()
        
        print(f"Se seleccionó correctamente la opción: {opcion_aleatoria.text}")
    else:
        print("No se encontraron opciones en el menú desplegable.")
        
except Exception as e:
    print(f"Ocurrió un error al interactuar con el menú desplegable: {e}")
# Intentar encontrar el botón de enviar y hacer clic
try:
    # Asegurarse de que el botón de enviar esté presente y se pueda hacer clic
    boton_enviar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd'))
    )
    boton_enviar.click()
    print("Formulario enviado correctamente.")
    
except Exception as e:
    print(f"Error interactuando con el botón de enviar: {e}")
# Cerrar el navegador
driver.quit()
