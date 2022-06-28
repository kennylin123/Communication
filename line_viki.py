

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	allen_word = 0
	Viki_word = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				allen_word += len(m)
		elif name == 'Viki':
			for m in s[2:]:
				Viki_word += len(m)
	print('allen說', allen_word)
		#print(s)
		#print(time)
		#print(name)
		#print(talk)
	



def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)


main()