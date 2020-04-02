from antlr4                     import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from HTMLParserListener         import HTMLParserListener
from HTMLParser                 import HTMLParser
from HTMLLexer                  import HTMLLexer


class HTMLAnalyzeListener(HTMLParserListener):

    def __init__(self):
        # output area by node
        self.csv = {}

    def getCSV(self, ctx):
        return self.csv[ctx]

    def setCSV(self, ctx, value):
        self.csv[ctx] = value
                    