"""5. Write a second module, myclient.py, which imports mymod and tests its functions;
run myclient from the system command line. If myclient uses from to fetch from mymod,
will mymod’s functions be accessible from the top level of myclient? What if it imports with import instead?
Try coding both variations in myclient and test interactively, by importing myclient ."""
import myclient
myclient.countLines("Redable_File.txt")
myclient.countChars("Redable_File.txt")