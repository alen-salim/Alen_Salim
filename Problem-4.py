# Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#   (examples)
#   input: [1,2,8,9,12,46,76,82,15,20,30]
#   Output: 
#     {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

input = [1,2,8,9,12,46,76,82,15,20,30]

output = {}

for number in range(1,10):
    count = 0

    for num in input:
        if num % number == 0:
            count += 1
    output[number] = count

print("output :", output)