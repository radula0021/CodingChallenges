import sys

def count_bytes(file_path):
    
        with open(file_path, 'rb') as file:
            byte_count = len(file.read())
        return byte_count

def count_lines(file_path):
    
        with open(file_path,'r', encoding='utf-8') as file:
            line_count = 0
            for line in file:
                 line_count += 1
        return line_count

def count_words(file_path):

        with open(file_path,'r', encoding='utf-8') as file:
             word_count = 0
             for line in file:
                  words = line.split()
                  word_count += len(words)
        return word_count

def main():
    option = sys.argv[1]
    file_path = sys.argv[2]

    if option == '-c':
         byte_count = count_bytes(file_path)
         print(f"Number of bytes:{byte_count}")

    elif option == '-l':
        line_count = count_lines(file_path)
        print(f"Number of lines: {line_count}")

    elif option == '-w':
         word_count = count_words(file_path)
         print(f"Number of words in a file: {word_count}")

    else:
        print("Usage: ccwc.py -c|-l|-w <file_path>")

if __name__ == "__main__":
    main()
