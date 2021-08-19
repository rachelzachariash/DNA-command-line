# dna-rachelzachariash
dna-rachelzachariash created by GitHub Classroom
The project's target:
Interface used to hold a string representing DNA where each type of DNA has a string representing each string has a name and ID

For that you build a CMD that the user can write command for managing the dna string in a good way for example cratering 
a new dna string or changing a dna that exist.

Design patter

for managing all the writing to the CMD I used a class CLI that all the classes that write to the user,
inherited the CLI class and contain the functions __init__ and start

for each type of command their a different class different class to create the
required command, all of these classes inherit a class that has a function __init__ that contain list of the words
in the command all the command and a object of type of DB, and a function exectue (to that make the command) and function that helps a few class.
For connect between the interface of the user to execute the command I used a factory that gets the command and
check the type create  a  object of the type of command and execute the command.

For managing the DB I used singleton that each class can access the DB with creating a new object and their only one DB.

For managing the batch command I used a observer class that has a list of all the object 
that are in the batch (each object is a command) and a notify function that execute all the object and a get_command function 
that give all the commands in strings. That each time that create a new batch cerate a new observer class and 
open the batch cmd and for each command send to a factory create a object of the type of command and but it in the observer list

commands implemented:

sequence creation:
new:

new <sequence> [@<sequence_name>] – get a sequence and optional a name of a string if no name
was given the name will be str + num of the next number that did not use yet
 
load:
 
load <file_name>  [@<sequence_name>] – get a file name that contain a dna sequence and optional 
name of the new dna and putting in the DB the dna string
 
dup:
 
dup <seq> [@<new_seq_name>] – get a sequence of #id or @name of sequence in DB and optional name of 
new sequence and and create a new dna that doubled  the dna sequence of the gets sequence and if no
name given give it the name of the given dna to doubled with _1, _2 if the mame is already taden
 
 sequence manipulation:
 
slice:
 
slice <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]] – gets sequence by id or name and index to slice and
optional : means to cerate a new sequence and not change the old sequence if only : so name the new dna 
str +num next optional new name or @@ name the dna given name with _s1,_s2 if already exist.
 
Pair:
 
pair <seq> [: [@<new_seq_name>|@@]] – gets a same like slice without the index and the sequence that gat
change all the C latter to G and T to A and vice versa
 
sequence management:
 
Delete:
 
del <seq> - get dna sequence by name or id and delete it from the DB before deleting gets a confirm form the user
 
Save:
 
save <seq> [<filename>] – gets a dna sequence by name or id and save it in file if optional given a name
of file otherwise the name of file will be the name of the dna sequence
 
sequence analysis:
 
length:
 
len <seq_id> - get a dna sequence by id or name and write the length of the sequence
 
find:
 
find <seq> <expressed_sub_seq> - get a dna sequence by id or name and a sequence of dna type and 
return the index that the sub string start 
 
count:
 
count <seq> <expressed_sub_seq or count <seq_to_find_in> <seq_to_be_found – gets - get a dna
sequence by id or name and a sequence of dna or a by id or name and return the ny-number times 
the the sub sequence is in the first sequence 
                                                                          
find all:
                                                                          
findall <seq_to_find_in> <seq_to_be_found or findall <seq> <expressed_sub_seq> - get asame like
count and return all the indexes that start with the sub string>  
 
control commands:
 
list:
 
list - shows all the sequences in the system, by order.   
For each sequence, it shows its number, its name and the sequence itself and sign   -/*/o 
- if sequence is save * did manipulation on sequence and did save in file o if not save at all
 
quit:
 
quit – print for the user how much sequence are not saved and how and ask for a confirm to quit.
 
Batch creation:
 
Batch:
 
batch <batch_name> - get batch name and create a new batch with this name and them ask the user
to but in the commands for this batch instill he insert end and then the batch is end.
 
Run:
 
run <@batchname> - get a name of batch and execute all the command that are in the batch
 
Listing:
 
batchlist – show a list of all the batch that exist
 
Showing:
 
batchshow <@batch_name> -gets a name of batch and print to the user all the command of that batch
 
Saving:
 
batchsave<@batch_name> [<filename>] - get name of batch and optional a filename  
and save the command of the batch in the given filename if not given save file name of batch
 
Loading
 
batchload <file_name>  [@<sequence_name>] – gets file name and optional name of batch and load all the commad to a object of batch 

  


 
