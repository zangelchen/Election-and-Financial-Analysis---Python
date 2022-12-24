#import
import os
import csv
 
# save file path location
election_data = os.path.join('..','Python_Challenge','Resources', 'election_data.csv')
save_file = os.path.join("..",'Python_Challenge', 'PyPoll','PyPoll.txt')

#track the candidate name, winning candidate, and winning vote count
candidate_options = []
winning_count = 0
winning_candidate = ""

#read csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #read header
    header = next(csvreader)
    first_row = next(csvreader)
    
    #create empty list and iteration for counting total votes
    candidate_votes = {}
    total_votes = 1

    #find total votes
    for row in csvreader:
        total_votes += 1
       
       #loop through list to find the neames -> later included in a dictionary
        candidate_names = row[2] 
        if candidate_names not in candidate_options:
            candidate_options.append(candidate_names)
            candidate_votes[candidate_names] = 0 
        candidate_votes[candidate_names]+=1 


    #save as txt file
    with open(save_file, "w") as txt_file:
        txt_file.write("Election Results \n")
        txt_file.write("----------------------------------------\n")

        #create dictionary
        for candidate in candidate_votes:
            number_of_votes = candidate_votes.get(candidate)
            percentage_of_votes =float(number_of_votes)/float(total_votes)*100        
            output = (f"{candidate}: {percentage_of_votes:.1f}% ({number_of_votes})")
            print(output)
            
            #print to txt file
            txt_file.write(f'{output}\n')

            #loop to find the winner
            if number_of_votes > winning_count:
                winning_count = number_of_votes
                winning_candidate = candidate
        print(winning_candidate)
        
        txt_file.write("----------------------------------------\n")
        txt_file.write(f"Winner: {winning_candidate}\n")
        txt_file.write("----------------------------------------\n")
