def lsp(pattern):
	n = len(pattern)
	k = 0
	j = 1
	f = [0] * n									#array of longest border, equal length to the text
	while j < n:
		while pattern[k] != pattern[j] and k>0:  #case 3, Fall Back circumstances
			k = f[k -1]
		if pattern[k] != pattern[j] and k == 0: #case one, this part is extra. It's only here for
			f[j] = 0							#better readability
		elif pattern[k] == pattern[j]: 			#case 2, equal characters
			k += 1
		f[j] = k
		j += 1
	return f

def kmp(pattern, text):
	n = len(pattern)
	array = lsp(pattern+'\x00'+text)
	for index, length in enumerate(array):
		if length == n:
			return index - 2 * n				#(index - n + 1) - n + 1  pattern\x00text
	return -1									# 	_ _ _ null _ i _ _ 

print(kmp("caba", "abababcabac"))
	
