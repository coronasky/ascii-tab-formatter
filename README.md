# ASCII Tab Formatter

A simple script to generate printing-friendly ascii guitar tablature.
The script consumes an existing guitar tab (e.g., downloaded from a website), and format the tab to a different length which is easy to print. For example, this tab [BWV1068 Air](https://www.classtab.org/bach_js_bwv1068_suite_no3_in_d_2_air.txt) has 2 measures per line.

```
E||---0-----0-----0-----0-----|--0--5------------------------|
B||---1-----1-----1-----1-----|--1----6-3---0-1-0------------|
G||*--0-----0-----2-----2-----|--2--------5-----0----2-0-----|
D||*--------------------------|-----3---4---0---0------0-----|
A||---3--3--2--2--0--0--------|---------5--------------------|
E||---------------------3--3--|--1----------2---3--3---1--1--|

                                                                   
--3---------3-----0---------3-1-|--1--------0-1---------------1-0-|
------------------------3-2-----|-----3-1-3-----3---3-----1-0-----|
-----3-2-3----3-2---3-2---------|--2--2---2-------0---2-0---------|
-----2---0--0---2---------------|--0--0-----------0---------------|
----------------4---4---0---0---|---------3---3---2---2-----------|
--0-----------------------------|-------------------------3---3---|
                                   _________________________________
                                  | 1                                     
--0--------2-3--------0---------|------------------------------------||
--1--------3---1----3-----3---1-|--0-----0-1----0--------------------||
--0--------0---0--5---0-2---2---|--0-2-2-----2----2-0---------------*||
---------------2--4---------0---|--0---2-----0--0---0-------0-3-2-0-*||
--3--3--2--2---0--0-------------|------3------------2-0-2-3----------||
------------------------2-------|--3------------2---3----------------||
```
When printing the tab, it is a waste of space. Maybe you want to put more measures that fits the width of the paper. 
The script can generate a printing friendly format for the same score.
```
E||---0-----0-----0-----0-----|--0--5------------------------|--3---------3-----0---------3-1-|--1--------0-1---------------1-0-|
B||---1-----1-----1-----1-----|--1----6-3---0-1-0------------|------------------------3-2-----|-----3-1-3-----3---3-----1-0-----|
G||*--0-----0-----2-----2-----|--2--------5-----0----2-0-----|-----3-2-3----3-2---3-2---------|--2--2---2-------0---2-0---------|
D||*--------------------------|-----3---4---0---0------0-----|-----2---0--0---2---------------|--0--0-----------0---------------|
A||---3--3--2--2--0--0--------|---------5--------------------|----------------4---4---0---0---|---------3---3---2---2-----------|
E||---------------------3--3--|--1----------2---3--3---1--1--|--0-----------------------------|-------------------------3---3---|
                                   _________________________________     _________________________                                         
                                  | 1                                   | 2                                                             
--0--------2-3--------0---------|------------------------------------||----------------------------||---------------------3-------0-------|
--1--------3---1----3-----3---1-|--0-----0-1----0--------------------||--0-----0-1----0------------||---0-----0-1-0---0-------2-3---------|
--0--------0---0--5---0-2---2---|--0-2-2-----2----2-0---------------*||--0-2-2-----2----2-0--------||*--0-----0-----2---0---2-3-----2-3---|
---------------2--4---------0---|--0---2-----0--0---0-------0-3-2-0-*||--0---2-----0--0---0--------||*--0-----0---------------2---0---5-3-|
--3--3--2--2---0--0-------------|------3------------2-0-2-3----------||------3------------2--------||---------------------------------5---|
------------------------2-------|--3------------2---3----------------||--3------------2---3--------||---3--3--1-----1-----0---------------|
```
You can copy the output to notepad or Word, choose a monospaced font and print.

## Getting Started

Copy or download formatscoretab.py. Save original score in a text file. 

Modify the beginning of script to set a few options for the score. See below section for the description for each options.

Run the script and redirect output.

`$ python formatscoretab.py score.txt > new_tab.txt`

It should work on both python2 and python3. No extra packages needed.

## User Options
* line_period

   Period for lines in input format, including all extra lines before/after the 6-line score.
* start_skip_lines

   Lines to be skipted at the beginning, for example the title and description.
* begin_char

   Number of common starting chars of each line, e.g., for 'B|' `begin_char = 2`. If there is no common starting char, use 0.
* measure_note

   Separator for measures, usually '|'.
* measure_per_line

   Max number of measures per line.
* max_char_line

   Max number of total chars per line.

It should be noted that both `measure_per_line` and `max_char_line` will be strictly followed. If you want to enable only one, just set the other to a very large number. A measure will not be broken in the middle.

### Optimal number of characters
For portriat orientation of a Letter size paper, taking monospaced font `Courier New` as an example, the `max_char_line` for each font size is listed in the table.

| Font         | `max_char_line`  |
| ------------- |-------------:| 
| 12| 64 | 
| 11| 70 | 
| 10.5| 74 | 
| 10| 77 | 
| 9| 86 | 
| 8| 97 | 
| 7| 111 | 
| 6| 129 | 
| 5| 155 | 

Personnally, size 7-10 is recommended for printing.

## Author
* **Haotian Liu** - [coronasky](https://github.com/coronasky)

## License
This project is licensed under the GNU General Public License v3.0.


