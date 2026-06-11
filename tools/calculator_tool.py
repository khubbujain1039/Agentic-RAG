from langchain.tools import tool

@tool
def calculator(expression: str):

    """
    Perform mathematical calculations.

    Use this tool whenever the user asks
    arithmetic, algebra, percentages,
    multiplication, division, etc.

    Examples:
    - 1+2
    - 45*23
    - 100/4
    """

    return str(eval(expression))