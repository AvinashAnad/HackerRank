def split_and_join(line):
# write your code here
	s = line.split(" ")
	return "-".join(s)

if __name__ == '__main__':
	line = input()
	result = split_and_join(line)
	print(result)