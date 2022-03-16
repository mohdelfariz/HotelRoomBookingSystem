import hashlib
from block import *

def blockexplorer(blockchain):		
		for block in blockchain:
				print(block.index)