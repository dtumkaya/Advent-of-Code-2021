# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 23:15:12 2022

@author: demet
"""

def part1():
    depth = 0
    horizontal = 0

    file = open("day2.txt", "r")
    for line in file:
        if (line.split()[0] == "forward"):      
            horizontal += int(line.split()[1])
        elif (line.split()[0] == "up"):      
            depth -= int(line.split()[1])
        elif (line.split()[0] == "down"):      
            depth += int(line.split()[1])
    return horizontal, depth
            

def part2():
    depth = 0
    horizontal = 0
    aim = 0

    file = open("day2.txt", "r")
    for line in file:
        if (line.split()[0] == "forward"):      
            horizontal += int(line.split()[1])
            depth += aim*int(line.split()[1])
        elif (line.split()[0] == "up"):      
            aim -= int(line.split()[1])
        elif (line.split()[0] == "down"):      
           aim += int(line.split()[1])
    return horizontal, depth


def main():
    hori1, dep1 = part1()
    hori2, dep2 = part2()
    
    print("First part starting...\n")
    print("Horizontal position: ")
    print(hori1)
    print("Depth: ")
    print(dep1)
    

    print("\nSecond part starting...\n")
    print("Horizontal position: ")
    print(hori2)
    print("Depth: ")
    print(dep2)

    print("\nEND")
    
main()