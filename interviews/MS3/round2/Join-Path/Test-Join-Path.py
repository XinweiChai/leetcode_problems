from subprocess import Popen, PIPE
import difflib

def check(cmd, expectedOutput):
    process = Popen(cmd.split(' '), stdout=PIPE)
    (output, error) = process.communicate()
    exit_code = process.wait()
    if exit_code != 0:
        print(error)
    elif output == expectedOutput:
        print('Pass')
    else:
        print('Failure. Diff:\n' + ''.join(difflib.ndiff(expectedOutput.splitlines(1), output.splitlines(1))))

if __name__ == '__main__':
    # '''It should output multiple paths when called with multiple -Path targets'''
    check('python Join-Path.py -Path TestDrive1:,TestDrive2: -ChildPath SubDir1 -Resolve',
          b'TestDrive1:/SubDir1\r\nTestDrive2:/SubDir1\r\n')
    """It should be able to join-path special string 'Variable:' with 'foo'"""
    check('python Join-Path.py -Path Variable: -ChildPath foo',
          b'Variable:/foo\r\n')
    """It should be able to join-path special string 'Alias:' with 'foo1' and 'foo2'"""
    check('python Join-Path.py -Path Alias: -ChildPath foo1 foo2',
          b'Alias:/foo1/foo2\r\n')
