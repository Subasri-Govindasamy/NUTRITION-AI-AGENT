# NUTRITION-AI-AGENT
The Smartest AI Nutrition Assistant, an interactive virtual assistant powered by Generative AI, Natural Language Processing (NLP), and multimodal capabilities
🥗 Nutrient Recipe Agent

This project demonstrates how to integrate **IBM Watsonx.ai**, **LangChain**, and multiple AI tools (like Google Search, Wikipedia, WebCrawler, Weather) using a structured agent approach for context-aware AI-powered applications.

---

📂 Project Structure

```
├── watsonx_agent_service.py   # Main logic for generating Watsonx AI responses  
├── test_api.py                          # Test script for scoring using IBM Cloud Deployment  
├── requirements.txt               # Required Python libraries  
└── README.md                   # You're here!
```

---

🧠 Features

- 🤖 AI agent powered by `mistralai/mistral-large`
- 🔍 Tool integrations: RAG (document retrieval), GoogleSearch, DuckDuckGo, Wikipedia, WebCrawler, and Weather
- 🧩 LangChain + IBM Watsonx agent setup using `create_react_agent`
- 📡 Streaming and standard response generation supported

---
Setup Instruction
1. Install dependencies

```bash
pip install -r requirements.txt
```

---

2.Set your IBM Cloud credentials in the code

In `test_api.py`, replace with your own:

```python
API_KEY = "<your IBM Cloud API key>"
```

In `watsonx_agent_service.py`, replace with your values:

```python
params = {
    "space_id": "your_space_id",
    "vector_index_id": "your_vector_index_id"
}
```

> ⚠️ **Important:** Do NOT share your real API key or space ID in public repositories.

---

 3. Run the test script

```bash
python test_api.py
```

This sends a test payload to your Watsonx AI deployment and prints the scored response.

---

Example Payload (in `test_api.py`)

```python
payload_scoring = {
    "messages": [
        {
            "role": "user",
            "content": "Tell me about the recent advancements in AI"
        }
    ]
}
```

---

📄 requirements.txt (example)

```txt
ibm-watsonx-ai
langchain_ibm
langchain
langgraph
requests
```

---

Created By

**Subasri G**  
Feel free to connect for collaborations or feedback!

---

