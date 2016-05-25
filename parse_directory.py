import sys
import unittest
import os
import re


from congressionalrecord.fdsys import cr_parser_modified
##save the cr_parser_removemods in the fdsys folder. Place this file at the top level of the directory

def directory_to_parse():
	cr_parser_modified.parse_directory("downloaded_cr_files/surveillance", logdir="downloaded_cr_files/surveillance/log", outdir="downloaded_cr_files/surveillance/parsed")
	##first one there is the directory location with the files you want parsed 
	##logdir is where the log that the parser generate goes
	##outdir is where the parsed files go 
	##Make folders in advance of executing code.
	

directory_to_parse = directory_to_parse()
