"""
Find chords for a given scale
"""
#Generate sets
Keys = ("Ab", "A", "A#", "Bb", "B", "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#")
Sharps = ("F", "C", "G", "D", "A", "E", "B")

while True:
	#Generate/reset lists
	pitchkey = []
	alphakey = []
	scalekey = []
	major_chords = []
	minor_chords = []
	
	#Get root
	print("Chord Finder")
	print("Keys: ", end="")
	for e in Keys:
		print(e + " ", end="")
	print("")
	key = input("Choose a key (q to quit): ")
	if key == "q":
		break
	while key not in Keys:
		print("error, not a key")
		key = input("Choose a key (q to quit): ")
		if key == "q":
			break
	
	#Sort notes based on pitch (#/b)
	if "#" in key:
		pitch = Sharps[::-1]
		keysign = "b"
	elif "b" in key:
		pitch = Sharps[::-1]
		keysign = "#"
	else:
		pitch = Sharps
		keysign = "b"
	for e in Keys:
		if keysign not in e:
			pitchkey.append(e)
	
	#Sort notes based on key
	index = pitchkey.index(key)
	i = len(pitchkey)
	while i > 0:
		try:
			alphakey.append(pitchkey[index])
			index += 1
			i -= 1
		except:
			index = 0
	
	#Sort notes into scale
	step = (0, 2, 4, 5, 7, 9, 11)
	for e in step:
		scalekey.append(alphakey[e])
	
	#Finds chords based on root
	majstep = (0, 3, 4)
	minstep = (1, 2, 5)
	dimstep = 6
	for e in majstep:
		major_chords.append(scalekey[e])
	for e in minstep:
		minor_chords.append(scalekey[e])
	dim_chord = scalekey[dimstep]
	
	#Display Maj/min/dim chords to user
	print("")
	print(key + " is root")
	print("Scale: ", end="") 
	for e in scalekey:
		print(e + " ", end="")
	print("")
	print("")
	print("Major chords: ")
	for e in major_chords:
		print(e)
	print("")
	print("minor chords: ")
	for e in minor_chords:
		print(e)
	print("")
	print("diminished chord: ")
	print(dim_chord)
	print("")
	