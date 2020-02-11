# ---------------------------------------------------------------
# -----    Python Challenge Homework Assignment #2        -------
# -----  02-10-2020                    Thomas A. VanEyck  -------
# ---------------------------------------------------------------

# -----handle dependencies
# ---------------------------------------------------------------
import os
import csv

# -----determine incoming file details
voter_csv = os.path.join("election_data.csv")

# -----create candidate votes Lists
VotesName = []
VotesCount = []

# -----------------------------------------------------------------
# -----   Write a function that assigns votes by candidate
# -----------------------------------------------------------------
def assignVotes(voteDetail,voteCands,votesCast,voteName,voteCount):
    # initialize
    voterId = str(voteDetail[0])
    voterCounty = str(voteDetail[1])
    Candidate = str(voteDetail[2])
    # --------------------------------
    cand = ""
    candIdx = 0
    voteCand = 0
    # -----Store Vote in Lists
    NewCandidate = True

    for cand in voteName:

        if cand == Candidate:
            NewCandidate = False
            break
        else:
            candIdx += 1    
            NewCandidate = True        

    # ----- Determine insert or update
    votesCast += 1
    
    if NewCandidate:
        voteName.insert(candIdx,Candidate)
        voteCount.insert(candIdx,1)
        voteCands += 1
    else:
        voteCand = voteCount[candIdx]
        voteCand += 1
        voteCount[candIdx] = voteCand

    return (voteCands, votesCast, voteName, voteCount)

# ---------------------------------------------------------------
# ------------------ Program Main Routine start  ----------------
# ---------------------------------------------------------------

totCands = 0
totVotes = 0
# -----Open and read csv
with open(voter_csv, newline="") as csvfile:
    csvvoter = csv.reader(csvfile, delimiter=",")

    # -----Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # -----Read through each row of data after the header
    for row in csvvoter:

        # -----determine where to accumulate with function assignVotes
        totCands,totVotes,VotesName,VotesCount = assignVotes(row,totCands,totVotes,VotesName,VotesCount)

# ---------------------------------------------------------------
# ---------------  Produce Report output to Terminal
# ---------------------------------------------------------------
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
         
print (Line1)
Line5 = "  Winner: " + WinNm + " with " + str(WinCtr) + " votes"
print (Line5)
print (Line1)

# ---------------------------------------------------------------
# --------------------- write output file
# ---------------------------------------------------------------

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
