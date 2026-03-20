import os
import requests


# CONFIG (OpenRouter API)
MODEL = "meta-llama/llama-3-8b-instruct"


# LLM CALL FUNCTION (Equivalent to Anthropic)
def call_llm(system_prompt, user_prompt):
    API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not API_KEY:
        print("❌ API key not found. Please set OPENROUTER_API_KEY.")
        return None

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost",
        "X-Title": "agentic-pipeline-assignment"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" not in result:
            print("⚠ API Error:", result)
            return None

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("⚠ Request failed:", str(e))
        return None


# Step 1: Decompose Topic (LLM)
def decompose_topic(topic):
    try:
        with open("prompts/system_prompt.txt", "r") as f:
            system_prompt = f.read()

        with open("prompts/user_prompt_template.txt", "r") as f:
            user_template = f.read()
    except Exception as e:
        print("⚠ Error loading prompt files:", str(e))
        return []

    user_prompt = user_template.replace("{topic}", topic)

    response = call_llm(system_prompt, user_prompt)

    # Handle bad LLM output
    if not response:
        return ["Error generating sub-questions"]

    questions = [
        q.split(".", 1)[-1].strip()
        for q in response.split("\n")
        if q.strip()
    ]

    # Edge case: empty or too few questions
    if len(questions) < 3:
        print("⚠ Warning: LLM returned insufficient questions")
        return ["Error generating sub-questions"]

    return questions


# Step 2: Mock Tool
def mock_answer_tool(question):
    if "future" in question.lower():
        return "[UNCERTAIN] Future trends are evolving and may vary across sources."

    return "This can be explained based on general knowledge and commonly observed examples."


# Step 3: Answer Questions
def answer_questions(questions):
    answers = []
    flagged = []

    for q in questions:
        ans = mock_answer_tool(q)
        answers.append((q, ans))

        if "[UNCERTAIN]" in ans:
            flagged.append(q)

    return answers, flagged


# Step 4: Synthesis (LLM)
def synthesize(topic, qa_pairs):
    system_prompt = "You are a helpful research assistant."

    context = "\n".join([f"{q} {a}" for q, a in qa_pairs])

    user_prompt = f"""
Using the following information, generate:
1. A title
2. A 150-word summary

Topic: "{topic}"

Data:
{context}
"""

    response = call_llm(system_prompt, user_prompt)

    # Handle failure
    if not response:
        return "Error generating final summary."

    return response


# Main Pipeline
def run_pipeline(topic):
    # ✅ Empty topic handling
    if not topic.strip():
        print("❌ Please enter a valid topic.")
        return

    print(f"\nTopic: {topic}\n")

    # Step 1: Decompose
    questions = decompose_topic(topic)

    print("Sub-Questions:")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q}")

    # Step 2 & 3: Answer
    qa_pairs, flagged = answer_questions(questions)

    print("\nAnswers:")
    for q, a in qa_pairs:
        print(f"\nQ: {q}\nA: {a}")

    # Step 4: Synthesize
    final_output = synthesize(topic, qa_pairs)

    print("\nFinal Output:\n")
    print(final_output)

    # Low confidence flag
    if flagged:
        print("\n⚠ Low Confidence Questions:")
        for q in flagged:
            print(f"- {q}")


# Run
if __name__ == "__main__":
    topic = input("Enter a Topic: ")
    run_pipeline(topic)
