# module import
from faker import Faker
from bs4 import BeautifulSoup
from mechanize import Browser

# browser settings
b = Browser()
b.set_handle_robots(False)
b.set_handle_referer(True)
# users input (count of email)
count = int(input('Count of email?\n> ')) # type int

# for loops
for mails in range(count):
    m = Faker('id_ID') # initial Faker locale
    emails = m.email() # generate random emails
    # initial emails server @yahoo.com
    if "@yahoo.com" in emails:
         # browser open for check emails live or not
         b.open('https://login.yahoo.com/')
         b._factory.is_html = True
         b.select_form(nr=0)
         b.form['username'] = emails
         s = BeautifulSoup(b.submit().read(), features = 'html.parser')
         f = s.find('p', class_='error-msg')
         if f == None:
              # output live emails
              print(emails)
