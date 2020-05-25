"""
Author: DracoY

# main.py
The main file to run Text Analyzer v04.
"""

from engine import *

def main():
    app = Engine()
    
    app.infile()
    app.outfile()
    app.run_animation()
    app.console_end()


if __name__ == "__main__":
    main()
