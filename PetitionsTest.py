import customFunc

turkey = "https://animals-now.org/investigations/turkey/?utm_source=test&utm_medium=test&utm_campaign=test"
live_transports = "https://animals-now.org/issues/live-transports/?utm_source=test&utm_medium=test&utm_campaign=test"
cages = "https://animals-now.org/issues/cages/?utm_source=test&utm_medium=test&utm_campaign=test"
protection_act = "https://animals-now.org/issues/animal-protection-act/?utm_source=test&utm_medium=test&utm_campaign=test"
fish = "https://animals-now.org/investigations/fish/?utm_source=test&utm_medium=test&utm_campaign=test"
zoglobek = "https://animals-now.org/issues/zoglobek-lawsuit/?utm_source=test&utm_medium=test&utm_campaign=test"
fur = "https://animals-now.org/issues/fur/?utm_source=test&utm_medium=test&utm_campaign=test"

site_list = [turkey, live_transports, cages, protection_act, fish, zoglobek, fur]

email_list = []  # list with the email used to sign up
petitions_list = []  # list with link to petition that the bot signed up
for site in site_list:  # sign up to petitions in the site list, for each sign up generate new info
    session = customFunc.webFunc(site)
    session.url()
    customFunc.sleep(6)
    session.insertinfo()
    session.petitions_age()
    session.petitions_send()
    email_list.append(session.info[2])
    petitions_list.append(site)
    session.driver.quit()
    customFunc.sleep(30)

customFunc.sleep(240)

session.check_in_gmail(email_list, petitions_list)