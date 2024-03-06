import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + '' * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_of_direct(prefix, maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_of_months(prefix):
    symbols = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
    return random.choice(symbols)


testdata = [Contact(firstname='', middlename='', lastname='', nickname='', company='', address='',
                    homephone='', mobilephone='', workphone='', email1='', email2='', email3='',
                    bday='', bmonth='', byear='')] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       company=random_string("company", 10), address=random_string("address", 20),
                       homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10, ),
                       workphone=random_string("workphone", 10), email1=random_string("email1", 10),
                       email2=random_string("email2", 10), email3=random_string("email3", 20),
                       bday=str(random_string_of_direct("bday", 2)), bmonth=random_string_of_months("bmonth"),
                       byear=random_string_of_direct("byear", 4)
                       )
               for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))
