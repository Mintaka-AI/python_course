"""The same engineering tool wrapped by a LangChain agent."""
import os

from langchain.agents import create_agent

from engineering_tools import calculate_stress


def main() -> None:
    model_name = os.getenv("OPENAI_MODEL", "gpt-5.6")
    agent = create_agent(
        model=f"openai:{model_name}",
        tools=[calculate_stress],
        system_prompt=(
            "You are an educational engineering assistant. Use tools for every numerical "
            "calculation. Do not guess missing values or units. Explain assumptions and limits."
        ),
    )
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Find the stress for 120000 N acting on 0.0008 m^2.",
                }
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
