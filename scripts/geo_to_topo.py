# -*- coding: utf-8 -*-
import sys, getopt, json

def converter_geo(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'converter_geo.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'converter_geo.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print 'Input file > ', inputfile
    with open(inputfile) as f:
        geojson = json.load(f)
    topojson = conversion.convert(geojson)
    with open(outputfile, 'w') as fp:
        json.dump(topojson, fp)

    print 'Output file > ', outputfile
    print 'Done.'

if __name__ == "__main__":
    if __package__ is None:
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from topojson import conversion
    converter_geo(sys.argv[1:])