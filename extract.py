import sys
import patoolib
import argparse
from patoolib.util import log_error, log_internal_error, PatoolError

#patoolib.extract_archive("archivedFiles.7z", outdir="S:tmp")

def checkArgument():
    
    parser = argparse.ArgumentParser()    
    parser.add_argument('--sourcefile', help="File location of archived file")
    parser.add_argument('--dest', help="file system location where unarchived files will be written to.")   
    return parser
    

def ExtractFiles(args):
    print("Extracting files\n\n")
    print("Archived File: " + args.sourcefile)
    print("Output File Location: " + args.dest)
    print("\n\n")
    patoolib.extract_archive(args.sourcefile, outdir=args.dest)




def main():

    try:
        argparser = checkArgument()
        args = argparser.parse_args()
      
        if (args.sourcefile == None or args.dest == None):
           argparser.error("\ntoo few arguments")
        else:
            ExtractFiles(args)

    except KeyboardInterrupt:
        log_error("aborted")
        
    except Exception:
        log_internal_error()


if __name__ == '__main__':
    main()
