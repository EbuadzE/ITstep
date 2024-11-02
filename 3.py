A = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))


B = [30.5, 34.25, 27.0, 23.25]

total_sum = sum(sum(sub_tuple)for sub_tuple in A)
total_elements = sum(len(sub_tuple) for sub_tuple in A)

average = total_sum / total_elements

print(average)


sumB= sum(B)
C=len(B)
aver=sumB/C
print (aver)
