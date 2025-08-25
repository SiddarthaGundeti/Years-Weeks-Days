# Years-Weeks-Days

Input: 1329

Output: 3 33 3

Question Explanation:

The program aims to convert a given number of days, N, into its equivalent in years (Y), weeks (W), and days (D). The conversion is based on the assumption that a year contains 365 days.

Logical Approach:

Read Input:
Read the number of days N as an integer.

Calculate Years (Y):
Divide N by 365 (the number of days in a year) to find the number of years.
Use integer division // to get a whole number of years.

Calculate Remaining Days After Years:
Compute the remainder of N divided by 365 using the modulo operator %.
This remainder represents the number of days not accounted for by full years.

Calculate Weeks (W):
Divide the remaining days by 7 (the number of days in a week) to find the number of weeks.
Use integer division // to get a whole number of weeks.

Calculate Remaining Days After Weeks (D):
Compute the remainder of the days after accounting for weeks using the modulo operator %.

Output:
Print the calculated number of years (Y) on the first line.
Print the calculated number of weeks (W) on the second line.
Print the remaining days (D) on the third line.

Example for Clarity:

Given N = 1329:
Divide 1329 by 365, resulting in 3 years.
The remainder is 1329 % 365, which equals 234 days.
Divide 234 by 7, resulting in 33 weeks.
The remainder is 234 % 7, which equals 3 days.

The output will be: 3 33 3

