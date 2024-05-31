from collections.abc import Callable
from typing import Any

from email.message import EmailMessage


def extract_content(
    capitalized_emails: dict[str, Callable[[], EmailMessage]]
) -> dict[str, Callable[[], str]]:
    for partition_id, partition_load_func in capitalized_emails.items():
        yield {partition_id: partition_load_func().get_content()}


def tokenize(contents: dict[str, str]) -> dict[str, Any]:
    for partition_id, partition_data in contents.items():
        yield {partition_id: partition_data.split()}
