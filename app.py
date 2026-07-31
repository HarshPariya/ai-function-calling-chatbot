import os
import json

from dotenv import load_dotenv
from groq import Groq
from pydantic import ValidationError

from tools import calculator, get_current_time
from schemas import Person

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------------------------------------------------
# Tool Schemas
# ---------------------------------------------------------

calculator_tool = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Perform mathematical calculations.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                    "description": "First number"
                },
                "b": {
                    "type": "number",
                    "description": "Second number"
                },
                "operation": {
                    "type": "string",
                    "enum": [
                        "add",
                        "subtract",
                        "multiply",
                        "divide"
                    ]
                }
            },
            "required": [
                "a",
                "b",
                "operation"
            ]
        }
    }
}

time_tool = {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "Returns the current local time.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
}

# ---------------------------------------------------------
# Chat
# ---------------------------------------------------------

print("=" * 60)
print("AI Assistant")
print("=" * 60)

while True:

    user_input = input("\nYou : ")

    if user_input.lower() in ["exit", "quit"]:
        print("\nGoodbye!")
        break

    # ---------------------------------------------------------
    # STEP 1 : Detect Intent
    # ---------------------------------------------------------

    intent_prompt = f"""
You are an intent classifier.

Classify the user's request into ONLY one of these categories.

calculator
time
extract
chat

Return ONLY one word.

User:

{user_input}
"""

    intent_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": intent_prompt
            }
        ]
    )

    intent = intent_response.choices[0].message.content.strip().lower()

    print(f"\nDetected Intent : {intent}")

    # ---------------------------------------------------------
    # STEP 2 : Structured Output
    # ---------------------------------------------------------

    if intent == "extract":

        extraction_prompt = """
Extract the following fields.

Return ONLY valid JSON.

{
"name":"",
"age":0,
"email":"",
"skills":[]
}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            response_format={
                "type": "json_object"
            },
            messages=[
                {
                    "role": "system",
                    "content": extraction_prompt
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        json_output = response.choices[0].message.content

        print("\nGenerated JSON\n")
        print(json_output)

        print("\nValidation\n")

        try:

            person = Person.model_validate_json(json_output)

            print("Validation Successful!\n")

            print(person)

        except ValidationError as e:

            print("Validation Failed!\n")

            print(e)

        continue

    # ---------------------------------------------------------
    # STEP 3 : Tool Calling
    # ---------------------------------------------------------

    if intent in ["calculator", "time"]:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            tools=[
                calculator_tool,
                time_tool
            ],
            tool_choice="auto"
        )

        message = response.choices[0].message

        if message.tool_calls:

            tool_call = message.tool_calls[0]

            function_name = tool_call.function.name

            arguments = json.loads(tool_call.function.arguments)

            if function_name == "calculator":

                result = calculator(
                    arguments["a"],
                    arguments["b"],
                    arguments["operation"]
                )

            elif function_name == "get_current_time":

                result = get_current_time()

            else:

                result = "Unknown Tool"

            print("\nAssistant :", result)

        else:

            print("\nAssistant :", message.content)

        continue

    # ---------------------------------------------------------
    # STEP 4 : Normal Chat
    # ---------------------------------------------------------

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("\nAssistant :", response.choices[0].message.content)