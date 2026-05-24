## code review
I usually approach code reviews in multiple layers instead of just checking whether the code works.

First, I try to understand the business requirement or user story. Then I review whether the implementation actually solves the requirement in the simplest and most maintainable way.

After that, I review technical aspects like:

1. readability and naming conventions
2. component reusability
performance impacts
edge case handling
API/error handling
security concerns
unit test coverage
coding standards followed by the team

For frontend applications, I also check things like unnecessary re-renders, state management usage, accessibility, responsive behavior, and whether the logic can be modularized better.

I try not to give vague comments like ‘improve this’. Instead, I give actionable suggestions with reasoning. For example, I may suggest extracting repeated logic into a custom hook or utility function to improve maintainability.

If the PR is large, I usually review it in smaller logical sections instead of reviewing everything at once.

I also appreciate good implementations during reviews because code review should feel collaborative rather than fault-finding.

For critical changes, I sometimes pull the branch locally and test the flows myself before approving.
