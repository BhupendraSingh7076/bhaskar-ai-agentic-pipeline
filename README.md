# Agentic AI Pipeline Assignment

This project implements a simple agentic pipeline that processes a topic through three stages: decomposition, answering, and synthesis.

---

## Overview

Given a topic, the system:

1. Breaks it into 3–5 focused sub-questions (using LLM)
2. Generates short answers using a mock tool
3. Synthesizes the results into a final summary with a title (using LLM)
4. Flags low-confidence outputs (`[UNCERTAIN]`)

---

## Pipeline Flow

Topic → Decompose → Answer → Synthesize → Final Output

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install requests


2. Set API Key (OpenRouter)

Get your free API key from: https://openrouter.ai

Windows (CMD):
set OPENROUTER_API_KEY=your_api_key_here
PowerShell:
$env:OPENROUTER_API_KEY="your_api_key_here"
Mac/Linux:
export OPENROUTER_API_KEY=your_api_key_here


Project Structure
project/
│
├── pipeline.py
├── sample_output.txt
├── README.md
├── NOTES.md
└── prompts/
    ├── system_prompt.txt
    └── user_prompt_template.txt
