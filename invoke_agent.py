from langgraph_deployment.agent import get_agent

if __name__ == "__main__":
    agent = get_agent()
    prompt = "what is 3*365 and who is president of india?"
    resp = agent.invoke(input={"messages": [{"role": "user", "content": prompt}]})
    print(resp["messages"][-1].content)
