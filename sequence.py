def main():
    answer = str(longest_substring([0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0]))
    print(answer)

def longest_substring(X):
    length = len(X)
    iteration_lenght = length -1 
    substring = 1
    longest_substring = 0

    if length == 1:
        return substring

    for alt in range(iteration_lenght):
        if X[alt] != X[alt + 1]:
            substring += 1
            longest_substring = substring if substring > longest_substring else longest_substring
        else:
            longest_substring = substring if substring > longest_substring else longest_substring
            substring = 1

    return longest_substring 



main()