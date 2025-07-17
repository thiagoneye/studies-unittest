import unittest
from unittest import mock
from email_client import EmailClient, EmailSender


class TestEmailSender(unittest.TestCase):
    def test_send_emails(self):
        # Mocking the EmailClient object
        email_client = mock.MagicMock(spec=EmailClient)

        # Creating a list of recipients
        recipients = [
            "recipient1@example.com",
            "recipient2@example.com",
        ]

        # Creating an EmailSender instance
        email_sender = EmailSender(email_client)
        email_sender.send_emails(recipients, "Test email", "This is a test email")

        # Asserting that the was called twice with the correct arguments
        email_client.send_email.assert_has_calls(
            [
                mock.call(
                    "recipient1@example.com",
                    "Test email",
                    "This is a test email",
                ),
                mock.call(
                    "recipient2@example.com",
                    "Test email",
                    "This is a test email",
                ),
            ]
        )
