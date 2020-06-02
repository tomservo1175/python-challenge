# Dependencies
import os
import csv

total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0


vote_file_path = os.path.join("election_data.csv")
results_file_path = os.path.join("results_data.csv")

# Open and read file
with open(vote_file_path, newline="",) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

#Loop thru each row count total votes
for row in csv_reader:
    total_votes =+ 1

    #count votes per candidate
    if row[2] == "Khan": 
        khan_votes +=1
    elif row[2] == "Correy":
        correy_votes +=1
    elif row[2] == "Li": 
        li_votes +=1
    elif row[2] == "O'Tooley":
        otooley_votes +=1

#List vote percentage with candidate attched to
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

#zip lists together and get winner
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#print table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

with open (results_file_path, "w") as results_data:
    results_data.write(f"Election Results")
    results_data.write("\n")
    results_data.write(f"----------------------------")
    results_data.write("\n")
    results_data.write(f"Total Votes: {total_votes}")
    results_data.write("\n")
    results_data.write(f"----------------------------")
    results_data.write("\n")
    results_data.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    results_data.write("\n")
    results_data.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    results_data.write("\n")
    results_data.write(f"Li: {li_percent:.3f}% ({li_votes})")
    results_data.write("\n")
    results_data.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    results_data.write("\n")
    results_data.write(f"----------------------------")
    results_data.write("\n")
    results_data.write(f"Winner: {key}")
    results_data.write("\n")
    results_data.write(f"----------------------------")