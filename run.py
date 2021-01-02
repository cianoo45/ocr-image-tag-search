import argparse
import sys
import glob
from ocr import tag_image,search_for_image



def parse_args():
    '''
    Parse command line arguments for plot customization
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', dest='mode', help='Mode select, Options are: "tag", "search" ', required=True)
    parser.add_argument('-f', '--files', dest='files',  nargs='?', const='',
                        help='List of files to tag, Seperated by ";", Leave blank for all files in the images/ folder',
                        required=False)
    parser.add_argument('-s', '--search', dest='search', help='Search keyword to search images for', required=False)
    args = parser.parse_args(sys.argv[1:])

    if args.mode == "tag" and args.files is None:
        print("Tag mode selected but -f command not provided")
        return None
    elif args.mode == "search" and args.search is None:
        print("Search Mode selected but -s command not provided")
        return None
    elif args.files is not None and args.search is not None:
        print("-f and -s can not both be entered")
        return None

    return args


def main(args):
    if args.mode == "tag" and args.files == "":
        fileList = glob.glob("images/*")
        tag_image(fileList)
        print("All Images Tagged Succesfully")
    elif args.mode == "tag" and args.files != "":
        fileList = args.files.split(";")
        tag_image(fileList)
        print("All Images Tagged Succesfully")
    elif args.mode == "search":
        print("Searching for word '{0}' in tagged-images folder".format(args.search))
        search_for_image(args.search)




if __name__ == "__main__":
    parsed_args = parse_args()
    if parsed_args:
        main(parsed_args)
