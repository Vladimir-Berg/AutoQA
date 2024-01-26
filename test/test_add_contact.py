import pytest
import time
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_addcontact(app):
    app.session.login("admin", "secret")
    app.contact.creeate_contact(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "//option[. = '26']",
                "//option[. = 'September']", 2000, "//option[. = 'Group']"))
    time.sleep(4)
    app.session.logout()
