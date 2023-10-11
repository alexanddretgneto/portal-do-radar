import chromedriver_autoinstaller
from selenium import webdriver

# Instala o ChromeDriver, se necessário
chromedriver_autoinstaller.install()

# Agora você pode criar e usar o driver do Selenium
driver = webdriver.Chrome()
