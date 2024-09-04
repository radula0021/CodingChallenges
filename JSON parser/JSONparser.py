import re
import sys

# Define token types for a simple JSON object '{}'
TOKEN_TYPES = {
    'LBRACE': r'{',
    'RBRACE': r'}',
    'WHITESPACE': r'\s+'
}

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.pos = 0

    def tokenize(self):
        while self.pos < len(self.text):
            match = None
            for token_type, pattern in TOKEN_TYPES.items():
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    if token_type != 'WHITESPACE':  # Skip whitespace
                        token = (token_type, match.group(0))
                        self.tokens.append(token)
                    self.pos = match.end(0)
                    break
            if not match:
                raise SyntaxError(f"Unexpected character: {self.text[self.pos]}")
        return self.tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        try:
            if self.tokens[self.pos][0] == 'LBRACE':
                self.pos += 1  # Skip '{'
                if self.tokens[self.pos][0] == 'RBRACE':
                    self.pos += 1  # Skip '}'
                    if self.pos == len(self.tokens):
                        return True
            raise SyntaxError("Invalid JSON structure")
        except (IndexError, SyntaxError) as e:
            return False

def main():
     # Get the file path from the command line argument
    if len(sys.argv) != 2:
        print("Usage: python jsonParser.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    try:
        with open(file_path, 'r') as file:
            json_text = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

    lexer = Lexer(json_text)
    
    try:
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        is_valid = parser.parse()
        
        if is_valid:
            print("File is in JSON format")
            sys.exit(0)
        else:
            print("This is not JSON format")
            sys.exit(1)
    
    except SyntaxError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
