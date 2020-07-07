"""Streaming pickle example"""
import pickle
from socket import socketpair

from moves import move1, move2, move3, move4

ws, rs = socketpair()
w, r = ws.makefile('wb'), rs.makefile('rb')

# Serialize
pickle.dump(move1, w)
pickle.dump(move2, w)
pickle.dump(move3, w)
pickle.dump(move4, w)
w.flush()

# De-serialize
for _ in range(4):
    move = pickle.load(r)
    print(f'{move.limb} {move.what}')
