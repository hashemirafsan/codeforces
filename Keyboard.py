side = input()
text = input()
keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
side = -1 if side == 'R' else 1
new_string = ''
for i in text:
   new_string += keyboard[keyboard.find(i) + side]

print(new_string)
