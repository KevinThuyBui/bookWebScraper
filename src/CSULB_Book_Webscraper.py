from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def main():
    textbook_url = "https://www.fortyninershops.net/buy_courselisting.asp"
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    click_timeout = 1

    driver = webdriver.Chrome(executable_path='C:/Users/Sinat/Desktop/WebScraping/chromedriver', chrome_options=option)

    driver.get(textbook_url)

    selTerm_field_options = getFieldOptions(driver, 'selTerm')

    for term in selTerm_field_options:
        term.click()
        wait_for_selection(driver, click_timeout, "fDept")
        selDept_field_options = getFieldOptions(driver, 'selDept')

        for department in selDept_field_options:
            department.click()
            wait_for_selection(driver, click_timeout, "fCourse")
            selCourse_field_options = getFieldOptions(driver, 'selCourse')

            for course in selCourse_field_options:
                course.click()

                wait_for_selection(driver, click_timeout, "fSection",)
                selSection_field_options = getFieldOptions(driver, 'selSection')

                for section in selSection_field_options:
                    section.click()

                    try:
                        WebDriverWait(driver, click_timeout)\
                            .until(EC.presence_of_element_located((By.XPATH, "//*[@class='book-meta book-isbn']")))
                    except TimeoutException:
                        print("Timed out waiting for Textbook")
                    textbook_table_elements = driver.find_elements_by_xpath("//*[@class='book-meta book-isbn']")
                    print(textbook_table_elements)

def wait_for_selection(driver, click_timeout, select_id):
    try:
        WebDriverWait(driver, click_timeout).until(EC.element_to_be_clickable((By.ID, select_id)))
    except TimeoutException:
        print("Timed out waiting for %s" %select_id)


def getFieldOptions(driver, select_name):

        select_field = driver.find_element_by_xpath("//select[@name='%s']" %select_name)
        select_field_options = select_field.find_elements_by_tag_name("option")
        return select_field_options


if __name__ == '__main__':
    main()
