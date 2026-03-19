
# Step 1: Decompose topic (Mock LLM)
def decompose_topic(topic):
    """
    Simulated LLM response using prompt logic
    """
    # Simple rule-based decomposition (mock behavior)
    return [
        f"What is {topic} and what defines it?",
        f"What are the main types or categories of {topic}?",
        f"How is {topic} used in real-world or cultural contexts?",
        f"What are the challenges and future trends related to {topic}?"
    ]


# Step 2: Mock tool (answer generator)
def mock_answer_tool(question):
    """
    Simulates a tool call returning answers
    """
    if "future" in question.lower():
        return "[UNCERTAIN] Future trends are evolving and may vary across sources."
    
    return "This can be explained based on general knowledge and commonly observed examples."



# Step 3: Answer all questions
def answer_questions(questions):
    answers = []
    flagged = []

    for q in questions:
        ans = mock_answer_tool(q)
        answers.append((q, ans))

        if "[UNCERTAIN]" in ans:
            flagged.append(q)

    return answers, flagged


# Step 4: Synthesis (Mock LLM)
def synthesize(qa_pairs, topic):
    """
    Simulated summary generation
    """
    summary = f"{topic.title()} are important subjects with various aspects including definition, types, applications, and challenges. "

    summary += "They play a significant role in cultural and practical contexts. "

    summary += "While they have strong traditional or functional value, they also face challenges and evolving future trends. "

    summary += "Understanding these aspects helps in gaining a complete overview of the topic."

    return f"Title: {topic.title()}\n\nSummary:\n{summary}"


# Main pipeline
def run_pipeline(topic):
    print(f"\nTopic: {topic}\n")

    questions = decompose_topic(topic)

    print("Sub-Questions:")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q}")

    qa_pairs, flagged = answer_questions(questions)

    print("\nAnswers:")
    for q, a in qa_pairs:
        print(f"\nQ: {q}\nA: {a}")

    final_output = synthesize(qa_pairs, topic)

    print("\nFinal Output:\n")
    print(final_output)

    if flagged:
        print("\n⚠ Low Confidence Questions:")
        for q in flagged:
            print(f"- {q}")


# Run
if __name__ == "__main__":
    topic = "Indian classical dance forms"
    run_pipeline(topic)
