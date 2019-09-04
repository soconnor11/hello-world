# Read in humanTFs file
id2motif = {}
motif2id = {}
with open('id_conversion/humanTFs_All.csv','r') as inFile:
    # Use the readline() function to read in a single line
    # strip() gets rid of the newline character at the end of the line
    # split(',') splits up the line into columns based on commas
    header = inFile.readline().strip().split(',')
    print (header)
    while 1:
        inLine = inFile.readline()
        if not inLine:
            break
        split = inLine.strip().split(',') 
        # TODO Fill out the id2moitf dictionary (key = Entrez ID, value = Motif Name)
id2motif[split[2]] = split[0] 
        # TODO Fill out the motif2id dictionary (key = Motif Name, value = Entrez ID)
motif2id[split[0]]= split[2]
