fname = input("Enter the file name: ")

try:
    fh = open(fname)
except:
    print("The file", fname,"does not exist.\nPlease enter a valid file name")
    quit()
counts = dict()

for line in fh:
    line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    word = words[5]
    time = word.split(":")
    time = time[0]
    counts[time] = counts.get(time,0) + 1
for k,v in sorted(counts.items()):
    print(k,v)
