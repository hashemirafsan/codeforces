m = input()
m = m.split(" ")
n = int(m[0])
k = int(m[1]) - 1
participant = input()
participant = participant.split(" ")
total = 0
for i in participant :
	if(int(i) > 0 and int(i) >= int(participant[k])) : 
		total += 1
print(total)