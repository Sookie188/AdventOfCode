with open("AdventOfCode_2022/Day01/input.txt", "r") as fp:
    nums = fp.readlines()

smol_arr = []
big_arr = []

for num in nums:
    snum = num.rstrip()
    if snum == '':
        big_arr.append(sum(smol_arr))
        smol_arr = []
    else:
        smol_arr.append(int(snum))
big_arr.append(sum(smol_arr))

# part 1
print(max(big_arr))

big_arr.sort(reverse=True)

# part 2
print(sum(big_arr[:3]))
