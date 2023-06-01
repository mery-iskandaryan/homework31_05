text = open('reaganomics.txt','r+', errors='ignore')
t = text.read()
target_text_length = t.find('Federal income tax and payroll tax level')
final_text = str() 
text1 = list(t)

for index,item in enumerate(text1): 
	if(index < target_text_length):
		final_text += str(item)
print(final_text)