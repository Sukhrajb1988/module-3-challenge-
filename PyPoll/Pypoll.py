import csv #Import csv 
import os #import os 
poll = r"C:\Users\sukhr\Desktop\module-3-challenge-\PyPoll\Resources\election_data.csv"
with open (poll) as csvfile: #Start csv file handling

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) #Read the header row first

    #Prepare variables
    voterids=[] #Generate list named "voterids" for the "Voter ID" column
    counties=[] #Generate list named "counties" for the "County" column
    candidates=[] #Generate list named "candidates" for the "Candidate" column
    candidatenames=[] #Generate list for actual candidate names
    totaleachcan=[] #Generate list for total votes for each found candidate
    resultprintcan=[] #Generate list for result printout of each found candidate
    totaleachcanperc=[] #Generate list for percentage of votes for each found candidate

    #Set start conditions
    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        voterid=row[0] #Assign column 0 as voterid
        county=row[1] #Assign column 1 as county
        candidate=row[2] #Assign column 2 as candidate
        voterids.append(voterid) #Add next line to list voterids
        counties.append(county) #Add next line to list counties
        candidates.append(candidate) #Add next line to list candidates
    
    line_count= len(voterids) #Count the total number of votes cast in the "Voter ID" column
    
    #print(line_count)

#Begin data analysis

candidatenames.append(candidates[0]) #Pre-loadfirst candidate name for comparison

#First loop is through the list of candidates to determine candidates voted for (variable loop1 as loop index counter)
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)

#print(n)

#Second loop variable loop2 as loop index counter
for loop2 in range (n): #Range of loop depending on how many candidates were found
    totaleachcan.append(candidates.count(candidatenames[loop2])) #Count total votes of candidates and add to list total



loservotes=line_count 

for loop3 in range(n): 
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 4)}%') #Calculate % per candidate found
    if totaleachcan[loop3]>winnervotes: #Find candidate with highest vote count
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]
    if totaleachcan[loop3]<loservotes: #Find candidate with lowest vote count
        loser=candidatenames[loop3]
        loservotes=totaleachcan[loop3]

#
for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})') 

resultlines='\n'.join(resultprintcan) 

#Generate output lines

analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
Last: {loser} :(\n\
----------------------------\n'

print(analysis) #Output results on screen

#Write text file

output_file = r"C:\Users\sukhr\Desktop\module-3-challenge-\PyPoll\Analysis/pypoll.txt"
with open(output_file, "w") as f:
    f.write(analysis)