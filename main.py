import curses
from curses.textpad import Textbox, rectangle
from database import DatabaseRead, DatabaseWrite
from utils import parse


class GetText:
    def get_tag(self):
        tag = curses.wrapper(self.get_text_with_box, "tag")
        return tag

    def get_title(self):
        title = curses.wrapper(self.get_text_with_box, "title")
        return title

    def get_desc(self):
        desc = curses.wrapper(self.get_text_with_box, "desc")
        return desc

    def get_text_with_box(self, stdscr, message):
        stdscr.clear()
        stdscr.addstr(0, 0, message)
        # Set rectangle
        editwin = curses.newwin(5, 30, 2, 1)
        rectangle(stdscr, 1, 0, 1+5+1, 1+30+1)
        stdscr.refresh()
        # Make box
        box = Textbox(editwin)
        # Let the user edit until Ctrl-G is struck.
        box.edit()
        # Get resulting contents
        data = box.gather()
        return data


class Note:
    def __init__(self, args):
        self.args = args
        self.get_text = GetText()

    def get_atts(self):
        self.tag = (
            self.args.g if self.args.g is not None
            else self.get_text.get_tag()
        )
        self.title = (
            self.args.t if self.args.t is not None
            else self.get_text.get_title()
        )
        self.desc = (
            self.args.d if self.args.d is not None
            else self.get_text.get_desc()
        )

    def get_note(self):
        return (self.tag, self.title, self.desc)


if __name__ == "__main__":
    args = parse()
    if args.s:
        search = DatabaseRead()
        a = search.read_all()
        for x in a:
            print(x)

    else:
        note = Note(args)
        note.get_atts()
        my_note = note.get_note()
        tag, title, desc = my_note
        write = DatabaseWrite(tag, title, desc)
        write.add_note()
