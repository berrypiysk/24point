import itertools
def equal_to_24(a,b,c,d):
    all_ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else 0,
    }
    for nums in itertools.permutations([a,b,c,d]):
        for ops in itertools.product(all_ops, repeat=3):
            result1 = all_ops[list(ops[2])[0]]((all_ops[list(ops[1])[0]](all_ops[list(ops[0])[0]](nums[0], nums[1]), nums[2])),nums[3])
            result2 = all_ops[list(ops[2])[0]](all_ops[list(ops[0])[0]](nums[0],nums[1]),all_ops[list(ops[1])[0]](nums[2], nums[3]))
            result3 = all_ops[list(ops[2])[0]](nums[3],(all_ops[list(ops[1])[0]](nums[2],all_ops[list(ops[0])[0]](nums[0], nums[1]))))
            result4 = all_ops[list(ops[2])[0]](nums[3],(all_ops[list(ops[1])[0]](all_ops[list(ops[0])[0]](nums[0], nums[1]),nums[2])))

            if result1 == 24:
                return ("(({0}{4}{1}){5}{2}){6}{3}".format(nums[0],nums[1],nums[2],nums[3],ops[0],ops[1],ops[2]))
            if result2 == 24:
                return ("({0}{4}{1}){6}({2}{5}{3})".format(nums[0], nums[1], nums[2], nums[3], ops[0], ops[1], ops[2]))
            if result3 == 24:
                return ("{3}{6}({2}{5}({0}{4}{1}))".format(nums[0], nums[1], nums[2], nums[3], ops[0], ops[1], ops[2]))
            if result4 == 24:
                return ("{3}{6}(({0}{4}{1}){5}{2})".format(nums[0], nums[1], nums[2], nums[3], ops[0], ops[1], ops[2]))
    return "It's not possible!"
if __name__ == '__main__':
    print(equal_to_24(1, 1, 1, 13))
