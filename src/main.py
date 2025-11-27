# def main():
#     print("Hello from mcp-server!")



def test_tool_call():
    from langchain.tools import tool

    @tool
    def get_weather(location: str) -> str:
        """Get the weather at a location."""
        return f"It's sunny in {location}."

    def initialize_llm():
        from llms import initialize_multiple_models
        chat_completion_model_params = [
        {"name": "gpt-4o", "type": "chat"}
        ]
        chat_completion_models_dict = initialize_multiple_models(
            model_specs=chat_completion_model_params
        )
        return chat_completion_models_dict["gpt-4o"]



    
    model = initialize_llm()

    model_with_tools = model.bind_tools([get_weather])  

    response = model_with_tools.invoke("What's the weather like in Boston?")
    for tool_call in response.tool_calls:
        # View tool calls made by the model
        print(f"Tool: {tool_call['name']}")
        print(f"Args: {tool_call['args']}")



if __name__ == "__main__":
    test_tool_call()
