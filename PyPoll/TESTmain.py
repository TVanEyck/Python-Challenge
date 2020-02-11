# -----handle dependencies
import os
import csv

# -----determine incoming file details
voter_csv = os.path.join("election_data.csv")
#voter_csv = os.path.join("TestVotes.csv")

# -----create candidate votes Lists
VotesName = []
VotesCount = []

# -----Write a function that assigns votes by candidate
def assignVotes(voteDetail,voteCands,votesCast,voteName,voteCount):
    #print ("Vote Dtl=", voteDetail, "Tot # candidates=", voteCands,
    #                 "Tot # votes=", votesCast, "Candidates=", voteName,
    #                 "Candidates Votes=", voteCount)
    #  For readability, assign values to variables with descriptive names
    voterId = str(voteDetail[0])
    voterCounty = str(voteDetail[1])
    Candidate = str(voteDetail[2])
    cand = ""
    # ---------------------------------------------------------------
    candIdx = 0
    voteCand = 0
    # -----Store Vote in Lists
    NewCandidate = True

    for cand in voteName:
        # TEST -----------------------
        #print ("Name array id=", cand)
        #print (voteDetail)
        #print ("voteCands=", voteCands, "votesCast=", votesCast ) 
        #print ("CurrName=", voteName[candIdx], "CurrVotes=", voteCount[candIdx])
        #print ("Candidate=", Candidate)
        # TEST -----------------------

        if cand == Candidate:
            #print ("fnd---------------------")
            NewCandidate = False
            break
        else:
            #print ("ntfnd-------------------")
            candIdx += 1    
            NewCandidate = True        

    #print ("==================")   

    # ----- Determine insert or update
    votesCast += 1
    
    if NewCandidate:
        #print ("      new-insert", "cand idx", candIdx)
        voteName.insert(candIdx,Candidate)
        voteCount.insert(candIdx,1)
        voteCands += 1
    else:
        #print ("      exist-update", "cand idx", candIdx)
        voteCand = voteCount[candIdx]
        voteCand += 1
        voteCount[candIdx] = voteCand

    # TEST 
    #    print ("array Idx=", candIdx, "Voter array Nm=" , voteName[candIdx], 
    #                    "voteCast array ctr=", voteCount[candIdx] )
    #    
    #print ("NamesBy=", voteName, "VotesBy=", voteCount, "TotCast=", votesCast, "TotCands=", voteCands)
    # TEST 
    return (voteCands, votesCast, voteName, voteCount)

# ---------------------------------------------------------------
# ------------------ Program Main Routine start  ----------------
# ---------------------------------------------------------------

totCands = 0
totVotes = 0
# Open and read csv
with open(voter_csv, newline="") as csvfile:
    csvvoter = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvvoter:
     #   print(row)
        #print ("=======> row in table =" , str(row))  
        # determine where to accumulate
        totCands,totVotes,VotesName,VotesCount = assignVotes(row,totCands,totVotes,VotesName,VotesCount)

# Produce Report output to Terminal
WinCtr = 0
WinNm =""
WinPrct = 0

print ("")
Line1 = "-------------------------------------"
Line2 = "<<<<<<<<< Election Results >>>>>>>>>>"
Line3 = "  Total Votes Cast: " + str(totVotes)

print (Line1)
print (Line2)
print (Line1)
print (Line3)
print (Line1)

for voteIdx, voteNm in enumerate(VotesName):
    WinPrct = (VotesCount[voteIdx]/totVotes)
    Line4 = (str(voteNm) + ":     {:.3%}".format(WinPrct) + "      (" + str(VotesCount[voteIdx]) + ")") 
    print (Line4)
    if VotesCount[voteIdx] > WinCtr:
        WinCtr = VotesCount[voteIdx]
        WinNm = voteNm
    # TEST    
    #elif VotesCount[voteIdx] == WinCtr:
    #    print ("=====> intermediate tie at ", WinCtr, " for ", WinNm, " and ", voteNm)
        
print (Line1)
Line5 = "  Winner: " + WinNm + " with " + str(WinCtr) + " votes"
print (Line5)
print (Line1)

# ---------------------------- write output file

WinPrct = 0

with open("winnerResults.txt","w") as writer_file:
    writer_file.write (Line1 + "\n")
    writer_file.write (Line2 + "\n")
    writer_file.write (Line1 + "\n")
    writer_file.write (Line3 + "\n")
    writer_file.write (Line1 + "\n")
    
    for voteIdx, voteNm in enumerate(VotesName):
        WinPrct = (VotesCount[voteIdx]/totVotes)
        Line4 = (str(voteNm) + ":     {:.3%}".format(WinPrct) + "      (" + str(VotesCount[voteIdx]) + ")") 
        writer_file.write (Line4 + "\n")
        
    writer_file.write (Line1 + "\n")
    writer_file.write (Line5 + "\n")
    writer_file.write (Line1 + "\n")





'''
  writer_file.write ("---------------------\n") 

    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))



data = []
col_width = max(len(word) for row in data for word in row) + 2  # padding
for row in data:
    print "".join(word.ljust(col_width) for word in row)
'''