from langchain.tools import tool

@tool
def calculator(expression: str):

    """
    Solve mathematical expressions.
    """

    return str(eval(expression))