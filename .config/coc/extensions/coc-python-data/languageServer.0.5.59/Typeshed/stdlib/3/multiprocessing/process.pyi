from typing import List
from multiprocessing import Process

def current_process() -> Process: ...
def active_children() -> List[Process]: ...
