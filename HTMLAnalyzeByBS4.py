import optparse

from bs4 import BeautifulSoup

class InputStream:
    def __init__(self, input_file, active_page):
        self.stream = ''
        
class HTMLAnalyze:
    def __init__(self, input_stream, parser):
        self.__soup = BeautifulSoup(input_stream, parser)
        
    def getNameValByTag(self, tag_name):
        return []    

if __name__ == '__main__':
    # Parse options
    usage = "Usage: %prog [-i input_filename] [-a] [-o output_filename]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-i', '--input',
                      dest="input_file",
                      default="",
                      help='set html source file name'
                      )
    parser.add_option('-a', '--active',
                      dest="active_page",
                      default=False,
                      action='store_true',
                      help='get html source of current active page'
                      )
    parser.add_option('-o', '--output',
                      dest="output_file",
                      default="output.csv",
                      help='set output file name'
                      )
    options, remainder = parser.parse_args()
    if not options.input_file and not options.active_page:
        print('ERROR: You have to provide input file name or set to active page!')
        parser.print_help()
        exit(1)

    # Get html source
    inputStream = InputStream(options.input_file, options.active_page).stream
    
    # Get infomation from html source
    analyzer = HTMLAnalyze(inputStream, 'lxml')
    pairs = analyzer.getNameValByTag('input')
    
    # Output infomation
    outStream = 'name,value\n'
    for data in pairs:
        outStream += data[0] + ',' + data[1] + '\n'
    f = open(options.output_file, 'w')
    f.write(out_stream)
    f.close()
    