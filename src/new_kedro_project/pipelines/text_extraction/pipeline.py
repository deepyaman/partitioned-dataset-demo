from kedro.pipeline import Pipeline, node, pipeline

from .nodes import extract_content, tokenize


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(extract_content, "capitalized_emails", "contents"),
        node(tokenize, "contents", "tokens"),
    ])
