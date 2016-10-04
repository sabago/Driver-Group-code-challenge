# Driver-Group-code-challenge
My attempt at the above

Problem: 50 DNA sequences each no longer than 1000 characters to be appended in an overlapping manner
Approach: Boyer-Moore variation
-I start with two random sequences and comppare if they have any matching segments; then I compare if their heading or trailing segments match; if there's a match, I join (append) them.
-I repaet the above for all 50 sequences until I have one 50000 character DNA segment, hopefully with the proper overlapping
-I run the algorithms for both the forward and reverse directions.
