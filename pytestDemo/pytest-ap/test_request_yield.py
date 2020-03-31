import pytest
import smtplib


@pytest.fixture(scope="module")
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.163.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print("finalizing %s (%s)" % (smtp_connection, server))
    smtp_connection.close()


smtpserver = "mail.python.org"  # will be read by smtp fixture


def test_showhelo(smtp_connection):

    assert 0, smtp_connection.helo()


if __name__ == '__main__':
    pytest.main()

