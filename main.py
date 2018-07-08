import csv
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui


application_id = ''
password = ''
applicant_index = 0

def fill_text(id, value):
    box = driver.find_element_by_id(id)
    box.clear()
    box.send_keys(value)

def parse_date(value):
    return datetime.strptime(value, '%d/%m/%y')

def handle_trip(trip, driver):
    if trip['done'] == 'x':
        return

    driver.find_element_by_css_selector("input[type='radio'][value='true']").click()
    driver.find_element_by_css_selector("input[type='submit']").click()
    assert 'Details of trips outside the UK' in driver.page_source

    depart_date = parse_date(trip['depart'])
    return_date = parse_date(trip['return'])

    fill_text('countryVisited_ui', trip['destination'])
    fill_text('reasonForTrip', trip['reason'])
    fill_text('departureDateOfTrip_day', depart_date.day)
    fill_text('departureDateOfTrip_month', depart_date.month)
    fill_text('departureDateOfTrip_year', depart_date.year)
    fill_text('returnDateOfTrip_day', return_date.day)
    fill_text('returnDateOfTrip_month', return_date.month)
    fill_text('returnDateOfTrip_year', return_date.year)
    fill_text('totalDaysAbsent', trip['days'])

    # YOLO/auto-accept mode
    #driver.find_element_by_css_selector("input[type='submit']").click()

    wait = ui.WebDriverWait(driver, 600)
    wait.until(lambda driver: 'Additional trips outside the UK' in driver.page_source)


driver = webdriver.Chrome()
driver.get('https://visas-immigration.service.gov.uk/resume/' + application_id)
assert 'UK visa application' in driver.title

fill_text('password', password)
driver.find_element_by_css_selector("input[type='submit']").click()
assert 'All applicants' in driver.page_source

driver.find_elements_by_partial_link_text('Answer questions')[applicant_index].click()
assert 'outside the UK' in driver.page_source

with open('trips.csv', newline='') as csvfile:
    trips = csv.DictReader(csvfile)

    #handle_trip(trips.__next__(), driver)

    for trip in trips:
        handle_trip(trip, driver)

#driver.close()