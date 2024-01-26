import pytest
import time
from model.contact import Contact
from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_addcontact(app):
    app.session.login("admin", "secret")
    app.contact.create(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "//option[. = '26']",
                "//option[. = 'September']", 2000, "//option[. = 'Group2']"))
    time.sleep(4)
    app.session.logout()
