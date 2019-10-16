from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


def random_string_for_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "@._-"
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", nickname="", email="", homephone="", mobilephone="", workphone="",
                    secondaryphone="", email2="", email3="", address="", )] + [
    Contact(firstname=random_string("Kseniya", 10), lastname=random_string("Kurashova", 10),
            nickname=random_string("Kotik", 10), email=random_string_for_email("kot@kot.kot", 5),
            homephone=random_string("123", 10), mobilephone=random_string("456", 10),
            workphone=random_string("789", 10), secondaryphone=random_string("147", 10),
            email2=random_string_for_email("kot2@kot2.kot", 5), email3=random_string_for_email("kot3@kot3.kot", 5),
            address=random_string("Gh12", 10))
    for i in range(3)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))