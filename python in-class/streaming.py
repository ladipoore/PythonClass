users = {}
songs = {}
maxsong = 0
popsong =''
maxuser = 0
popuser =''
totalsongs =0
#accept data
filein = "streaming.txt"
file = open(filein,'r')
data = []
for line in file:
    data.append(line.split())
file.close()

#counting users
for i in range(len(data)):
    if data[i][0] not in users.keys():
        countu =1
        users.update({data[i][0]:countu})
    if data[i][0] in users.keys():
        countu +=1
        users[data[i][0]]= countu
    if countu >maxuser:
        maxuser = countu
        popuser = data[i][0]

#counting songs
for i in range(len(data)):
    if data[i][1] not in users.keys():
        count =1
        songs.update({data[i][1]:count})
    if data[i][1] in users.keys():
        count +=1
        songs[data[i][1]]= count
    if count >maxsong:
        maxsong = count
        popsong = data[i][1]
    #average songs listened
    totalsongs +=count

print ("The most popular song is ",popsong)
print ("The most active user is ",popuser," with ",maxuser," songs listened to.")
print ("On average users listen to ", int(totalsongs/len(users)))