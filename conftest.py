
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", # set 'english' by default!!
                     help="Choose language")
    parser.addoption('--link', action='store',
                     default="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
                     help="Check link")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    lang = request.config.getoption("language")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    return language

@pytest.fixture(scope="function")
def link(request):
    link = request.config.getoption("link")
    return link
