import uuid
from collections.abc import Callable

from email.message import EmailMessage


def generate_emails(n: int) -> dict[str, EmailMessage]:
    emails = {}

    for _ in range(n):
        string_to_write = "what would you do if you were invisable for one day????"

        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(string_to_write)
        msg["Subject"] = "invisibility"
        msg["From"] = '"sin studly17"'
        msg["To"] = '"strong bad"'

        emails[str(uuid.uuid4())] = msg

    return emails


def capitalize_content(
    emails: dict[str, Callable[[], EmailMessage]]
) -> dict[str, Callable[[], EmailMessage]]:
    capitalized_emails = {}

    for partition_id, partition_load_func in emails.items():

        def _capitalize_content(msg: EmailMessage) -> EmailMessage:
            msg.set_content(msg.get_content().capitalize())

            return msg

        capitalized_emails[partition_id] = lambda: _capitalize_content(
            partition_load_func()
        )

    return capitalized_emails
