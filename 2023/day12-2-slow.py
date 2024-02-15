from time import time
import re

data = """??#??#????## 2,7
..?##????????.?#?.? 10,2
#??.???..? 1,1,1
#??.#??.??#?#????#?# 2,1,6,3
?.#??.????..?.??? 1,2
#???##?.???#? 2,3,5
?##??#????.??. 2,3,2
??.#??#?????##? 2,1,3,4
?#????#?#.. 2,1,3
?#???#???##?#??? 2,11
#?##??.#??#?? 6,2,1
#.?#????#?#.?? 1,2,5,2
????#?#?#???? 1,6,1,1
.?????.??? 2,1
????????.?#.??? 5,1,1,1
????..???????.??? 1,1
?#???#??#??.????.# 11,1,1,1
???.#?.???#? 2,2,2
???.???.????##? 1,5
??#?#???.#??????#??? 1,5,3,3
???.???.????. 1,2,1,1
????#?...????. 4,1
?.????#??#? 1,7
.?#?.?.##?.?????? 1,3,2,2
????.?????##?.# 3,8,1
????#..????? 1,1,3
.?#???.#????. 1,2,1,2
????.??###.#??.??? 1,1,4,3,1
?????????? 1,1,1
?#.??#...???? 2,1,1
?#????#?????? 7,3
?????.#####??? 1,6
?..?##.#?????? 1,2,4
#??#?#???????????#? 1,4,1,4,1,1
??#??###.???#??. 3,3,3
??????.?#??.?? 3,2
?#???#??#??..?# 6,1,2
#.??.??##?????#?? 1,1,10
.?#???#?.? 2,4
???..????## 2,1,2
??????????????? 1,3,1
??##???????### 1,6,4
?#??????.??? 2,1
??#??????#???? 5,2,2
?#.??#???#?? 2,2,1,1
??#?????#???????. 2,1,1,4
?#?##??#?.. 4,3
##?????#??.??? 9,1,1
??.?...????#???#? 2,9
?????????.? 3,1
.???.??#?.????? 2,4,1
#?##.?#?#????? 4,1,6
????#??#?#??? 1,8
.??.?.###?????? 1,7
??##????#. 4,1,2
???#?.???. 2,1
.?##?##?#?.?#????# 7,3,3
#????..####??.#? 2,1,4,1,1
#..#?#?????#??? 1,9
#.??????.?#??#..???# 1,6,1,1,1,1
???????##?#???#.??? 1,1,5,2,2
?#????.???#? 5,3
#.?#?##??????#?#?? 1,14
.????..?.#???#. 1,1,1,2,1
?#????#???.#????? 8,1,2
????#?.??#??????. 1,3,7
??.??.?.???? 1,1,1,1
??#????..??? 2,1,1,2
?.??#??#??#?.?.???# 10,2
.?#.??#??.? 1,5
?.##????????##?? 4,1,3
.?.??##?#??? 1,6
?????#.??? 1,1,1
.#?#???#???? 4,3,1
????#??.??????? 1,3,1,1,1
???#?.??#?##?# 3,7
?#?#?#???????? 8,1
??.?#????? 1,2
?#???#????.??????? 1,1,3,1,1,1
##???.???.? 3,3
####???????.???? 4,3,1
??#?##??????? 6,3
?..??????? 3,2
.?#??###????#? 8,3
##?###????? 8,1
?.?#?????###??.??#?? 10,1
??????#?????? 3,1,1,1
.#???#?#?.?????? 1,5,1,2,1
???.#???#.??#?#?. 1,2,2,5
..???#????### 1,2,4
????#???#????. 1,7,1
??????#????#.? 3,7,1
???#???????#?...? 4,5,1
#????????##?# 1,3,4
?.#???.???#??. 3,4
.???????.??????.? 4,2,1,3
.?.??.???? 2,2
.???.??????###?#. 3,10
????..?????## 2,1,2,4
#?.???#??.??? 1,4,1
?????..???? 1,4
??????#.????????? 3,1,8
????#??????? 5,1,1,1
????#?#??#????? 1,4,1,2,1
?#?.???#???.? 2,6,1
?.???#??.?#. 1,1,1,1
??.#.#.??????#???? 1,1,1,10
.##?.?????.. 2,2,1
???#?#??#??#??#? 5,1,1,1
?#.?.????????????#? 1,1,10
??#?????.. 3,1
?#.?#?#?????.?????? 1,2,3,1,4,1
?#???..#?.??#?#. 2,1,2,1,1
.????#????.?#?????# 7,1,3
..###??#???#???.??? 10,1,1
??????##?.?#?#.#??# 4,3,2,1,2,1
?.???####.?#?? 4,2
?#.???#???#??##?#?? 1,15
?.?##?#?#? 5,2
?#???#?#??????##??? 9,3
.??????????.??. 6,3,1
???????.#? 1,2,1
????#?#??#?#.. 5,6
?????.?.?#????? 2,1,5
????..??#?#?#??.???? 3,8
#???.?.??????. 1,2,1,2
?????????.???????.?. 1,2,3,4,1
????????##???? 1,7
?.??#.?#??#? 1,1,5
#??????#?##??? 3,9
???#??.?.#?#??### 4,8
?.##??##?#??? 2,7
.?.#?#?????.#?#??.? 1,8,1,1,1,1
?.???#.?????? 2,2
.#.??##???.#??.??. 1,5,3,1
??#???##?? 1,1,4
??????#??##?#. 2,8,1
????#?????.???.?.? 6,1,3
.?.#.?##.??.????#? 1,1,2,2,2,2
.??#?.???? 4,1,1
?.?#?##??##?#??.?? 2,8,1,1
#???##???.??. 1,2,1,1
?#???##??.??#??? 3,3,5
.???#??#??? 1,5,1
?#.?????#???. 2,7
?.???#????????.?. 1,1,1,4,1
??#??#.??#??? 4,1,2
???#.????#???##???? 2,12
..??????.??#??#?? 2,6
??#?.?#?#???..??#?? 3,4,1,1,2
?#????.#?????#?. 2,3,3,3
?????#????.? 2,3,1
.?.?????.?.##.? 5,2
.???.???.???#?? 1,2,3
.????.?#?#???.??. 1,7,2
???#???#??????.. 1,9,1
.#???#?.?? 1,2
##?#??#?##??????#??# 2,7,8
?.?????#????##??.?? 1,8,2,1
??????#.##??##?##?## 3,1,9,2
???#?#?#???#? 1,7,1
???#????.?????? 6,1,1
?.##?#.?#?.?. 1,2,1,2
.????.?..?????? 1,2,1,3,1
?.??????.. 1,1
.?????.?#??. 1,4
???.??????... 2,1
?#?#?#?#.?..#..??? 6,1,1,1,1,1
.??..?#???? 2,1,1
??#?????????#?..??? 10,2,1
?.???.?.?.?.#? 1,2,1,2
#?.?#?.?#???.??????# 2,2,2,1,2,2
????..??####???#?? 4,1,10
.????..??#?? 1,3
.#??#?#?.?.##. 6,2
??#?#..?.??#?#??# 2,1,1,5,1
??##??#??###??..??? 3,7,1,1
????.#.???..??. 1,1,1,1,2
#?.??..??. 1,1,1
.#??????#?.????? 1,5,3,1
?.???#?..??#??? 4,4
?????##?#..#???#?? 7,1,1,1,1,1
?????????? 5,2
????.????.?#?.. 1,1,3
????????????#????#? 4,2,5,4
???#???.??##? 1,1,1,5
?##????????#????##?. 2,7,3
???..??#?? 2,3
#.?#?.???..?? 1,3,3,1
.????????? 2,1,1
???????????##? 6,1,2
?..#????#?? 2,3
????.??..#? 3,1,2
.#.?????#.?#?? 1,2,1,3
????????.?# 7,1
?????#?#??##??#???? 15,2
?#.??.?????#?? 1,1,7
??????#????#?#????? 8,1,7
#..????#???. 1,4,1
##??#.??????. 2,1,2,2
.????.#?#####?. 1,1,7
#????#???..?????? 9,4
???#??.#?.# 3,1,1
.?#?#.?..???? 4,2
??...??.?#?##??? 1,2,8
?.??#?????..???.?.? 5,1,1
?.?##??.?#?##????# 5,5,3
??#?????##??????? 9,1
???#????#? 1,2,2
?.?????????#?#?.?#? 1,3,7,2
???.?#??##?#?? 1,1,5,2
?????.#.?? 3,1,1
?#???#???..??.##??? 2,6,1,5
#??#????????? 2,1,3,1
.#??.?.??.?#. 2,2,1
.???#???????#??##??? 12,2,2
##?#?#???###???????? 13,1,1,1
.?#.??##?????.? 1,3,2,1
#????.???#????. 1,1,3,2
##????????? 2,1,2
?#?..?#????.??? 3,6
.?..??.??#??#?#? 1,1,7
?????????.???.? 1,1,1,2,1
??.????#.???? 1,1,1,2
###?##.??? 6,2
.?#####???????.#??? 5,6,4
.???.??????????? 1,2,1,1,2
?????#?#?#.??#??? 6,1,1,2,1
??.??#???.. 2,1,1
#..?.?.##??. 1,1,3
?##???.?.? 4,1,1
????????##??????.??# 1,10,1,1,1
???#.???.?????? 1,2,1,2,2
????????????.????#? 1,3,3
.?.?????..?#?? 1,1,1,3
?..???##????##? 1,9
.??????#??? 1,2,5
.#?????.?..#???## 1,3,1,1,3
#????.???.? 5,1,1
.?#.?????#??##??? 1,12
???.?#???.?#?? 2,4,4
?.?.??????.?????#?? 1,5,8
???##?#?#?.#. 4,4,1
.#.???.????#????? 1,6
??#?##???#??.????? 9,2
?.?.###??##?#?? 1,11
???.?.???.? 1,1,2
.?#?????#? 3,2
?.??#??#???#?#?## 8,6
???###.?????????? 4,6,1
?.???#???#?## 1,2,2,4
??##??????..???#?? 1,3,3,1,1
.??.#?????#???..?? 1,9,1
...??????? 2,1
???.?###??.????? 3,3,1,1,1
??.?#?..???#????. 2,1,1,3,1
??????..#???.#. 1,4,2,1,1
?.??##?#???##?..???. 11,3
???##?.?##??? 5,4
????.??#?????? 3,7
#??#..?#???#?.? 1,1,2,3,1
????##?#???.?#?# 2,6,4
?#???.##????.? 3,6
.?#????.#????.?.#? 4,1,1,1,2
.??##?#.????#.. 6,3
.#?#??..?? 3,1
#.?.??..??.?? 1,2,1,1
.?????????#???#????? 1,10
?#.#..#?#?#?#????#?? 2,1,3,1,8
??????#????# 6,3
??????..#??#?. 1,1,3
?.??#.??????#?. 1,1,3,1,2
???..##.??##?.????? 1,2,5,2
??????..???# 2,2,1
?????#?.????..?#??#? 4,3,2,3
.??#??????????#??? 11,2,1
??.??..?????.?? 1,1,5,1
#?###?.????????##?? 1,4,9
.?#?#???#??.# 9,1
?????#.??#??#. 1,3,3,1
????#???#??#?.?????. 6,1,2,5
????????.##?# 1,1,2,1
??#?##??????? 8,2
???.???#?#????#??. 1,1,6,2,1
#??.#??????#? 2,1,3,1
.###??.??.? 4,2
?????.??#. 3,1
??????.#..?# 4,1,1,1
?.#??#?.??##?##???? 4,8
??????#?#???? 2,6,1
???..###???..??????? 1,1,4,1,2,1
??..?.???#?? 1,1,1,3
.??#?#????.?.#??#??? 3,1,5
??????.??? 1,1,3
#?.???#??.??#?. 2,5,3
??#??##??.? 6,1
?#?????????#?? 1,10
.????#.??? 4,1
.?###?..?#?#??? 5,5,1
??#??#.?#????.?. 1,1,1,3,1
.???#???#???????? 1,9,1
???..?????? 1,2
??#?.#??##?. 3,2,2
?#?#????.?? 4,2
??#????.##??? 6,4
???#.??.?#?###?.#?? 2,1,6,3
???.?#?##?.? 1,5
?#.?##?.?? 1,4
????###??? 1,4
???##????#?# 1,3,1,3
##???????? 6,2
????#??.####?.? 2,2,1,4,1
#.??#????#???.???? 1,11,1,1
?#??????.? 1,1,1
#..?.?#?.??###??.? 1,1,3,5,1,1
???.??#??#?#?##?? 1,12
??????#??#?##?? 1,2,7
???#???.??.???#? 4,1,5
?????#?????#.?#?#??? 3,1,1,2,5
#??.????#? 3,1,3
???????????...# 8,1
#??#.#.?..????.? 1,1,1,1,4
?#????.??.?. 1,1,2,1
?.??##?.?.???#????.. 5,5
?#??#????.##.## 2,2,2,2,2
?.#????.?? 2,1,1
.#??????????? 1,6
??#.??.#????.??#.??. 2,2,1,1,3,2
??#?#??.??#??? 5,1,2
???#?#??.???.??? 6,2,1
.??#????...?????#.? 6,1,2,1
??.???????.?#??? 2,2,1,4
.?.??????? 1,1,1
.????..??#?#? 2,5
?.?#?##.???.?#??# 1,5,2,1,1
.#??#?.??#?#??.?#??? 2,1,1,5,2,1
?.#??..????#?????#.? 2,10
???#???.?#.???????? 6,1,1,3
?.??#?###??.??##???? 1,8,4,1,1
?????#.??##? 1,2,1,2
..??.##.?.???# 1,2,3
??#?.????#???????? 2,10
?#??????#??.????? 7,1,1,1
#???.?#?.???.??#?? 1,1,2,1,1,5
??##????.#.#?.#?. 6,1,1,1
?#???#??????????.?.? 1,11,1
??#????#???#???. 3,1,8
?#???????.#??? 2,1,2,1
?.#???????.?? 1,1,2
???.????#????#???#? 3,1,4,4,2
????.#??##???#?.### 1,1,6,2,3
??????.?#?#?#?? 2,1,8
.??????.#? 3,1
#??????.????#.????? 1,1,1,2,1,4
???????????????.??# 1,1,7,2
#??.????#?#??.??#?#? 1,7,6
??#?????????## 5,4
????.??#?.. 1,2,4
#?#??.#?#.?? 1,2,3,2
..?#?#?.?#??????#?? 3,1,7
.?????#??###..?#?? 1,6,3
?.#?#????.????###. 1,5,1,1,1,3
?????####?##?.#.??? 10,1,1
.?##???###???. 3,1,6
.??#.?.???.?.?.?? 1,2,1,1
?#????.???.?? 6,1,1
??#.?????#? 1,1,2
.??#?.?.#????? 3,1,1,1
??.?????????# 1,3,1,1
?#.#?????.?????? 2,1,1,5
.????#??..????#? 1,1,3,4
?????..#?.#??# 4,1,4
??.????##?..?#?? 1,2,3,2
???##??.#?##???? 1,2,1,5,2
??#???????#???#? 4,8
#?#??#.???????#?. 4,1,2,1,2
?????#?#??.??.??? 1,5,2,2
?#???#???.? 1,2,1
????.?##??#???#??##? 3,7,5
#?????#?.#? 1,3,2
.??#?####?##?#??? 11,1,1
####??#.###.??.?? 4,2,3,2,1
#???.??#?#??# 1,1,5,1
?##.?????. 3,2
.?.????????#? 1,2,2,3
??????#??.??#?#?.? 8,5
??.?...?..?.??.?.?.? 1,1
.#??.???#.?#?#?? 2,1,1,6
?.#??##??#???????? 1,1,2,4,1,1
##?.?.##??????#??.?? 2,10
.?????##????.?.??#? 1,6,1,1,2
.##??#?#??##?#??? 2,8,2
??.?#.??#?.???#??? 1,2,2,5
?????.?????????#?.? 1,1,3,2,2,1
.#?##???##??.?.# 9,1,1
??????#???????? 7,2
#?????.?????#?. 1,2,1,1,1
?.#?????????#.#?# 1,1,4,1,3
?.??#??#??#??#.. 1,2,2,1,2
??.##??????#?????. 1,2,2,1,1,4
#?.?????#?.?##?? 1,2,2,5
.?#?#?#?.?.# 6,1
#.????#?#??# 1,6,2
??.??????? 1,2
???#?.?..??.??#????. 2,2,4
??????#??????? 2,2,4,1
?.????#?..???? 5,1
???..????.?????? 3,1,3
???.???#??. 1,1
?...?#?.??.?#?.? 2,3
???#..??..#?#??. 4,2,3
..?????#??? 4,1
???##?.#???#?? 6,3,1
????#??.??.. 5,1
??????#??? 3,2
??????????#?????? 3,3
?????.??#??#??? 3,8
?#?##..?#.?#? 1,2,1,2
#???##?#????. 10,1
??????.???#??? 2,2
?????###??.???. 9,1
??##???#????.?#??#? 1,2,5,1,1,2
?.?????#??#.?? 1,5
?#...???#?#??#?. 1,9
???.#?????????.???# 3,6,2,1,1
.?#?#????.?? 7,1
??.#?.#??#??.?? 1,2,1,1,1
????????##?..? 1,1,5,1
?????????????.?.?. 3,5,1
??#?.#?????? 1,1,1,1
?????????#..??#? 3,6,1,1
.?.??..?.??.?.???.?. 1,2
????#???.?###...???? 6,4,1,1
???#?#??#??????..??. 13,2
.##???.?????? 4,2
??????????? 7,1
.???.#?#?##?.???. 1,6,1,1
?????.#?.??#???# 3,2,1,2,1
?????#?#?###??##??# 1,1,1,5,6
???...?#?.#??#?. 2,2,1,2
.?#???????? 2,1
?.?##????????? 1,5,1,1
..??????##?#???.?? 3,8,2
?????.?.??????#?.?? 1,2,3,1,2,2
??#..??##?.# 1,3,1
#?#??..??#.?.?#?.??? 5,3,1,3,1,1
?????#??#??#? 1,2,1,1
??.#???#?#???#?..??? 12,1
??#?#..???#??? 3,1,1,1
?.??.??.#??#???#?#?? 1,11
??#.??#??#??.?? 1,5,2
?#???#?#?#?????.?? 10,1,1,1
?#???#?????##?. 7,4
???##??#?#.???.??. 5,1,1,1,1,2
????.?????#??? 3,1,3,1
.???#?.??#?.????# 3,2,5
??#?????#????#??#??? 4,2,8
?????#???.#?#??? 1,3,1,3,1
?###.???#?????.#? 3,5,1
#.?##..??.#???. 1,2,1,1,1
??#?#??????.#?..?.?? 8,1,2,1,1
????.?????.????#??? 1,1,3,2
?#?#????#????#??# 6,1,1,1,2
.???#?#???#?#?#????? 15,1
..???##.??. 1,3,2
.???#.?#??#???? 4,1,2,1
????????#?#?#??##.? 2,11
??.?.??????#??. 3,3
??.???###????##??? 1,10
#????.?#??.??.??? 5,3,1,1
?.????????##.? 1,5,2,1
???#?##??#??. 2,4,2
?.#??.??#??#?#? 1,1,8
.##???.?#???. 4,1,1
??#.????.?.#??#? 2,2,1,2,2
???##????# 1,5,1
#???????#?..?#??? 4,5,3,1
??.?????.???? 2,1,1,2
??.???.?????.???#?? 1,2,2,1,5
??.??#??#?#?..??. 1,7,1
?#???#?##?..?.?????? 9,5
#?##?#????..#? 6,1,1,1
#????.???. 3,2
?????##.?..??##????? 6,4
??????.??.??? 2,2,1,1
??????#?.??# 1,2,3
????#?????## 1,1,1,2
..#????#??#????. 2,2,2
?#.??.??????? 2,1,1
.#???????#.?#?##.. 1,1,1,1,4
?????#....?.# 3,1,1
???????#??.?#?#?? 1,2,3,4
.???#??#?? 3,1
??#??#???##??.#????? 1,11,1,1,1
??????#.#? 1,4,2
.???#?.#??.? 1,1,2,1
.?#?#????#.# 9,1
?#?.##???.?.?#.#?? 3,4,1,2,1,1
????.???.???..??? 3,2,1,1,1
#?#??..????.?????# 1,2,2,1,1,1
.??#??.#?#??#???? 1,1,1,6,3
?#?????????????#??? 2,1,3,9
?????#.?????? 1,1,1,4
?.??#???#?.#????. 1,3,2,1,1
??..#?#?.? 1,4
????#?????#. 3,1,4
??.?##??#?###??#???? 1,15
????.??#?.?..? 3,3,1
#?.??.??#?####?? 1,1,1,8
?#????##??????????? 14,2
?#????.#??.? 1,2,3
???.##?????#?????? 2,2,1,3,1
.?????????##?.# 1,8,1
??.???????? 1,2,2
??????#?#? 2,1,1
???????.#?? 1,3
?...?####????.?#?? 1,4,2,1,1
.?##?#??????? 9,1
????.???????#???#?? 2,9
?????.?.????? 2,2
????.?????. 1,1
.?????????###.??.? 11,1,1
????##?????.?? 1,2,1,1
???#?.#??##???#?#?.. 4,1,2,5
???????#??.??. 3,1,1,2
.??????????#??#?? 4,6,3
??.?????..?.?##?#??? 1,1,2,1,4,1
??#..??.????? 2,1,1,1
.#??#??.#??#? 1,3,5
.?????##??????.? 3,6,1
##?.?#..?. 3,1,1
?.#.??????#?????#?? 1,12
#??.????.?# 3,1,1
#.#?#.##??#?..???? 1,1,1,6,1,1
????#???.???#??.. 3,4
???????.##??.???? 2,2,4,1
??#??#?.####???#??? 4,10
.????###???###???? 6,6
???.??????. 1,3
??##..?#??#??###? 2,3,1,5
.????#?#????.#? 9,1
??.???#.#????????? 4,1,2,2
???#?.????#?# 1,1,4,1
.#?????.#??? 2,1
??????...???????#??# 5,2,1,5
#.?????###?????. 1,2,6
??##..????..?# 3,2,2
##???????.?#?. 2,2,1,3
??#?.#.??#.? 1,1,1,1
??##.??????..?.??. 4,1,1,1,1,1
??##?#?????????#?#?? 3,8,1,1
???????#????.????#?. 8,1,1,1,2
??????????#????#?? 1,2,11
???#??.??#. 5,2
.??????????# 3,1,2
??#.?????##?#???. 1,10
?.#???#?#???#????# 1,1,4,2,1,1
#????.?#?????#??? 2,2,9
.???#???##? 1,3,3
.??.??#???#? 3,2
???#???##??#???.??## 14,3
???##?##??.##?.?.#?? 2,6,3,1,1
???###????#???? 6,6
??.?.?#?##?##?#???? 1,1,1,5,5
?#???..?.???#?#.?? 5,1,4,1
#?????#????#???#??? 4,1,1,1,5
??#.???#????#???? 1,5,1,2
.??#?#???? 5,1
?.???..#???#?? 1,2,5,1
???#?##????..???##? 7,4
??..#?.???? 2,2,2
?.??#?.##?????#? 4,5,2
?.?##???##??##?#?. 9,4
??#?#??..#??????? 6,4
???#??.??.? 4,1
?..#?#?#?????????#? 1,6,1,2
???.#?..?? 1,2
??????????.?.#?. 4,2,1,1,1
#..??.???###?.?.? 1,1,6,1,1
??.?????#?#??#.?? 1,1,6,2
?.?##???#?? 3,2
??.???????? 1,5,1
?.#???#????#??## 1,1,5,1,2
???????????###??? 2,1,8
???.????.?# 2,1,2
.#?.??#????#.?????? 1,1,1,4,1,1
#???###?##?.??...? 10,2,1
..#.??????.?# 1,1,4,1
????#?????#.? 1,5,1,1
???#??#??#??# 2,1,2,2
?#??????????#? 1,1,3,1
??#??#??#?#?? 3,1,4
???.?????????#. 1,1,1,2,1
#??##??.?#? 5,1,1
..?##???#?#???? 2,6
#??????#?.?? 2,1,2,1
.###???.??###??#?? 5,10
?.????..?????#??? 4,3,2,1
???##??????? 1,3,1,2
????.?.####??####??? 1,11
??##???.?? 4,1
??#?.?????# 1,3,1
??.???...#..?. 1,3,1,1
.##?#??#?#??#??#??? 2,1,5,1,4
?#.????#??????????## 1,1,2,10
.#?.??#???? 2,5
?#?.#?????.??.? 3,4,2,1
.#?????.?..?? 6,1,1
###????????###? 6,3,3
#??????.??#?#? 4,1,6
??????#?????? 1,2,1
.?#.???#??????????#? 2,1,2,1,2,2
.????#?????????? 5,5
.??????????. 5,1
?????????.?#?? 2,5,1
.?#??.?.?? 2,1,2
?.#.?#?#?. 1,4
??##.??##?#??###?? 3,5,3,1
.????..??#?.? 1,1,4
.???#?????# 1,3,3
??????.?????##???.? 6,7
???#?###?.??#?##??# 6,9
##???#?.#?..#?????. 6,2,3,1
???????#?#????#.?.?# 3,11,1,1
?#?.??#??#? 2,3,2
???#?????.?? 7,1,1
?.???????#?#??.?.#? 4,2,3,2
.#.?#.??#??????? 1,1,1,5,1
?.##??????????? 7,1
?.?#????????.? 6,1
.##??#?.???? 2,1,3
#?.#?#?#????.? 1,1,6
?##???#??#.???.? 6,1,1,1
???????#?? 2,1,1
..?#????#???#?? 1,1,3,4
.?.#??##?#.?#??..#? 1,1,5,1,1,1
?#?##?#????. 6,1,1
#?#?????#?##???#?#?# 1,4,12
.????#???? 1,2,1
?..??.???. 1,1
.????????????.???? 4,1,1,1,1,1
??.??##???.?#?? 2,4,1,2
?????#.##???#??#?.? 1,3,4,1,1,1
??#?.?#??##. 1,2,6
.???.??#?#.#????##.? 2,3,1,7
.?.????????. 3,3
?????#.?.#...? 2,2,1,1
??????.##????..?. 3,4
?#.??????#???### 1,1,9
??..???#.??##????#?# 2,1,1,10
?????#?..#?. 3,2,1
???????..?# 2,1,1
???#???#?? 1,3,2
.#?#??.?????????.? 5,1,1,1,1
?.#?.?.??????# 2,6
???#.??????? 1,1,1,3
?#???#?????.#?? 3,5,2
???#???????.?? 1,6,1,1
..?#????#.. 1,4
?????.???# 1,1,3
??#.?????????..? 1,1,1,5,1
??##??...??#??? 6,3
#??#????#? 2,2,1
?#???##.##???? 6,2
?.?#????.?#?.????# 1,3,1,3,1,3
??.##??#?????????.. 1,8,1,1
?###?##.?????#?.???# 4,2,1,4,3
???.???????.#.??? 2,1,3,1,2
??.???#????. 1,4,1
.?##?????##???.???? 13,2
??##.???????#??#??#? 2,1,2,5,2
#??????##???. 2,1,3,2
#.???????? 1,1,1
?#?.#.?#??.??????? 1,1,4,1,3
?????#??#??? 2,5
??.??#?#?? 2,5
?.#?#?#?????????. 1,9,2,1
??#??.?##.??#.??? 1,3,1,1,3
???????.?????? 4,6
#?.?#??#?????.??? 2,9,1
#??#??#?.??#????# 5,2,4,1
?#.#?#?.?? 1,4
.?.?.????#??#?? 1,1,1,2,2
?.#???????#?.?. 1,1,3,1
#.??????..?.?. 1,4,1,1
???????.#???#??.? 7,6,1
?..##???##???? 3,3
?????###?#..???#.?#? 1,1,5,1,1,1
??.????#?.?..# 2,2,1,1
????#???##??#? 6,5
#?????##??????? 1,1,3,1,4
#?.?????#?.?? 1,2,1,1
??..#?#??##? 1,3,3
???#??#???#??. 4,1,1
???.#??##???????? 3,6,1,1,1
#?###?#?##?.#?.?.?.. 1,9,1,1,1
?#???#??#?.?.#???? 1,4,1,4
????..#.?.???#??.? 2,1,1,4,1
?????##??#.??#?.# 9,2,1
????.?##??#?????..?. 2,3,1
??????.#?#???#??.??# 4,8,3
?#?##?#????????#?? 7,1,3
?#??###??#?#?#?.? 13,1
?.??##???.??????#.? 1,6,1,2,1,1
??#??#????? 3,3,1
??.??????????#.. 5,5
????????#?? 2,6
#?.??#???.#??? 1,6,1,1
##.?????#?. 2,2,1
????#??.?#???? 4,1,5
.?????????????##?.? 5,3
.?.???.?#??.## 2,1,2
.?????????###????? 3,5
.###??.##?? 5,3
?#??????#?.??#???? 5,3,3
.????#??????? 1,2
??#??????..#???#?. 3,1,5
.???#?#?.???.?????? 6,3,2,2
??.#??.???. 3,2
?.??.???#.?? 1,4,1
.?????.???..#?? 1,1,1,1,3
#????????? 4,2
????#?...????????#?# 1,2,1,9
??#?#####???? 2,5,1
.??#???#?. 3,2
?#?#?.##????#?????? 1,1,9,2
?####?????.?.???? 8,2
#???#??.??.??? 2,3,1,3
.#??##?????#.#?? 7,1,1,1,1
?..????.???###????. 1,7
???##???#???.??#?#? 9,1,6
???#?????????. 3,5
#?#??#??#?. 3,5
?#??.?.???? 3,1
???###.?#.. 3,2
?????????.??? 4,1,1,2
???#??#??.? 8,1
#..??.#???? 1,5
????#??###?#?#?#???? 2,1,6,7
???????????###????. 13,1
???####?.? 1,4,1
?##.???#????##?##?? 2,1,9
???..??..?.#?#??#.. 3,2,6
.#?#???.?#?##??? 1,1,1,6,1
??#?..??????#??? 1,6,1
#.????#??????# 1,8
???#??..?? 1,1
???..????????? 1,1,4,1
.????.#???. 1,1
#???#?#?#?.??.#?? 9,2
#??#?##????.??.?? 10,1
.?#?.?????##????#? 2,11
????#??.#???#?????? 1,4,1,3,1,1
.?.??..???#?? 1,2,5
.#?????.?.???#?#??#? 1,4,2,1,1,1
??#????#??#???#.??? 1,1,10,1,1
.???..#??#???.. 2,7
??.#???.#?????? 1,2,1,5
????#??.??????#? 1,3,1,3,2
##?????##..???.???.? 2,6,3,1,1
??##???.??????#?? 7,4,1
#..##.??#???#??? 1,2,1,1,3
#??.?##...?? 1,3
??##?...###... 5,3
#?#??#????#??#..#? 11,2,1
???#?????#?#???#??.? 4,8
??.??????#????????? 9,1
??.??.?????# 1,1,5
???.??????#??? 1,1,3,1
.?.#???.???#?????? 2,7
???##??.?#?###? 2,2,1,2,3
???????#.??.#????#.? 1,4,1,1,2,1
.???#.????#.?????? 1,1,5,2,1
?.?.???###?##???? 1,10
?????.?#?.? 5,1
????????##.?? 3,5,1
.???#??##?####??? 1,6,4
#?????????#?. 3,4
.?.??#?.??.???.? 1,1
.???#?????? 4,1,1
???#?#?..?...#???.. 4,1,1,1
?????.????##???? 1,1,1,1,6
??#..????? 1,1
?#?.?????#??#..?#. 2,2,2,2,2
????#..????? 4,3
??????????#.?. 2,4,1
??..#?????..?.#???? 1,6,1,1,1
??#?####????? 10,1
?#???#.?..?? 3,1,1
?????#????????????? 5,4,2
##??.??..?.?? 2,1
.?#?#??.??####???? 6,8
##?.??#???#?#???. 3,4,3
?#.?#...?#.???.# 1,1,2,2,1
?#..????#??? 2,2,3,1
??#??????? 2,1
????..?.????#?# 3,1,1,3
?????.??.????#???#?? 1,1,1,1,2,7
.?##??.?#?.? 4,2
????#??.??. 5,1,1
??????.??? 5,2
????????#?#? 2,1,4
??.?????????#??.#?? 2,5,4,1
??.??????????? 1,4,1,1
???#????.? 2,4,1
??????.?#?# 1,2,3
#???????#?. 1,4,1
????#.??#???.???.? 5,1,1,1,2,1
?#?????.??##?? 1,1,2,3
?...???????? 1,1,3
.##????#.?#?? 3,2,1
#??#?.?.#??##.????? 5,1,5,1,1
.???#????? 6,1
?#???????.?###??#. 2,1,1,4,1
#??????.???????? 5,1,1,1,3
.?#??###?#?#?##?..?? 15,2
.?.??#?######?.??.?? 1,10,2
??#???.#??#?????# 5,8,1
????.????? 4,3
??#.???.??? 1,1,3
.????.##??????#?##? 4,2,2,4
??#??????###????#?.? 4,1,10,1
????#..???? 4,2
#?????????#???????.# 1,2,1,1,3,1
?#??##???.#?#.? 8,3,1
????.#?#???#### 1,1,1,3,4
??.?#?#?#?.??. 1,1,4,1
??#??????????.# 2,4,1
???#??.???##??#? 6,1,2,3
?.???#?#??#??##?.?.. 14,1
??.#??#?#??? 4,3
?#?.??????#??????#? 2,15
???.???#??.???#??. 1,2,3,5
?#?.?#?#?#?#???#???? 2,4,1,1,5,1
???????????#???. 1,1,6
??????????.?? 2,5,1
.##???????.?#???? 9,3
.???..?.?###? 2,1,3
?#??##??????????. 10,1
?????.????.?##?? 4,1,4
.???##?.???????#? 1,2,1,6
????????????.?? 5,1,2
.?#????????? 3,1,3
#?.?#?.??. 2,1
?#?#????????. 7,1
??????####???????#? 2,10,1
?.???..????? 1,4
.????##??#?##? 2,9
#??#?#?#??.#.#?? 9,1,2
?#??.?###???????? 1,1,6,2,1
?###??????.?# 4,2,1
#.??#??.?##?#. 1,4,5
?????.????????? 1,1,5,2
??.?#..#?????#?? 1,2,3,5
?.??#????.?????#?# 6,8
?.??#.?##?????? 1,2,6,1
#??#.?.?.#?#?????#?# 1,1,1,1,1,9
.????#??##?????#??? 9,5
?#????#?##.????? 7,2,1,1
?.??????.??? 1,1,2,1
??##???#?##?? 4,5,1
#??????####?.???? 1,8,1,1
?.#?###?????#?#? 5,4
?.??#.???.#.#?#. 1,2,1,1,3
#.#?#?##??##?.??.. 1,10,2
???????#?????#??? 3,2,1,1,5
.?.#??.?#?#?.?#???? 1,1,4,2,2
??##???.???# 6,1,1
?#??..???#?#???#.??? 1,1,2,5,1,1
##?.??#???#??###? 2,3,2,5
?.???#???#?#?#???#? 1,1,1,1,9
?#??#??#??.?.#?. 2,2,2,1,2
????#??.?##? 4,3
?.?#???..?####???? 1,2,1,7,1
#???????.? 1,2,1
#?..???..??????? 1,1,1,1
.#??#?????? 1,6,1
.#?.?.???##?? 1,1,5
??#????.###?##??? 2,2,3,2,2
?#?.?.???. 2,1
.??..???????.????? 2,3,1,1,1,1
.??.#???.???? 3,2
...?.??#???.. 1,1
.??.?.?????????#??? 1,3,2,5
?.???..?#.#????# 1,2,1,6
.?#???.??#?????. 4,5
?##?.???..#? 3,3,2
.##???#?#?.?#??.??? 3,4,3,2
.????#??.?? 4,1
?##??#?###???#???#?? 2,5,1,5,1
??#??.?.##??? 1,2
..#????#??#?? 1,2,1,3
??????##?. 2,3
.????????.?#????? 1,6,1,2
??.?#????.#??#?. 1,2,2,1,1
.?#?????????.#?# 2,5,1,1,1
???????.???????#?#? 2,10
?#?#?.#.?????#? 3,1,2,2
???????#?????????? 3,1,4,2
?.?.??????? 1,3,1
????.#???#?.##.?? 1,1,5,2
????..#????.????? 3,1,1,1,2
????#?.#???#?? 6,6
?.?#???.??.??### 1,2,1,1,3
..##?.??#?.?#?.#?. 3,1,2,2,2
.?##?#??.? 2,1,1
?#???##?????. 6,1
???#?#???#?#?#???? 2,3,7,2
.#?#?..####?? 1,1,6
#???#??#????? 2,9
?..?#??????#???.?#? 1,1,8,2
?.#???#??? 1,1,4
..???##???#?#?.#??. 11,2
????##????. 1,6
??????#??.?????. 1,1,1,2,2
?#?##???????#.?#? 13,2
?????????# 2,2
##???????. 5,3
????????##??# 2,5,1
???#?#?##???#?#??#? 8,1,1,4
?.????????. 6,1
???????#.??#?#??# 4,3,7
#####????#?????????. 10,1,1,1
#??????#?#.?????? 1,6,1,2
.??.??????????#?# 4,3
.???..#??. 1,3
???.?????? 1,1,2
#?.??#???.??? 1,3,1,1
???????.???.. 1,2
.##???#?.#???#?#?# 2,2,9
.?#???.?.? 1,1
?#?#????#?#.??#? 4,3,1,4
.?????.?????????# 4,1,6,1
????.???#?#??###? 4,1,5,3
??#????????#??#?..# 3,1,1,3,1,1
.?????.?????????.# 1,1,1,1,5,1
..?????????#???.??? 5,5,1
??#????#?? 1,1,1
????#?#?????? 1,1,4,1
???#??#??.?#?? 7,2
????.#??.?.##? 1,1,1,3
??.#???.??? 1,2,1
#?????##?#????? 11,1
?...??#??. 1,5
?????#?#?.???# 1,1,3,4
??.??##.####????.# 2,1,2,7,1
??#????..? 5,1
????#??#???#??#?##? 3,2,7
.???##????.##?##?. 5,5
??#??#??#?#? 1,9
??#?#??#??.#???#???? 10,5,2
.??.?????#? 2,1,2
???#.??#?#??#? 1,1,9
??#?????..???# 7,4
..#??.?###???#?#.? 3,9
???#?????##?.????# 3,4,5
#??#?#???# 1,4,2
??#??#???#?.#?#??? 1,1,6,1,1,1
??#????.???#.#? 2,2,1,1,2
##?#?????#?.????#?? 6,3,5
????#?.?????? 3,3
??#.???.?.#????#???? 2,1,2,7
??#?#???.???? 8,1
#.?#.?#????.???. 1,1,3,1,3
##???#????.?..?.??? 10,1,1,1,1
????#??#?????? 1,7,3
???.?.??.??? 2,1,1,1
?#?###?????.?#?#?.?? 9,1,1,1,1
???###?##???.#? 1,4,2,1,1
????###?????#?.? 1,11,1
????#??..??##??? 5,1,3
.????##??????..##. 12,2
?.#????#?? 2,2
????????#?#????#??.? 2,4,3
????.#???.??#?#. 4,3,5
??##????.#?.?#. 7,1,1
.?.??.??..? 1,2
##???.#?.? 2,2,2
.?????#?.??#.? 4,2,1
..##??#??#? 2,2,2
??..?.?.??..?. 1,1
???.?.?..???#?#?? 1,1,8
???##?#???#????? 1,3,2,2,1
?.?????#?????#??.??? 1,1,2,6,2
?????.#?????#?#???. 1,1,9,2
?#?.????.???????## 1,4,1,1,1,2
.?.?##??.### 2,3
??????##???# 2,4,2
.?#.#.?#????..#.?? 2,1,1,3,1,1
?.#???..??????.? 2,3
#..#??????????? 1,1,3,5
??.??.???.?...? 1,2
.?.#???#?#. 1,4
#??..??#.?#? 1,1,1,3
?.?##??.#.?? 4,1
???????.#??? 1,2,1,1
.????#??.?. 2,3,1
????.?#???? 2,3,1
???#???.?#?????? 1,4,2,2,1
.#?????..???????.? 6,7"""

data_test = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

data_one = "#??.### 1,1,3"

start = time()

data = data.split('\n')

final = 0
for row in data:
    record, groups = row.split(' ')
    record = re.sub(r'\.+', '.', record)
    record = ((record + '?') * 5)[:-1]
    groups = [int(c) for c in groups.split(',')]
    groups = groups * 5
    # print(record, groups, len(record))

    possibles = []
    for caracter in record:
        if not possibles:
            if caracter == '?':
                possibles.append('.')
                possibles.append('#')
            else:
                possibles.append(caracter)
            continue
        if caracter == '?':
            np = []
            for e in possibles:
                np.append(e + '#')
                np.append(e + '.')
            possibles = np
        else:
            np = []
            for e in possibles:
                np.append(e + caracter)
            possibles = np

    for possible in possibles:
        possible_groups = [len(x) for x in re.findall('(#+)', possible)]
        # print(possible, len(possible), possible_groups, g)
        if possible_groups == groups:
            final += 1

print('day 12 - part 1:', final)
print('time:', time() - start)
