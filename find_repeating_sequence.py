# Script to find repreating sequence in list of numbers

from typing import List


def find_repeating_sequence(sequence: List[int]) -> List[int]:
    nonrepeating_sequence = [sequence[0]]
    counter=0
    for i, value in enumerate(sequence[1:]):
        if i+1 == len(nonrepeating_sequence)*2:
            break
        if value == sequence[counter]:
            nonrepeating_sequence.append(value)
            counter+=1
        else:
            nonrepeating_sequence = []
            counter=0
    return nonrepeating_sequence


def main():
    test_sequence = [1,4,2,8,5,7,1,4,2,8,5,7,1,4,2,8,5,7,1,4,2,8,5,7]
    test_sequence = [1,1,2,2,1,1,2,2]
    result = find_repeating_sequence(sequence=test_sequence)
    print(result)

if __name__ == "__main__":
    main()


