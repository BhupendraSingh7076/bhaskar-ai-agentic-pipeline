### Design Notes

The pipeline is designed as a three-stage agentic workflow: decomposition, answering, and synthesis. The decomposition and synthesis steps use an LLM via OpenRouter (as an equivalent to the Anthropic SDK), while the answering step is implemented as a mock tool to simulate tool-based interactions, as required.

Prompts are stored separately (`system_prompt.txt` and `user_prompt_template.txt`) to ensure modularity and allow easy iteration without changing core logic. The system prompt enforces structure, output format, and edge case handling to improve reliability.

Basic error handling is included for empty inputs, API failures, and invalid LLM responses. Additionally, low-confidence outputs are detected using a simple `[UNCERTAIN]` flag.

This design reflects a realistic separation between reasoning (LLM) and execution (tools), similar to modern agentic systems.



### Reflection

The weakest part of this pipeline is the answer step, which uses a mock tool that returns templated responses instead of generating detailed answers.

If I had more time, I would replace it with a real data source or API and add retry logic for LLM calls.

A potential failure mode is inconsistent LLM output formatting. In production, this could be handled with validation and retry mechanisms.
