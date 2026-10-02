# Week 3 Assignment: Grade Reporter & Bug Hunt

## Files

- `grade_reporter.py` - Reports grades, counts passes and failures, and calculates the average.
- `bug_hunt.py` - Fixes three bugs in a while loop program that calculates the sum from 1 to 5.

## Part B Reflection

The hardest bug was the silent logic bug because the program ran without showing an error. I knew something was wrong because the program printed 10 instead of the expected 15. I found that the loop stopped before reaching 5 and changed the operator from `<` to `<=`.