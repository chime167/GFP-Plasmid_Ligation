# GFP-Plasmid_Ligation
Script for ligating a GFP gene to a plasmid

**ABOUT**
This is a simple script that takes a GFP DNA sequence, a plasmid sequence, and restriction sites, cuts them according to their restriction sites,
and integrates the gene within the plasmid.

**USAGE**
The program accepts a file as input when run. Enter the file name or path to file. The format of the file should be lines in the following order:
  1: the plasmid strand
  2: the plasmid's restriction site
  3: the GFP strand
  4: the two left and right restriction sites for the GFP strand
The program then prints the result of ligating the strands, both the original and the complement.
