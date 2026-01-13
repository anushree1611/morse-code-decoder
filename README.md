Morse Code Decoder
Problem Statement

Alice wants to send an encrypted message to Bob using a dot (.) and underscore (_) based encoding scheme (Morse code). Each English capital letter from A to Z has a unique Morse code representation. Since there are no spaces between letters in the encrypted message, the same string can be decoded in multiple valid ways.

The task is to take an encrypted message as input and print all possible valid decoded messages in alphabetical order.

Input

A single line containing the encrypted message made up of dots (.) and underscores (_).

Example:

_.__.

Output

-All possible valid decoded strings.

-Each decoded string is printed on a new line.

-The output is sorted in alphabetical order.

Approach

-Store the Morse code representations of letters A–Z in a dictionary.

-Use recursion and backtracking to try all possible ways of splitting the encrypted string.

-For each valid Morse code match, append the corresponding letter and continue decoding the remaining string.

-When the full string is decoded, store the result.

-Sort all decoded strings alphabetically and print them.

Sample Input
_.__.

Sample Output
KN
KTE
NG
NME
NTN
NTTE
TAN
TATE
TEG
TEME
TETN
TETTE
TP
TWE
YE

How to Run the Program

-Make sure Python 3 is installed.

-Open terminal or command prompt in the project folder.

-Run the command: python solution.py

-Enter the encrypted message when prompted.

Conclusion

This program successfully finds all possible valid decodings of a Morse code encrypted string using recursion. Since multiple interpretations are possible due to the absence of separators, all valid combinations are generated and displayed in sorted order.
