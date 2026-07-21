import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('--keyword')
args = parser.parse_args()

pseudo = args.keyword

result = subprocess.run(['echo', pseudo], capture_output = True, text = True)
print(result.stdout)
