#!/usr/bin/env python
import sys
line_period = 10      # line period for input format
start_skip_lines = 0  # lines to be skipted at the beginning
begin_char = 2        # starting chars of each line, e.g., 'B|'
measure_note = '|'    # separator for measures
measure_per_line = 12 # max measure per line
max_char_line = 120   # max num of chars per line

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def read_score():
    if len(sys.argv) < 2:
        print( '''Usage: ./*.py ori_tab.txt''' )
        exit(1)
    infile = sys.argv[1]
    with open(infile) as f:
        content = f.read().splitlines()
    return content

def preprocess_score(content):
    global start_skip_lines, line_period
    prefix = [ content[i][:begin_char] for i in range(start_skip_lines, start_skip_lines + line_period ) ]
    data = [ content[i][begin_char:] for i in range(start_skip_lines, len(content) ) ]
    measures = [''] * line_period
    for i in range(len(data)): 
        curr_len, tot_len = len(data[i]), len(data[ i - (i % line_period) + 2])
        measures[i % line_period] = measures[i % line_period] + data[i].ljust(tot_len)
    pre_len = len(prefix[2])
    prefix = [ pre.ljust(pre_len,'*') for pre in prefix ]
    return prefix, measures

def format_measures(prefix, measures):
    global measure_note, max_char_line, begin_char, measure_per_line
    pos = find( measures[2], measure_note )
    max_char_line -= begin_char
    start, end, rep = 0, 0, 0
    for i in range(len(pos)):
        rep += 1
        if pos[i] - start > max_char_line or rep >= measure_per_line or i == len(pos) - 1: # break line here
            extra_end = pos[i] - start > max_char_line and i == len(pos) - 1
            end = pos[i-1] + 1 if pos[i] - start > max_char_line else pos[i] + 1
            print( "\n".join( [prefix[j] + measures[j][start:end] for j in range(len(measures)) ] ) )
            rep, start = 0, end
            if extra_end:       # special treatment when last measure happen to be out of bound
                print( "\n".join( [prefix[j] + measures[j][start:pos[-1]+1] for j in range(len(measures)) ] ) )

def main():
    content = read_score()
    # print titles etc.
    print( "\n".join( content[:start_skip_lines] ) )
    prefix, measures = preprocess_score(content)
    format_measures(prefix, measures)

if __name__ == "__main__":
    main()
