''' Approach
1.Create a loop that moves 2 times at a time to loop through the list to check adjacent numbers
2.Check in the loop if the adjacent numbers are alternating using an if statement and count the length of the subsequence.
3.return the count
'''

''' Step 1- Loop '''

def main():
    # print(alt_subsequence_best([0,1,0,1,0,1,0,1,0,0,0,1,0,1,0]))
    print(alt_subsequence_best([1,0,0,1,0,1,0]))


def alt_subsequence_best(x):
    initial_count = 0
    count = 1
    length = len(x)
    for i in range(0, length, 2):
        if i+1 >= length:
            if count > 0:
                if x[i-1] == x[i+1] and x[i] != x[i-1]:
                    count+=1
                    if initial_count < count:
                        initial_count = count

                else:
                    count = alt_subsequence_best(x[i+1:])
                    if initial_count < count:
                        initial_count = count
            elif count == 0 and x[i] == 0:
                initial_count = count + 1
        else:
            if x[i] == 0 and x[i+1] == 1:
                count += 2
                if initial_count < count:
                    initial_count = count
            else:
                count = alt_subsequence_best(x[i+1:])
                if initial_count < count:
                    initial_count = count
    return initial_count
	
					
if __name__=="__main__":
    main()
		