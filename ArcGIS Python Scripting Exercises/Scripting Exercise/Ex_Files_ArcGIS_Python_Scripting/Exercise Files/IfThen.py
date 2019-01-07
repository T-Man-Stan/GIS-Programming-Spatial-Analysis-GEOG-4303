strInput = raw_input('Enter a number:')
if strInput.isdigit():
    print 'You entered',strInput,'which is a valid number.'
else:
    print 'Hey, you entered'+strInput+'! That\'s not a number.'
