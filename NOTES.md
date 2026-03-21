### Design Notes

This pipeline is designed to clearly separate reasoning and execution. I used an LLM for the decomposition step because it can intelligently break a broad topic into focused sub-questions. The answer step is implemented as a mock tool to simulate external tool usage, as required by the assignment, and to demonstrate how agentic systems integrate tools. 

Prompts are stored in separate files to keep the system modular and easy to update without changing code. 

The pipeline can handle any user-provided topic dynamically, making it flexible and reusable. Basic edge case handling is included, such as checking for empty input and handling API failures or invalid LLM responses. 

This design keeps the system simple, readable, and aligned with real-world agentic workflows.


### Reflection

The weakest part of this pipeline is the answer step, which uses a mock tool that returns templated responses instead of generating detailed answers.

If I had more time, I would replace it with a real data source or API and add retry logic for LLM calls.

A potential failure mode is inconsistent LLM output formatting. In production, this could be handled with validation and retry mechanisms.
