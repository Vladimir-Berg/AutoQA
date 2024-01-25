import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_add_group(app):
    app.session.login("admin", "secret")
    app.create_new_group(Group("Group", "Header", "Comment"))
    app.session.logout()
    app.driver.close()
