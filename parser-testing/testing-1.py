import argparse

parser = argparse.ArgumentParser(description="Advanced argparse example")
parser.add_argument("--a", type=int, default=5, help="this is an integer argument")
parser.add_argument("--b", type=str, required=True, choices=['x', 'y', 'z'], 
                    help="this argument is required and can only be x, y or z")
parser.add_argument("--c", nargs='*', help="this argument takes a list of values")
parser.add_argument("posarg1", type=int, help="this is a positional argument")
parser.add_argument("posarg2", type=int, help="this is another positional argument")

args = parser.parse_args()

print(args.a)
print(args.b)
print(args.c)
print(args.posarg1)
print(args.posarg2)
