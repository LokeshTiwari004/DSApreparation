#!/bin/python
import time
from colorama import Fore, Style

def DNF(nums, display=False):
    lo, mid, hi = 0, 0, len(nums) - 1
    while mid <= hi:
        if display:
            print(*nums[:lo], f"{Fore.GREEN}{nums[lo]}{Style.RESET_ALL}", *nums[lo+1:mid], f"{Fore.CYAN}{nums[mid]}{Style.RESET_ALL}", *nums[mid+1:hi], f"{Fore.YELLOW}{nums[hi]}{Style.RESET_ALL}", *nums[hi+1:])
            print()
            time.sleep(1.5)
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    numbers = parser.add_argument("numbers", type=int, nargs='+')
    args = parser.parse_args()
    DNF(args.numbers, display=True)
