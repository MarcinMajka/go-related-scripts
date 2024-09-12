import argparse
import os

def print_sgf(sgf_path):
    with open(sgf_path, 'r') as file:
        sgf = file.read()
        print(os.path.basename(sgf_path))
        print(sgf)
        print("")
        

def main(root_dir):
    files = os.listdir(root_dir)
    files = [os.path.join(root_dir, f) for f in files if f.endswith('.sgf')]
    for f in files:
        print_sgf(f)
    return
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser('parser')
    parser.add_argument('--root_dir')
    args = parser.parse_args()
    main(args.root_dir)