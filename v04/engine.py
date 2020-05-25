"""
Author: DracoY

# engine.py
The engine for Text Analyzer v04.
"""

import sys
import time

class Engine:
    """
    The App Engine.
    """

    def infile(self):
        """ Get the infile from user and read it. """

        print("Please enter the file to be read...")
        self.infile = input("::> ")

        with open(self.infile) as f:
            self.content = f.read()

        self.content = create(self.content)

    def outfile(self):
        """ Get the outfile from user and generate it. """

        print("Please enter the file to be created...")
        self.outfile = input("::> ")

        with open(self.outfile, "w") as f:
            intro = f"CONCORDANCE for {self.infile}\ncreated using Text Analyzer v04\n"
            f.write(intro + "\n")

            rank = 1
            for info in self.content:
                text = f"#{rank}    '{info[1]}':  {info[0]}"
                f.write(text + "\n")
                rank += 1

            outro = "\nReview to contact in README.txt!\nThe End."
            f.write(outro)

    def console_end(self):
        """ This is the end of console. """
        
        msg = "\r" + "File has been created. Check it out!"
        print(msg)


    def run_animation(self):
        """ Run the animation in the console. """

        msg = "Your file is being created..."
        print(msg)

        i = 0
        while (i < 10):
            for a in ("/-", "|-", "\\-"):
                time.sleep(0.25)
                console_flush(a)
            i += 1


def frequency(text, char):
    """ Counts frequency of a character in a string. """

    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


def console_flush(text):
    """ Flushes the console for animations. """

    sys.stdout.write("\r" + text)
    sys.stdout.flush()

    
def create(text):
    """ Creates the meta list. """

    mega = []
    dup = ["\n", " "]

    for char in text:
        if char not in dup:
            count = frequency(text, char)
            baby = [count, char]

            mega.append(baby)
            dup.append(char)

    mega.sort(reverse=True)
    return mega

