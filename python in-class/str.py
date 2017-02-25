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
        songs = [data[i][1]]
        users.update({data[i][0]:songs})
    if data[i][0] in users.keys():
        users [data[i][0]]= songs.append(data[i][1])

#Finding the max user
for key in users:
    usage = len(users[key])
    if usage > maxuser:
        maxuser = usage
        popuser = key

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

user = input("Which user wants music recommendations: ")

def recommendation(user):
    songlist =[]
    for i in range (len(data)):
        if data[i][0] == user:
            songlist.append(data[i][1])
        