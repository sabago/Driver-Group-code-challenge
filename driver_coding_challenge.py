# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:05:34 2016

@author: sabago
"""

X = 1000 # Length of DNA


#Read the data into a DNA list
def main():	
	
	#filename = input("enter file\n")
	filename = "./coding_challenge_data_set"
	
	DNAsequences = readFile(filename)

	if DNAsequences != None:

		# build off of one sequence
		longSequence = DNAsequences[0]
		del DNAsequences[0] 
  
		# build off of left end of Sequence
		longSequence, DNAsequences = keyfunction(longSequence, DNAsequences, 0) # print(len(sequences))
		# build off of right end of Sequence
		longSequence, DNAsequences = keyfunction(longSequence, DNAsequences, 1) # print(len(sequences))
		print(longSequence)
		return longSequence 
  
def readFile(filename):
	try:
		givenfile = open(filename + ".txt", "r")	
		print ("File opened successfully\n")		
		DNA = givenfile.readline() 
		DNAline = "" 
		DNAsequence = [] 

		while DNA:
			if DNA[0] == ">": #Check for first line before each DNA sequence
				if DNAline:
					DNAsequence.append(DNAsequence) 
					DNAline = ""  #reset DNAblock
			else:
				DNAline += DNA
			DNA = givenfile.readline().rstrip() # get next DNA line
		
		DNAsequence.append(DNAline)

		return DNAsequence
		givenfile.close()
	except IOError:
		print("Failed to open file\n")
		return None

"""
Checks if the leading or trailing part of a shorter sequence exists in a longer sequence; returns true if match\\
if tag ==0, check leading part, otherwise check trailing part.
"""
def ShortAndLong1(longerSequence1, shorterSequence1, i, tag):
	if tag == 0:
		j = X-1
		while i < len(shorterSequence1):
			if shorterSequence1[i] != longerSequence1[j]:
				return False
			i+=1;j+=1		
	else:
		j = len(longerSequence1) - 1
		while i > 0:
			if shorterSequence1[i] != longerSequence1[j]:
				return False
			i-=1;j-=1
	return True
"""
Checks whether a given sequence exists in a longer sequence, if match, output is true; otherwise false
"""
def ShortAndLong2(longerSequence2, shorterSequence2, i):
	j = 0
	# compare starting from i and 0
	while j < len(shorterSequence2):
		if longerSequence2[i] == shorterSequence2[j]:
			return True
		else:
			j+=1
			i-=1
	return False
"""
Function to combine sequences where they overlap; tag is defined as before
"""
def combineSequences(longerSequence3, shorterSequence3, i, tag):
	newSequence = ""
	if tag == 0:
		j = 0
		while j < i-(X-1):
			newSequence+= shorterSequence3[j]
			j+=1
		longerSequence3 += newSequence 
	else:
		j = i+1
		while j < len(shorterSequence3):
			newSequence+= shorterSequence3[j]
			j+=1
		longerSequence3 += newSequence 
	return longerSequence3
"""
Searching and adding on sequences 
"""
def keyfunction(longSequence, sequences, tag):
	if tag == 0:
		mainSequence = longSequence[:X] # get first 1000 characters
	else:
		mainSequence = longSequence[-X:] # get last 1000 characters
	# reverse for convenience, puts search value at 0 
	reverseSequence = mainSequence[::-1]

	j = 0 # counter for list of sequences
	i = X-1 # counter for each individual sequence

	# Go through and check for a matching sequence
	while j < len(sequences):
		DNAinputs = sequences[j]
		while i < len(DNAinputs): # Not Boyer Moore, but has the whole word shift , grows O(n)
			# start comparing at the Xth letter of sequence
			firstSequence = DNAinputs[i] 
			lastSequence = reverseSequence[0] # end value of keySequence
			# compare two letters
			if firstSequence == lastSequence: 
				# if they match, compare entire chunks
				if ShortAndLong2(DNAinputs, reverseSequence, i): # grows O(n)
					beforeSequence = mainSequence
					"""
					Function to compare left and right chunks"""
					
				def compare(j):
					longSequence2 = combineSequences(longSequence, DNAinputs, i, 0)
					mainSequence = longSequence2[:X] # new keySequence
					del sequences[j] # delete that sequence
					j = 0 
            				if beforeSequence == mainSequence:
							return longSequence2, sequences
            				else:
							reverseSequence = mainSequence[::-1]
							#return reverseSequence       
					if tag == 0: # compare right part of sequence
						
						if ShortAndLong1(longSequence2, DNAinputs, i, 0): 
        						compare()
							
					else:
						if ShortAndLong1(longSequence2, DNAinputs, i, 1):
        						compare(reverse=True)				
			else:
				# if not, check if cs is in subsequence at all 
				if firstSequence not in reverseSequence:
					i+=1000 # skip over 1000 spaces
			i+=1
		i = X-1 # reset position of i
		j+=1 # evaluate next sequence 
	  
	return longSequence, sequences 


          
# run main
if __name__ == "__main__": 
	main()
