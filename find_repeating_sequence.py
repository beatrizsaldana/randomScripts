'''
Script to find repreating sequence in list of numbers.
Assumption: sequence consists ONLY of repeating sequences.
For example...
    if input = 1,2,3,1,2,3
    output = 1,2,3

    if input = 1,1,1,2,3,1,2,3
    output = None

    if input = [1,2,3,1,2,3,1]
    output = [1, 2, 3]

The script will validate that the ENTIRE input sequence
consists of the same repeating sequence.

Worst case scenario runtime:
n = sequence length
loop through entire sequence
loop through sequence but in sequence/repeating_sequence chuncks
O(2n)
'''

from typing import List


def validate_perfect_repeating_sequence(repeating_sequence: List[int], sequence: List[int]) -> bool:
    '''
    This function will be called when a sequence can be
    divided perfectly into the repeating sequence without
    any extra values.
    For example:
        sequence: 1,2,3,4,1,2,3,4,1,2,3,4
        repeating sequence: 1,2,3,4
    
    This each chunk of sequence of len(repeating_sequence)
    is equal to the repeating sequence, then return True,
    otherwise return False.
    For example:
        If the sequence is [1,2,3,4,1,2,3,4,1,2,3,4]
        and the repeating_sequence is [1,2,3,4]
        The first iteration of the while loop will start at
        index 0 and will check if the values from index 0 to
        index len(repeating_sequence) are the repeating_sequence.
    '''
    i = 0
    while i < len(sequence):
        if not sequence[i:i+len(repeating_sequence)] == repeating_sequence:
            return False
        i=i+len(repeating_sequence)
    return True


def validate_imperfect_repeating_sequence(repeating_sequence: List[int], sequence: List[int]) -> bool:
    '''
    This function will be called when a sequence cannot be
    divided perfectly into the repeating sequence without
    any extra values.
    For example:
        sequence: 1,2,3,4,1,2,3,4,1,2
        repeating sequence: 1,2,3,4
    '''
    remainder = len(sequence) % len(repeating_sequence)
    if not validate_perfect_repeating_sequence(repeating_sequence, sequence[:len(sequence)-remainder]):
        return False
    if sequence[-remainder:] == repeating_sequence[:len(sequence[-remainder:])]:
        return True
    else:
        return False


def validate_repeating_sequence(repeating_sequence: List[int], sequence: List[int]) -> bool:
    '''
    Call the correct validation function.
    '''
    if len(sequence) % len(repeating_sequence) == 0:
        return validate_perfect_repeating_sequence(repeating_sequence, sequence)
    else:
        return validate_imperfect_repeating_sequence(repeating_sequence, sequence)


def find_repeating_sequence(sequence: List[int]) -> List[int]:
    '''
    The main function that will build a repeating sequence
    from the input sequence. If the input sequence does
    not consist of repeating sequences, then the function
    will return None.

    The function will loop through the sequence until
    it finds a repeating sequence. Then it will validate
    the collected repeating sequence, if the repeated sequence
    does indeed repeat n times in the input sequence, then the
    loop will stop and the repeating sequence will be returned.
    '''
    repeating_sequence = [sequence[0]]
    for i, value in enumerate(sequence[1:]):
        if (
            value == repeating_sequence[0] and
            sequence[i+1:i+1+len(repeating_sequence)] == repeating_sequence and
            validate_repeating_sequence(repeating_sequence, sequence)
        ):
            break
        else:
            repeating_sequence.append(value)
    if repeating_sequence == sequence:
        repeating_sequence = None
    return repeating_sequence


def main():
    print(find_repeating_sequence(sequence=[1,4,2,8,5,7,1,4,2,8,5,7,1,4,2,8,5,7,1,4,2,8,5,7,1,4,2]))
    print(find_repeating_sequence(sequence=[1,1,1,2,3,1,2,3]))
    print(find_repeating_sequence(sequence=[1,2,3,1,2,3,1,2]))


if __name__ == "__main__":
    main()
