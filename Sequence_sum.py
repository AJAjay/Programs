

#search for a sequence to form sum

def gen_sequence(sequence,target_number,existing_sequence):

	if len(sequence) == 0:
		return 

	for index,value in enumerate(sequence):
		existing_sequence.append(sequence[index])
		
		#if target number is found print the existing_sequence
		if sequence[index] == target_number:
			print(existing_sequence) 

		#else divide the problem into subproblems
		elif len(sequence)>1 and target_number>sequence[index]:
			gen_sequence(sequence[index+1:],target_number-sequence[index],existing_sequence)
	
		existing_sequence.pop()

def main():

	#get the sequence	
	print("enter the sequence")
	sequence = list(map(int,input().split()))
	print("sequence we got -- ",sequence)

	#get the sum
	print("enter the target_number")
	target_number = int(input())

	#process the sequence to get the number
	gen_sequence(sequence,target_number,[])



if __name__ == '__main__':
	main()
