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

    def setCSVFromChild(self, ctx):
        value = ''
        if ctx.children:
            for child in ctx.children:
                if child in self.csv.keys():
                    value += self.getCSV(child)
        self.setCSV(ctx, value)

    # Exit a parse tree produced by HTMLParser#htmlAttribute.
    def exitHtmlAttribute(self, ctx:HTMLParser.HtmlAttributeContext):
        value = ''
        attr_name = ctx.htmlAttributeName().getText()
        if ctx.htmlAttributeValue():
            attr_value = ctx.htmlAttributeValue().getText()
            if attr_name.upper() == 'NAME':
                value = attr_value + ','
                self.setCSV(ctx, value)
            elif attr_name.upper() == 'VALUE':
                value = attr_value + '\n'
                self.setCSV(ctx, value)

    # Exit a parse tree produced by HTMLParser#htmlElement.
    def exitHtmlElement(self, ctx:HTMLParser.HtmlElementContext):
        self.setCSVFromChild(ctx)

    # Exit a parse tree produced by HTMLParser#htmlContent.
    def exitHtmlContent(self, ctx:HTMLParser.HtmlContentContext):
        self.setCSVFromChild(ctx)

    # Exit a parse tree produced by HTMLParser#htmlElements.
    def exitHtmlElements(self, ctx:HTMLParser.HtmlElementsContext):
        self.setCSVFromChild(ctx)

    # Exit a parse tree produced by HTMLParser#htmlDocument.
    def exitHtmlDocument(self, ctx:HTMLParser.HtmlDocumentContext):
        self.setCSVFromChild(ctx)
                    