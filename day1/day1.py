# Advent of Code 2021 - Day 1 Challenge

def part1(num_array):
    count = 0
    for i in range(1,len(num_array)):
        if num_array[i]>num_array[i-1]:
            count+=1
    print(count)


def part2(num_array):
    sum_array = []

    count = 0
    for i in range(0, len(num_array)-2):
        sum=num_array[i]+num_array[i+1]+num_array[i+2]
        sum_array.append(sum)

    for i in range(1,len(sum_array)):
        if sum_array[i]>sum_array[i-1]:
            count+=1
    print(count)

def main():
    num_array = []
    file = open("day1.txt", "r")
    for i in file:
        num_array.append(int(i))

    print("First part starting...\n")
    print("Count: ")
    part1(num_array)

    print("\nSecond part starting...\n")
    print("Count: ")
    part2(num_array)

    print("\nEND")


main()

