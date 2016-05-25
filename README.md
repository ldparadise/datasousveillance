# datasousveillance

download_urls_from_CR.py - this downloads the URLs that you've amassed and saved as a text file. 
Save it in the same folder as the text file. When you start this script, it will go to the list of urls, and save them as an htm file whose name is the text from the last slash of the URL forwards. so https://www.gpo.gov/fdsys/pkg/CREC-2002-07-31/html/CREC-2002-07-31-pt2-PgS7709-2.htm is saved as CREC-2002-07-31-pt2-PgS7709-2.htm

Cr_parser_modified.py - Add this to the fdsys folder in the folder when you download from https://github.com/unitedstates/congressional-record
This file is identical to the one within the original script with two exceptions that let you point it at a file of varied congressional record files
1) It deletes the mods file that is downloaded from the congressional record website
2) It includes a sleep command to try and fend off the CR server kicking you off the shoulder. This command is at line 1043 and is seconds. 
You can modify as needed, putting it at a larger # of seconds if you just want to leave it running, or a smaller # of seconds if you have a smaller # of files that you want to try to get in one fell swoop.

parse_directory.py - save this at the level above cr_parser_modified within the congressional record folder you downloaded.
Open this file to edit and modify it to point at the folder of CR files you want parsed, and the folders you've added as destination files 

gather_speaker_names - pulls all the speaker names and prints to a file. From there you'd need to de-duplicate it to narrow it down. 

collate_speaker_as_csv - uses a text file of all speakers as a reference, looks for speaker across the files and creates a csv file where each of their entries in a group of files is written in as a row. You just have to provide the speaker list as text and point it at the file path containing your parsed files. You can change the order or change the headers if you wish.
collate_speaker_as_csv_filename_text_only - does same but only prints filename and text, leaves out speaker. This was so the overuse of names didn't mess up our sentiment analysis.
collate_recorder - collates speech in a csv that's the recorder (bill text, procedural, etc)
collate_recorder_quotes - collates recorded text being quoted. 
