import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_add_group(app):
    app.login("admin", "secret")
    app.create_new_group(Group("Group", "Header", "Comment"))
    app.logout()
    app.driver.close()
