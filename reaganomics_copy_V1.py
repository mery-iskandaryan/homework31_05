text = open('reaganomics.txt','r+', errors='ignore')
t = text.read()
text.close()
target_text = t.find('Federal income tax and payroll tax level')
copy_text = open('copytext.txt','w')
copy_text.write(t[:target_text])

