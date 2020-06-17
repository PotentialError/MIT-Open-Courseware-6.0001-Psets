# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: 0:15

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    list = []
    if len(sequence) == 1:
        return [sequence]
    else:
        small_list = get_permutations(sequence[1:len(sequence)])
        first = sequence[0]
        for i in small_list:
            for j in range(0,len(i) + 1):
                temp = i[:j] + first + i[j:len(i)]
                list.append(temp)
        return list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'car'
    print('Input:', example_input)
    print('Expected Output:', ['car', 'cra', 'rca', 'rac', 'acr', 'arc'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'eat'
    print('Input:', example_input)
    print('Expected Output:', ['eat', 'eta', 'aet', 'ate', 'tea', 'tae'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'gas'
    print('Input:', example_input)
    print('Expected Output:', ['gas', 'gsa', 'ags', 'asg', 'sga', 'sag'])
    print('Actual Output:', get_permutations(example_input))

