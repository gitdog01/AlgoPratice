for test_case in range(10):
	L = input()
	T = list(input())
	for i in range(len(T)):
		if T[i] == '*':
			T[i-1] = str(int(T[i-1])*int(T[i+1]))
			T[i],T[i+1] = '0'

	print(T)