import argparse
import os

def process_sgf(sgf_path):
    with open(sgf_path, 'r') as file:
        sgf = file.read()
    
    parentheses_count = 0
    semicolon_count = 0
    for i, char in enumerate(sgf):
        if char == '(':
            parentheses_count += 1
            if parentheses_count == 3:
                sgf = sgf[:i] + ')'
                break
        elif char == ';':
            semicolon_count += 1
            if semicolon_count == 3:
                sgf = sgf[:i] + ')'
                break
    
    with open(sgf_path, 'w') as file:
        file.write(sgf)
    
    print(f"Processed: {os.path.basename(sgf_path)}")
    print(sgf)
    print("")

def main(root_dir):
    files = [os.path.join(root_dir, f) for f in os.listdir(root_dir) if f.endswith('.sgf')]
    for f in files:
        process_sgf(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('SGF File Processor')
    parser.add_argument('--root_dir', required=True, help='Directory containing SGF files')
    args = parser.parse_args()
    main(args.root_dir)