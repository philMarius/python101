'''Learning about python emailing'''

import smtplib

HOST = "mySMTP.server.com"
SUBJECT = "Test email from Python"
TO = "mike@someAddress.org"
FROM = "python@mydomain.com"
TEXT = "Python 3.5 rules them all"

BODY = "\n".join((
  "From: %{FROM}s",
  "To: %{TO}s",
  "Subject: %{SUBJECT}s",
  "",
  TEXT
))

SERVER = smtplib.SMTP(HOST)
SERVER.sendmail(FROM, [TO], BODY)
SERVER.quit()
