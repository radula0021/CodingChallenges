import os
import subprocess

def run_tests(directories):
    for directory in directories:
        print(f"Testing directory: {directory}")
        
        # Ensure the directory exists
        if not os.path.exists(directory):
            print(f"Directory {directory} does not exist.")
            continue
        
        # Loop through all files in the directory
        for filename in os.listdir(directory):
            # Construct the full file path
            filepath = os.path.join(directory, filename)
            
            # Ensure it's a file (not a subdirectory)
            if os.path.isfile(filepath):
                print(f"Testing file: {filename}")
                
                # Run the json_parser.py script on the file using subprocess
                result = subprocess.run(['python', 'jsonParser.py', filepath], capture_output=True, text=True)
                
                # Print the output from json_parser.py
                output = result.stdout.strip()  # Get the output from stdout
                error = result.stderr.strip()   # Get the output from stderr
                
                # Print the output
                if output:
                    print(output)
                if error:
                    print(f"Error: {error}")

if __name__ == "__main__":
    # Directories containing the test files
    test_directories = ['./tests/step1/', './tests/step2/']
    
    # Run the tests on the specified directories
    run_tests(test_directories)

