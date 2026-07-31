# 🤖 Structured Output & Function Calling Chatbot

A Python-based AI chatbot built using the **Groq API** that demonstrates **Native Function Calling**, **Structured JSON Output**, **Pydantic Validation**, and **Intent Detection**.

This project was developed as part of an AI Engineering internship assignment to showcase how Large Language Models (LLMs) can interact with external Python functions and generate validated structured data.

---

# 🚀 Features

✅ Native Function Calling using Groq API

✅ Automatic Intent Detection

✅ Calculator Tool

✅ Current Time Tool

✅ Structured JSON Extraction

✅ Pydantic Schema Validation

✅ Interactive Command Line Chatbot

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Groq API | LLM & Native Function Calling |
| Llama 3.3 70B | Language Model |
| Pydantic | JSON Validation |
| python-dotenv | Environment Variables |
| Email Validator | Email Validation |

---

# 📂 Project Structure

```
structured-output-function-calling/
│
├── app.py                 # Main chatbot
├── tools.py               # Calculator & Time tools
├── schemas.py             # Pydantic schemas
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── examples/
```

---

# ⚙️ How It Works

The chatbot first detects the user's intent.

```
                    User
                      │
                      ▼
             Intent Detection
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Calculator        Current Time      Information
      │               │              Extraction
      ▼               ▼                │
 Python Tool      Python Tool          ▼
                                      JSON
                                       │
                                       ▼
                             Pydantic Validation
```

Depending on the detected intent, the chatbot either:

- Calls a Python calculator function
- Calls a Python function to fetch the current time
- Extracts structured JSON and validates it
- Responds like a normal AI assistant

---

# 🔧 Tool 1 — Calculator

The chatbot automatically detects mathematical questions.

### Example

**Input**

```
Calculate 250 multiplied by 40
```

**Output**

```
Assistant : 10000
```

Supported operations

- Addition
- Subtraction
- Multiplication
- Division

---

# 🕒 Tool 2 — Current Time

The chatbot automatically detects time-related questions.

### Example

**Input**

```
What is the current time?
```

**Output**

```
Assistant : 02:10 PM
```

---

# 📄 Structured Output

The chatbot can extract structured information from natural language.

### Input

```
My name is Harsh Pariya.
I am 20 years old.
My email is harsh@gmail.com.
I know Python, Java, SQL and Machine Learning.
```

### Output

```json
{
  "name": "Harsh Pariya",
  "age": 20,
  "email": "harsh@gmail.com",
  "skills": [
    "Python",
    "Java",
    "SQL",
    "Machine Learning"
  ]
}
```

---

# ✅ Pydantic Validation

After generating JSON, the output is validated using a Pydantic schema.

```python
class Person(BaseModel):
    name: str
    age: int
    email: EmailStr
    skills: List[str]
```

Benefits

- Ensures correct data types
- Validates email format
- Prevents malformed JSON
- Makes AI output reliable

---

# 🧠 Intent Detection

Instead of requiring commands like:

```
extract:
```

the chatbot automatically detects user intent.

Example

```
Calculate 50 + 20
```

↓

Calculator Tool

---

```
What is the current time?
```

↓

Time Tool

---

```
My name is Harsh...
```

↓

Structured Output

---

```
Hello
```

↓

Normal Conversation

---

# 💬 Example Conversation

```
You : Calculate 500 multiplied by 25

Detected Intent : calculator

Assistant : 12500
```

---

```
You : What is the current time?

Detected Intent : time

Assistant : 02:15 PM
```

---

```
You :
My name is Harsh Pariya.
I am 20 years old.
My email is harsh@gmail.com.

Detected Intent : extract

Generated JSON

{
   ...
}

Validation Successful!
```

---

```
You : Hello

Detected Intent : chat

Assistant :
Hello! How can I help you today?
```

---

# 📸 Screenshots

Create an `examples/` folder and add screenshots.

```
examples/
│
├── calculator.png
├── current_time.png
├── structured_output.png
└── chat.png
```

Then display them like this:

```markdown
## Calculator

![Calculator](examples/calculator.png)

## Current Time

![Time](examples/current_time.png)

## Structured Output

![Structured Output](examples/structured_output.png)

## Chat

![Chat](examples/chat.png)
```

---

# 📌 Assignment Requirements Covered

- ✔ Native Function Calling
- ✔ Two Python Tools
- ✔ JSON Tool Schemas
- ✔ Structured JSON Output
- ✔ Pydantic Validation
- ✔ Interactive Chatbot
- ✔ Intent Detection
- ✔ Example Outputs

---



