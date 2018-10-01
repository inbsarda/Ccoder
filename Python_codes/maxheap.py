def max_heapify(A, i):
    print(i)
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(len(A)):
        max_heapify(A, i)



def ptree(A, i=0, indent=0):
    if i < len(A):
        print('  ' * indent, A[i])
        ptree(A, i * 2 + 1, indent + 1)
        ptree(A, i * 2 + 2, indent + 1)

A = list(range(9))
#ptree(A)
build_max_heap(A)
print(A)
#ptree(A)
