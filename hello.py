import argparse
name = argparse.ArgumentParser()
name.add_argument("--name")
arg = name.parse_args()
print(f'bonjour {arg.name}')
