import pytest
import time
from contact import Contact
from application_contact import ApplicationContact


@pytest.fixture
def app_contact(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_addcontact(app_contact):
    app_contact.login("admin", "secret")
    app_contact.creeate_contact(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "//option[. = '26']",
                "//option[. = 'September']", 2000, "//option[. = 'Group']"))
    time.sleep(4)
    app_contact.logout()
