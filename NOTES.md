I designed the prompt to enforce structure, clarity, and consistency in the decomposition step. The system prompt assigns a clear role ("research planning assistant") and defines strict requirements for sub-questions, including specificity, non-overlap, and coverage of multiple aspects of a topic.

I included a few-shot example to guide the model toward the expected output format and quality. This reduces ambiguity and improves reliability.

Edge cases are explicitly handled to ensure robustness when dealing with broad, unclear, or low-information topics.

The output format is constrained to a numbered list to make downstream parsing in the pipeline simple and predictable.
