# Agentic AI Pipeline Assignment

This project implements a simple agentic pipeline that processes a topic through three stages: decomposition, answering, and synthesis.

## 🚀 Overview

Given a topic, the system:
1. Breaks it into 3–5 focused sub-questions
2. Generates short answers using a mock tool
3. Synthesizes the results into a final summary with a title
4. Flags low-confidence outputs

---

## 🧠 Pipeline Flow

Topic → Decompose → Answer → Synthesize → Final Output


## ⚙️ Setup Instructions

# 1. Install dependencies
pip install anthropic

# 2. Set API Key
Windows:
set ANTHROPIC_API_KEY=your_api_key_here
Mac/Linux:
export ANTHROPIC_API_KEY=your_api_key_here

---

## 📂 Project Structure
