from agents.research_agent import agent_executor

while True:
    query = input("\nAsk Question: ")

    if query.lower() == "exit":
        break

    response = agent_executor.invoke(
        {"input": query}
    )

    print("\nAnswer:")
    print(response["output"])