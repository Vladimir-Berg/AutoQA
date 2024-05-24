from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()

    for item in l:
        print(item)
    print(len(l))

finally:
    pass  #db.destroy()


all_phones = ["wer", "werww", "dfgdg" + '\n' +
                              "cbcbcv", "xcvxcv", "dfgdfg"]
print(all_phones)
print([p.split('\n') for p in all_phones])