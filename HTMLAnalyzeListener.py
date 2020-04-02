from antlr4                     import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from HTMLParserListener         import HTMLParserListener
from HTMLParser                 import HTMLParser
from HTMLLexer                  import HTMLLexer


class HTMLAnalyzeListener(HTMLParserListener):

    # need rewriter to change token stream
    def __init__(self, tokens:TokenStream):
        self.tokens = tokens
        self.rewriter = TokenStreamRewriter(tokens)
                    