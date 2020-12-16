'''
def is_palindrome (word):
	word = word.lower()										# turn word in to lowercase word
	return word[::-1] == word								# reverse word and compare with original

result = is_palindrome('mother')							# if the word is an palindrome return true otherwise false

print (result)
'''

'''
def is_anagram(word1, word2):								# create function
	word1 = word1.lower()									# turn word in to lowercase word
	word2 = word2.lower()									# turn word in to lowercase word
	return sorted(word1) == sorted(word2)					# sort the characters of each word and compare them

inputWord1 = input('type word 1: ')
inputWord2 = input('type word 2: ')

result = is_anagram(inputWord1,inputWord2)
print(result)
'''

'''
def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found
'''

'''
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)
'''

'''
# not working

def findMin(alist):
	overallMin = alist[0]
	for i in alist:
		isSmallest = True
		for j in alist:
			if i > j:
				isSmallest = False
			if isSmallest:
				overallMin = i
		return overallMin

print(findMin([5,4,3,2,1,0]))
print(findMin([0,1,2,3,4,5]))
'''

'''
movies = ['Interstellar', 'Inception', 'The Prestige', 'The Dark Knight', 'Batman Begins']									# create a list
ratings = ['1', '10', '10', '8', '6']																						# create a list
new_list = []																												# create empty list

for tree in zip(movies, ratings):																							# combine list with zip
	new_list.append(tree)																									# attache new list tuple to new list for each pair

print(new_list)
'''
