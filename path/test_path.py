import os
from pathlib import Path

path = os.path.abspath('.')
print(f'os.path.abspath: {os.path.abspath(path)}')
print(f'os.path.realpath: {os.path.realpath(path)}')
print(Path())
print(f'os.path.dirname: {os.path.dirname(path)}')
print(f'os.getcwd: {os.getcwd()}')

print(f'Path(__file__): {Path(__file__)}')
print(f'Path(__file__).resolve: {Path(__file__).resolve()}')
print(f'Path(__file__).parent: {Path(__file__).parent}')
print(f'Path(__file__).parents: {Path(__file__).parents}')
print('-----------------------------------------')
print(type(Path(__file__).resolve()))
print(type(Path(__file__)))
print(type(Path(__file__).resolve().parent))
print(Path(__file__).resolve().parent)
