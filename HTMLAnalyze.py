import sys
import os

from antlr4 import *

from HTMLLexer              import HTMLLexer
from HTMLParser             import HTMLParser
from HTMLAnalyzeListener    import HTMLAnalyzeListener

DEFAULT_FILE_NAME = '.\work\output.csv'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1], encoding = 'ansi')
        file_name, file_ext = os.path.splitext(sys.argv[1])
        output_file = file_name + '.csv'
    else:
        input_stream = InputStream(sys.stdin.readline())
        output_file = DEFAULT_FILE_NAME
    
    lexer = HTMLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = HTMLParser(tokens)
    tree = parser.htmlDocument()

    listener = HTMLAnalyzeListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    f = open(output_file, 'w')
    out_stream = listener.getCSV(tree)
    f.write(out_stream)
    f.close()
