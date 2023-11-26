import sys

import renaming_func as renf
import argparse


def main(arguments: argparse.Namespace):
    curr_dir = renf.DirectoryWorking.get_curr_dir()

    if arguments.delimiter == '/' or arguments.delimiter == '\\':
        print('You cannot use symbol ' + arguments.delimiter + ' as a delimiter')
        sys.exit(1)

    if curr_dir != '/' and '.' not in curr_dir:
        if arguments.action == 'rename':
            renf.DirectoryWorking.renaming_files_in_dir(curr_dir, arguments.beginVal,
                                                        arguments.prefix, arguments.delimiter)
        elif arguments.action == 'undo':
            renf.DirectoryWorking.undo_renaming_in_dir(curr_dir, arguments.prefix, arguments.delimiter)
    else:
        print('Seems like you should not rename files in this system directory!')
        sys.exit(1)


if __name__ == "__main__":
    parseArg = argparse.ArgumentParser(prog='rnmdir', description='Rename files by integer sequence in some directory')

    parseArg.add_argument('--action', '-A', choices=['rename', 'undo'], required=True,
                          help='Rename all files in current directory OR undo previous sequence renaming ')
    parseArg.add_argument('--delimiter', '-D', nargs='?', type=str, action='store',
                          const='. ', default='. ',
                          help='Delimiter for renamed files prefix and sequence values')
    parseArg.add_argument('--beginVal', '-B', nargs='?', action='store', type=int,
                          const=1, default=1,
                          help='Begin value for rename sequence')
    parseArg.add_argument('--prefix', '-P', action='store', nargs='?', type=str,
                          const='', default='',
                          help='Prefix for renamed files. Will be placed before each sequence value')

    args = parseArg.parse_args()
    print(args)

    main(args)