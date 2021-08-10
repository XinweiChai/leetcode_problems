# ********************************************************************
# Copyright (c) Microsoft Corporation.  All rights reserved.
# ********************************************************************

import os.path
import sys


class JoinPathCommand:
    '''A command that adds the parent and child parts of a path together
       with the appropriate path separator.'''

    @staticmethod
    def Main(args):
        Path = None
        ChildPath = ''
        Resolve = False
        p = 1
        while p < len(args):
            if args[p] == '-Path' or args[p] == '-ChildPath':
                pass
            elif args[p] == '-Resolve':
                Resolve = True
            elif args[p - 1] == '-Path':
                Path = args[p]
            elif args[p - 1] == '-ChildPath':
                ChildPath = []
                while p < len(args) and args[p][0] != '-':
                    ChildPath.append(args[p])
                    p += 1
            p += 1
        if Path == None:
            raise Exception('Parameter is missing.')
        JoinPathCommand.ProcessRecord(Path.split(','), ChildPath, Resolve)

    @staticmethod
    def ProcessRecord(Path, ChildPath, Resolve):
        '''Parses the specified path and returns the portion determined by the 
           boolean parameters.'''
        for path in Path:
            joinedPath = os.path.join(path, *ChildPath)
            joinedPath = joinedPath.replace('\\', '/')
            if Resolve:
                resolvedPaths = os.path.normpath(joinedPath)
                print(resolvedPaths)
            else:
                print(joinedPath)


if __name__ == "__main__":
    JoinPathCommand.Main(sys.argv)
