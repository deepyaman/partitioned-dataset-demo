from kedro.pipeline import Pipeline, node, pipeline

from .nodes import capitalize_content, generate_emails


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(generate_emails, "params:n", "emails"),
        node(capitalize_content, "emails", "capitalized_emails"),
    ])
