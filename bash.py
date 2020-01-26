#!/usr/bin/env python
import subprocess

'''
Use cat, grep, wc, cut, sort, head and tail to implement the following tasks.
You can use the man page for each command for detailed instructions.

1. A command to count the lines in data/bonds.csv

2. A command to count the number of lines between 2000-2009.
The second column is the year.

3. A command to count the number of lines not between 2000-2009.

4. A command to extract the largest number of games Bonds played in a year.
Games played is column six.

5. A command to extract the distinct teams Bonds played for.
Team is column four.

6. A command to extract the year from the first row in file.
'''

# correct c1..c6 with the right command
c1 = 'cat data/bonds.csv | wc -l'
c2 = "cat data/bonds.csv | wc -l"
c3 = "cat data/bonds.csv | wc -l"
c4 = "cat data/data/bonds.csv | wc -l"
c5 = "cat data/bonds.csv | wc -l"
c6 = "cat data/bonds.csv | wc -l"




def main():
    for c in [c1, c2, c3, c4, c5, c6]:
        print(c)
        print(subprocess.check_output(c, shell=True))


def test_c1():
    out = subprocess.check_output(c1, shell=True)
    assert (out == b'22\n' or out == '22\n')

def test_c2():
    out = subprocess.check_output(c2, shell=True)
    assert (out == b'8\n' or out == '8\n')

def test_c3():
    out = subprocess.check_output(c3, shell=True)
    assert (out == b'14\n' or out == '14\n')

def test_c4():
    out = subprocess.check_output(c4, shell=True)
    assert (out == b'159\n' or out == '159\n')

def test_c5():
    out = subprocess.check_output(c5, shell=True)
    assert (out == b'PIT\nSFN\n' or out == 'PIT\nSFN\n')

def test_c6():
    out = subprocess.check_output(c6, shell=True)
    assert (out == b'1986\n' or out == '1986\n')
    
    
#run main and check tests    
if __name__ == '__main__':
    main()
    print('done')

    try:
        test_c1()
        print("test_c1 passed")
    except:
        print("test_c1 failed")
        
    try:
        test_c2()
        print("test_c2 passed")
    except:
        print("test_c2 failed")
        
    try:
        test_c3()
        print("test_c3 passed")
    except:
        print("test_c3 failed")
        
        
    try:
        test_c4()
        print("test_c4 passed")
    except:
        print("test_c4 failed")
        
        
    try:
        test_c5()
        print("test_c5 passed")
    except:
        print("test_c5 failed")
        
    try:
        test_c6()
        print("test_c6 passed")
    except:
        print("test_c6 failed")
