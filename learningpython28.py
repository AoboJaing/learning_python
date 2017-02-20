import optparse

def main():
    parser = optparse.OptionParser('usage%prog ' +\
                                   '-f <zipfile> -d <dictionary>')
    parser.add_option('-f', dest='zname', type='string',\
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',\
                      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
        pass
    else:
        zname = options.zname
        dname = options.dname
        dlist = dname.split(',')
        pass
    print('zname is ', zname)
    print('dname is ', dname)
    print('dlist is ', dlist)
    pass

if __name__ == '__main__':
    main()
    pass
