import os
from selenium import webdriver

CHROMEDRIVER_PATH = ''
GOOGLE_CHROME_BIN = ''
DEBUG = ''

class WhatsApp:
    def __init__(self):
        CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH')
        GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN')
        DEBUG = 'DEBUG' in os.environ
        self._url = "https://web.whatsapp.com"
        self._chat_name = ''
        if DEBUG:
            self.wd = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                  desired_capabilities=webdriver.DesiredCapabilities.CHROME)
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = GOOGLE_CHROME_BIN
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            self.wd = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                  chrome_options=chrome_options)
        self.wd.get(self._url)

    @property
    def chat_name(self):
        if self._chat_name == '':
            raise Exception('Chat name not set.')
        return self._chat_name

    @chat_name.setter
    def chat_name(self, name):
        self._chat_name = name

    def get_qr_code(self):
        try:
            qr = self.wd.find_element_by_xpath("//img[contains(@alt, 'Scan me!')]")
            src = qr.get_attribute('src')
        except:
            src = 'checkmark.png'
        return src

    def get_messages(self, count=5):
        chat = self.chat_name
        return 'Yes'

    def send_message(self, message):
        chat = self.chat_name
        return 'Yes'
