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
'''

from typing import List


def find_repeating_sequence(sequence: List[int]) -> List[int]:
    '''
    For each value of a sequence, check
    '''
    repeating_sequence = [sequence[0]]
    counter=0
    for i, value in enumerate(sequence[1:]):
        if (
            i+1 == len(repeating_sequence)*2 and
            sequence[i+1:i+1+len(repeating_sequence)] == repeating_sequence
        ):
            # check if we have reached the expected end of the repeated sequence
            # check if the sequence repeats at least one more time
            break
        if value == sequence[counter]:
            repeating_sequence.append(value)
            counter+=1
        else:
            repeating_sequence = []
            counter=0
    return repeating_sequence

def validate_perfect_repeating_sequence(repeating_sequence, sequence) -> bool:
    i = 0
    while i < len(sequence):
        if not sequence[i:i+len(repeating_sequence)] == repeating_sequence:
            return False
        i=i+len(repeating_sequence)
    return True


def validate_imperfect_repeating_sequence(repeating_sequence, sequence) -> bool:
    remainder = len(sequence) % len(repeating_sequence)
    if not validate_perfect_repeating_sequence(repeating_sequence, sequence[:len(sequence)-remainder]):
        return False
    if sequence[-remainder:] == repeating_sequence[:len(sequence[-remainder:])]:
        return True
    else:
        return False


def validate_repeating_sequence(repeating_sequence, sequence) -> bool:
    if len(sequence) % len(repeating_sequence) == 0:
        return validate_perfect_repeating_sequence(repeating_sequence, sequence)
    else:
        return validate_imperfect_repeating_sequence(repeating_sequence, sequence)


def find_repeating_sequence_alt(sequence: List[int]) -> List[int]:
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
    test_sequence = [1,4,2,8,5,7,1,4,2,8,5,7,1,4,2,8,5,7,1,4,2,8,5,7,1,4,2]
    #test_sequence = [1,1,1,2,3,1,2,3]
    #test_sequence = [1,2,3,1,2,3,1,2]
    result = find_repeating_sequence_alt(sequence=test_sequence)
    print(result)


if __name__ == "__main__":
    main()
