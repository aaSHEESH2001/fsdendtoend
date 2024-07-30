import logging
import os
from datetime import datetime
from pathlib import Path

to_create = f"log/logging.log"

filepath = Path(to_create)

filedir,filename = os.path.split(filepath)

if filedir != '':
    os.makedirs(filedir,exist_ok=True)

if (not os.path.exists(filepath)) or (os.path.getsize() == 0):
    with open(filepath,'w') as f:
        pass
 
else:
    print('file already exist')