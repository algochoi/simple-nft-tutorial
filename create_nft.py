import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

sandbox_exec = Path(os.environ['ALGORAND_SECRET'])
print(sandbox_exec)
