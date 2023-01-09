
from pathlib import Path

import os
import sys



FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


print('파일 경로: ' + str(FILE))
# print('Root 경로: ' + str(ROOT))
print('Root parent: ' + str(FILE.parents[0]))
print(FILE.parent)
print(FILE.parents)

for i in FILE.parents:
    print(i)