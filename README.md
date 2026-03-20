# Agentic AI Pipeline

This project implements a simple agentic pipeline that processes a topic through three stages: **decomposition → answering → synthesis**.

---

## 🚀 Overview

Given a topic, the system:

1. Breaks it into 3–5 focused sub-questions using an LLM
2. Generates answers using a mock tool
3. Synthesizes the results into a final summary with a title using an LLM
4. Flags low-confidence outputs containing `[UNCERTAIN]`

---

## 🔄 Pipeline Flow

Topic → Decompose → Answer → Synthesize → Final Output

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install requests
```

### 2. Required Libraries

* `os` (built-in)
* `requests`

### 3. Set API Key (OpenRouter)

Get your free API key from: https://openrouter.ai

#### Google Colab

```python
import os
os.environ["OPENROUTER_API_KEY"] = "your_api_key_here"
```

#### Windows (CMD)

```bash
set OPENROUTER_API_KEY=your_api_key_here
```

#### Mac/Linux

```bash
export OPENROUTER_API_KEY=your_api_key_here
```

---

## 🤖 Model & API

* **API Used:** OpenRouter (equivalent to Anthropic SDK)
* **Model Used:** LLaMA (via OpenRouter)

---

## 🧠 Agentic Pipeline

```
User Input (Topic)
        │
        ▼
Decomposition Step (LLM)
- Uses system_prompt.txt
- Uses user_prompt_template.txt
        │
        ▼
Sub-Questions (3–5)
        │
        ▼
Answer Step (Mock Tool)
- Each question processed
- Returns fixed/templated answers
        │
        ▼
Answer Collection
- Store all Q&A pairs
- Detect [UNCERTAIN] responses
        │
        ▼
Synthesis Step (LLM)
- Combines all answers
- Generates Title + Summary
        │
        ▼
Final Output
- Title
- Summary
- ⚠ Low-confidence questions (if any)
```

---

## 📝 Note on LLM Usage

This implementation uses an external LLM via the OpenRouter API as an equivalent to the Anthropic SDK mentioned in the assignment.

The decomposition and synthesis steps are powered by the LLM using structured prompts stored in separate files.

The answer step is intentionally implemented as a mock tool, as required in the assignment, to simulate tool-based responses and demonstrate how external tools would be integrated in a real-world agentic system.

This design reflects a realistic separation between LLM reasoning and tool execution.
