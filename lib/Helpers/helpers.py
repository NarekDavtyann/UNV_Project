from selenium import webdriver
import logging
import random
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from colorlog import ColoredFormatter


def setup_browser(browser_type="chrome", url=None, maximize_window=True):
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_type.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser_type.lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")

    if url:
        driver.get(url)

    if maximize_window:
        driver.maximize_window()

    return driver


def wait_element_to_be_clickable(driver, by, value):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((by, value)))
    return element


def random_numbers():
    random_number = random.randint(1, 1)
    return str(random_number)


def random_file_name():
    faker_instance = Faker()
    file_name_example = faker_instance.word() + "_" + faker_instance.word()
    return file_name_example


def setup_colored_logger():
    # Set up the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a ColoredFormatter
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)s:%(message)s%(reset)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    # Create a StreamHandler and set the formatter
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger


colored_logger = setup_colored_logger()


def mylogger(text):
    colored_logger.info(text)

