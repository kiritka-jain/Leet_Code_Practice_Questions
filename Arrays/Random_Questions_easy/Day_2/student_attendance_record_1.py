"""
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.
"""
s = input()
s_len = len(s)
consecutive_late = 0
absent = 0

for status in range(s_len):
    if s[status] == "A":
        absent += 1
    elif (status+3 <= s_len) and (s[status:status+3] == "LLL"):
        consecutive_late =3
if (absent<2) and consecutive_late != 3:
    print(True)
else:
    print(False)


