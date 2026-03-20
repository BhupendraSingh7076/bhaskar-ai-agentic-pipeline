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

This implementation uses an external LLM via the OpenRouter API as an equivalent to the Anthropic SDK mentioned in the assignment.

The decomposition and synthesis steps are powered by the LLM, using the prompts defined in `system_prompt.txt` and `user_prompt_template.txt`. 

The answer step is intentionally implemented as a mock tool, as per the assignment requirements, to simulate tool-based responses and demonstrate how the pipeline would integrate external tools in a real-world system.

This setup reflects a realistic agentic workflow with clear separation between LLM reasoning and tool execution.
