from database import DatabaseRead, DatabaseWrite
from utils import parse


args = parse()

if args.s:
    search = DatabaseRead()
    a = search.read_all()
    for x in a:
        print(x)


if args.g == "test":
    write = DatabaseWrite(args.g, args.t, args.d)
    write.add_note()
