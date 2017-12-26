import pickle
import argparse
import getpass

from passlib.hash import bcrypt
from random import shuffle

parser = argparse.ArgumentParser(description='Password Trainer, Marek Mateusz Narozniak', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--add', nargs=1, metavar=('label'), type=str, default=None, help='add new password')
parser.add_argument('--remove', nargs=1, metavar=('label'), type=str, default=None, help='remove password')
parser.add_argument('--test', action='store_true', help='test your memory')
args = parser.parse_args()

db = None
try:
    db = pickle.load(open('db.p', 'rb'))
except (OSError, IOError) as e:
    db = {}
    pickle.dump(db, open('db.p', 'wb'))

if args.add is not None :
    label = args.add[0]
    if label in db :
        raise ValueError('This label already exists, remove it first')
    else :
        p = getpass.getpass()
        h = bcrypt.hash(p)
        db[label] = h
        pickle.dump(db, open('db.p', 'wb'))
        print label + ' added succesfully'

if args.remove is not None :
    label = args.add[0]
    if label not in db :
        raise ValueError('This label is not in the database')
    else :
        del db[label]
        pickle.dump(db, open('db.p', 'wb'))
        print label + ' removed succesfully'

if args.test :
    drill = []
    for label in db :
        drill.append(tuple([label, db[label]]))
    shuffle(drill)
    total = len(drill)
    for i, (l, h) in enumerate(drill) :
        done = False
        while not done :
            print str(i+1) + '/' + str(total)
            print l
            p = getpass.getpass()
            done = bcrypt.verify(p, h)
    print 'congratulations!'
