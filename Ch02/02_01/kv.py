"""shelve example"""
import shelve

from moves import move1, move2, move3, move4


db = shelve.open('dance.db')
db['1'] = move1
db['2'] = move2
db['3'] = move3
db['4'] = move4
db.close()

# Go on vacation, ...

db = shelve.open('dance.db')
print(db['1'])
