def check_whether_clarification_needed(requirements, user_story):
    return f"""
# INSTRUCTIONS
As an experienced software engineer, your task is to carefully review the provided user story and determine if you have enough information to implement it precisely based on the project requirements.

Thoroughly analyze the user story and identify any missing, ambiguous, or unclear details that could impact the implementation. Consider the following aspects:

- all the necessary functionalities and behaviors clearly defined
- specific requirements about system integration
- any edge cases or exceptional scenarios to consider
- any specific performance criteria or constraints to consider
- how should the feature integrate with existing systems or components
- any security considerations or requirements

you job is to see which of the above options apply to the user story
NONE or some could apply, depending on the user story context

If any information is missing or unclear, provide a list of specific questions or points that require further clarification from the business owner. Each clarification request should be clear, concise, and directly related to the implementation of the user story.

Make sure the clarifications and questions are ONLY about the content the user story itself vs. other non relevant requiements of the project.

Only share the final set of questions wit no headers, no footers, no explanations, just the questions.
(!) Only if the user story is already complete and no further clarification is needed respond with "No clarification needed."

# PROJECT REQUIREMENTS
{requirements}

# USER STORY
{user_story}

# ENGINEER'S RESPONSE
"""
