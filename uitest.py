import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_notes_can_be_created():
    # Arrange
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/notes/add/')

    # Act
    driver.find_element(By.NAME, 'title').send_keys('Django Course')
    driver.find_element(By.NAME, 'description').send_keys(
        'Complete course with urls, templates, models, etc')
    driver.find_element(By.NAME, 'submit').click()
    time.sleep(2)  # Bad but easy

    # Assert
    title = driver.find_element(By.TAG_NAME, 'td').text
    assert 'Django Course' in title

    driver.quit()
    
# def test_error_occurs():
#     driver = webdriver.Chrome()
#     driver.get("http://127.0.0.1:8000/notes/")
    
#     driver.find_element(By.NAME, "title").send_keys('Test Note')
#     driver.find_element(By.NAME, "description").send_keys('des')
#     driver.find_element(By.NAME, 'submit').click()
#     time.sleep(2)
    
#     error = driver.find_element(By.CLASS_NAME, "error").text
    
#     assert error == "Description must be at least 10 characters long."
#     driver.quit()