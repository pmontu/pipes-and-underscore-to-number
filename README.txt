Input
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

Output
123456789

Illegible Input
    _  _     _  _  _  _  _ 
  | _| _||_| _ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _ 

Output
1234?678? ILL

python main_solution.py

Runs solution for user stories 1,2,3 with set of entries stored in input files.
Generated output is tested with expected output present in output files.

Ambivalent Digit
Example 1
Input 
 _ 
|_|
 _|

Output
Valid resolution by single change of pipe or underscore 
 _ 
|_|
|_|
 _ 
 _|
 _|
 _ 
|_ 
 _|

Example 2
Input
   
 _|
  |

Output
   
|_|
  |
   
  |
  |

python digit_permutations_over_a_pipe_and_underscore.py
