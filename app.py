from agents.research_agent import agent

print("Agentic RAG Started")
print("Type 'exit' to quit")

while True:

    query = input("\nAsk Question: ")

    if query.lower() == "exit":
        break

    try:

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }
        )

        print("\nAnswer:")

        print(
            response["messages"][-1].content
        )

    except Exception as e:

        print("\nError:")
        print(e)