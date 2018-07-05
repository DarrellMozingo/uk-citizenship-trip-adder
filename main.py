from selenium import webdriver
from selenium.webdriver.common.keys import Keys


application_id = ''
password = ''
person_index = 0

def fill_text(id, value):
    box = driver.find_element_by_id(id)
    box.clear()
    box.send_keys(value)

driver = webdriver.Chrome()
driver.get('https://visas-immigration.service.gov.uk/resume/' + application_id)
assert 'UK visa application' in driver.title

fill_text('password', password)
driver.find_element_by_css_selector("input[type='submit']").click()
assert 'All applicants' in driver.page_source

driver.find_elements_by_partial_link_text('Answer questions')[person_index].click()
assert 'Additional trips outside the UK' in driver.page_source

# loop here

driver.find_element_by_css_selector("input[type='radio'][value='true']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
assert 'Details of trips outside the UK' in driver.page_source

fill_text('countryVisited_ui', 'Ireland')
fill_text('reasonForTrip', 'Holiday')
fill_text('departureDateOfTrip_day', '19')
fill_text('departureDateOfTrip_month', '09')
fill_text('departureDateOfTrip_year', '2013')
fill_text('returnDateOfTrip_day', '23')
fill_text('returnDateOfTrip_month', '09')
fill_text('returnDateOfTrip_year', '2013')
fill_text('totalDaysAbsent', '4')
#driver.find_element_by_css_selector("input[type='submit']").click()
#assert 'Additional trips outside the UK' in driver.page_source

#driver.close()