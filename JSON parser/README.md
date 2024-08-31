# JSON PARSER

### The goal is to handle very simple JSON objects like {} and correctly identify valid and invalid JSON, returning the appropriate exit code.

## Explanation:
- **Lexer**: The lexer is simplified to handle just the curly braces {} and whitespace.
- **Parser**: The parser checks for the exact structure {} and reports if it finds anything else as invalid.
- **Exit Codes**: The script exits with 0 for valid JSON and 1 for invalid JSON.
- **File Handling**: The script reads a JSON file, making it easier to test with different inputs.
## Testing:
- Valid JSON: {} should print "Valid JSON" and exit with code 0.
- Invalid JSON: Any other content should print "Invalid JSON" and exit with code 1.
