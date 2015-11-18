# https://codility.com/programmers/task/max_product_of_three

def main():
    print(solution([-3,1,2,-2,5,6])) # 60 == indexs 2,4,5 == 2 * 5 * 6
    print(solution([1,2,3])) # 6
    print(solution([-10, -2, -4])) # -80
    print(solution([-5, 5, -5, 4])) # 125
    print(solution([-2, -3, -5, -6, 0])) # 0
    print(solution([-5, -6, -4, -7, -10])) # -120 

def solution(A):

	# deal with the simple case first
	if len(A) == 3:
		return A[0] * A[1] * A[2]

	maxs = [ -1001, -1001, -1001]
	mins = [ 1001, 1001 ]

	for l in xrange(0,len(A)):
		v = A[l]
		update_mins(mins, v)
		update_maxs(maxs, v)
		
	max_product_from_positives = maxs[0] * maxs[1] * maxs[2]
	max_product_from_negatives_and_largest_positive = mins[0] * mins[1] * maxs[2]

	largest = max(max_product_from_positives, max_product_from_negatives_and_largest_positive)

	return largest

def update_mins(arr, value):
	if value <= arr[0] : 
		arr[1] = arr[0]
		arr[0] = value
	elif value < arr[1] :
		arr[1] = value
	return arr

def update_maxs(arr, value):
	if value >= arr[2] : 
		arr[0] = arr[1]
		arr[1] = arr[2]
		arr[2] = value
	elif value >= arr[1] :
		arr[0] = arr[1]
		arr[1] = value
	elif value > arr[0] :
		arr[0] = value
	return arr

if __name__ == "__main__":
    main()