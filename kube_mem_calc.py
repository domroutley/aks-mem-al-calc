import sys

def calc(remainingMemory, threshold, portionUsable):
    amountUsable = 0
    # If the remaining amount is less than the next threshold
    if remainingMemory < threshold:
        amountUsable = (remainingMemory * portionUsable)
        next = remainingMemory
        remainingMemory = 0
    else:
        remainingMemory = remainingMemory - threshold
        amountUsable = (threshold * portionUsable)
        next = threshold
    return amountUsable, remainingMemory, next

def main(nodeMemory):
    print(f"Total node memory: {nodeMemory}GB")
    remainingMemory = int(nodeMemory)
    first = second = third = fourth = fifth = 0

    # 25% of first 4GB
    if remainingMemory > 0:
        first, remainingMemory, next = calc(remainingMemory, 4, 0.75)
        print(f"Out of first 4GB, {first}GB is usable")

    # 20% of next 4GB
    if remainingMemory > 0:
        second, remainingMemory, next = calc(remainingMemory, 4, 0.8)
        print(f"Out of next {next}GB, {second}GB is usable")

    # 10% of next 8GB
    if remainingMemory > 0:
        third, remainingMemory, next = calc(remainingMemory, 8, 0.9)
        print(f"Out of next {next}GB, {third}GB is usable")

    # 6% of next 112GB
    if remainingMemory > 0:
        fourth, remainingMemory, next = calc(remainingMemory, 112, 0.94)
        print(f"Out of next {next}GB, {fourth}GB is usable")

    # 2% of total remainder
    if remainingMemory > 0:
        fifth = (remainingMemory * 0.98)
        print(f"Out of remaining {remainingMemory}GB, {fifth}GB is usable")

    totalAllowed = first + second + third + fourth + fifth
    print(f"Memory avaliable after deduction of portions reserved by AKS: {round(totalAllowed, 2)}GB")

    # 750Mi eviction threshold
    totalAllowed = totalAllowed - 0.75

    print(f"Max allocatable Memory for AKS cluster: {round(totalAllowed, 2)}GB")
    print("Does NOT include resources reserved by OS, includes 750Mi eviction threshold")

if __name__ == "__main__":
    main(sys.argv[1])
