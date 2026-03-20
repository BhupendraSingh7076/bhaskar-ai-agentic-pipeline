# Agentic AI Pipeline Assignment

This project implements a simple agentic pipeline that processes a topic through three stages: decomposition, answering, and synthesis.

## Overview

Given a topic, the system:
1. Breaks it into 3–5 focused sub-questions
2. Generates short answers using a mock tool
3. Synthesizes the results into a final summary with a title
4. Flags low-confidence outputs

---

## Pipeline Flow

Topic → Decompose → Answer → Synthesize → Final Output


## ⚙️ Setup Instructions

#### 1. Install dependencies
pip install anthropic

#### 2. Set API Key
Windows:
set ANTHROPIC_API_KEY=your_api_key_here

Mac/Linux:
export ANTHROPIC_API_KEY=your_api_key_here

---

## 📂 Project Structure
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

### Note on LLM Usage
The assignment suggests using the Anthropic SDK. However, due to API billing requirements, I simulated LLM behavior in the decomposition and synthesis steps.

The prompts designed in Task 1 are intended to be used with an LLM in a real implementation. The current pipeline structure mirrors how the system would function with actual API calls.
