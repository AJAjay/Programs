
#program to remove palindrome from a sentence on the same variable without using split 

#check condition for palindrome
def check_palindrome(sentence,begin,end):
	word = sentence[begin:end]
	if begin>=end:
		return sentence,begin
	if word.lower()[::-1] == word.lower():
		return sentence[:begin]+sentence[end:],begin+1
	return sentence,end+1


#remove palindrome logic
def remove_palindrome(sentence):
	begin,i = 0,0
	while i <= len(sentence):
		if i == len(sentence) or not sentence[i].isalpha() :
			sentence,i = check_palindrome(sentence,begin,i)
			begin = i
		else:
			i+=1

	return sentence
	
#main function
def main():
	print("provide the sentence:")
	sentence = input()
	print(remove_palindrome(sentence))





if __name__ == '__main__':
	main()
