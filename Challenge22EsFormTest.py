import customFunc

site = "https://challenge22.com/es/?utm_source=test&utm_medium=test&utm_campaign=test"
sheet = "הרשמה לאתגר 22 - SPANISH"

session = customFunc.webFunc(site)
session.start_driver()
session.url()
customFunc.sleep(6)
session.insert_info_to_field('FirstName', session.first_name)
session.insert_info_to_field('LastName', session.last_name)
session.insert_info_to_field('Email', session.email)
session.insert_info_to_field('Phone', session.phone)
session.ch_confirm_sixteen()
session.send()
session.driver.quit()

customFunc.sleep(600)
session.check_in_sheets(sheet)
