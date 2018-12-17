#!/usr/bin/env python

# curl 'https://cirm.ucsc.edu/cgi-bin/cdwGetFile?acc=sc000AKB' --create-dirs -o
# raw/reads-ByExp-sra-SRX-SRX995-SRX995861-SRR1974543-/SRR1974543_1.fastq.gz --insecure
# My database will include accession, meta, and file_name. I will not be including
# folder name because it is experiment_name + meta + file_name. Here are the columns:
# accession     file_type       meta_name       file_name
# sc000AKB      reads           SRR1974543      SRR1974543_1.fastq.gz
# meta appears to be shared amongst files uploaded simultaneously, so it can't be
# a primary key. I'm picking accession as primary key cause I feel like it, lol.

# reads fastq.gz example line
#reads_example_line = "curl 'https://cirm.ucsc.edu/cgi-bin/cdwGetFile?acc=sc000AKI' --create-dirs -o raw/reads-ByExp-sra-SRX-SRX995-SRX995862-SRR1974544-/SRR1974544_2.fastq.gz"
# analysis line line_example
#analysis_META_line = "curl 'https://cirm.ucsc.edu/cgi-bin/cdwGetFile?acc=sc000IRT' --create-dirs -o analysis/kallistoOut/SRR1974786/abundance.tsv"
#analysis_META_NULL_line = "curl 'https://cirm.ucsc.edu/cgi-bin/cdwGetFile?acc=sc000JAJ' --create-dirs -o analysis/geneMatrix.tsv"
# summary line example
#summary_example_line = "curl 'https://cirm.ucsc.edu/cgi-bin/cdwGetFile?acc=sc003DMP' --create-dirs -o summary/index.html"

#test_line = "curl 'https://cirm.ucsc.edu/cgi-bin/cdwGetFile?acc=sc000AKI' --create-dirs -o raw/reads-ByExp-sra-SRX-SRX995-SRX995862-SRR1974544-/SRR1974544_2.fastq.gz\
#curl 'https://cirm.ucsc.edu/cgi-bin/cdwGetFile?acc=sc000JAJ' --create-dirs -o analysis/geneMatrix.tsv\
#curl 'https://cirm.ucsc.edu/cgi-bin/cdwGetFile?acc=sc003DMP' --create-dirs -o summary/index.html"

# this module is used for interacting with a MySQL database
import MySQLdb
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='elfcheese',
    db='Quake_Brain_Table')
cursor = mydb.cursor()

# only one table is required, so I'll enter it manually
# MAKE SQL COMMAND FOR TABLE CREATION HERE
# create SQL table for current file
# cursor.execute("""CREATE TABLE 23andMe_Specimen_Table(rsid varchar(20) not null, chromosome varchar(5) not null, position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));""".format(table_name=table_name))
#

test_file = open("quakebrainName files as submitted and put into subdirectories.sh")
test_lines = test_file.readlines()

# determine max lengths
accession_name_length_MAX = 0
file_name_length_MAX = 0
file_type_length_MAX = 0
meta_name_length_MAX = 0

for line in test_lines:
    #################################################################################
    # CONSTANTS

    # accession_name
    start_of_accession = line.find("=")+1
    # all accessions are only 8 characters long
    end_of_accession = start_of_accession + 8
    accession_name = line[start_of_accession:end_of_accession]

    # get file_name
    start_of_file_name = line.rfind('/') + 1
    file_name = line[start_of_file_name:-1]
    # get file type
    if "reads" in line:
        file_type = "reads"
    elif "analysis" in line:
        file_type = "analysis"
    elif "summary" in line:
        file_type = "summary"
    else:
        #print "david is a bad programmer, lol :P"
        pass

    ##################################################################################
    # VARIABLE NAMES
    if "reads" in line:
        # get meta
        meta_start = line.find("SRX995-")+17
        # LOL, starting on line AUK it switches to SRX996 ... this is why you troubleshoot! :D
        # THIS ERROR DROVE ME CRAZY ... SHOULD HAVE REWRITTEN, BUT I'M LAZY
        # this would be negative 1, but note that it's getting + 17 above, so -1 + 17 = 16
        if meta_start == 16:
            print "BAD META: " + str(meta_start)
            # I NEED TO EXPLAIN THIS BEFORE I FORGOT WHY I DID IT, HAHA
            # GOOD LUCK FUTURE DAVID :)
            meta_start = line.find("SRX996-")+17
        else:
            print "david has not handled all possible conditions, lol :P"
            print "meta is: " + str(meta_start)
        meta_end = meta_start + 10
        meta_name = line[meta_start:meta_end]
    elif "analysis" in line:
        if "kallistoOut" in line:
            meta_start = line.find("SRR")
            meta_end = meta_start + 10
            meta_name = line[meta_start:meta_end]
        else:
            meta_name = ""
    else:
        #print "david is a bad programmer"
        pass

    #print "test line was: " + line.rstrip()
    #print "accession: " + accession_name
    #print "file_type: " + file_type
    #print "meta_name: " + meta_name
    #print "file_name: " + file_name
    #print "\n"

    # this should be a function, but I have other things I wanna do
    if len(accession_name) > accession_name_length_MAX:
        accession_name_length_MAX = len(accession_name)
    if len(file_name) > file_name_length_MAX:
        file_name_length_MAX = len(file_name)
    if len(file_type) > file_type_length_MAX:
        file_type_length_MAX = len(file_type)
    if len(meta_name) > meta_name_length_MAX:
        meta_name_length_MAX = len(meta_name)


    # print("""INSERT INTO Quake_Shell_Table(accession, file_type, meta_name, file_name) VALUES('{accession_name}', '{file_type}', '{meta_name}', '{file_name}');""".format(accession_name=accession_name, file_type=file_type, meta_name=meta_name, file_name=file_name))
    cursor.execute("""INSERT INTO Quake_Shell_Table(accession, file_type, meta_name, file_name) VALUES('{accession_name}', '{file_type}', '{meta_name}', '{file_name}');""".format(accession_name=accession_name, file_type=file_type, meta_name=meta_name, file_name=file_name))

mydb.commit()
cursor.close()




print "max length of accession name: " + str(accession_name_length_MAX) # 8
print "max length of file name: " + str(file_name_length_MAX) # 21
print "max length of file type: " + str(file_type_length_MAX) # 8
print "max length of meta name: " + str(meta_name_length_MAX) # 10


# accession     file_type       meta_name       file_name
# sc000AKB      reads           SRR1974543      SRR1974543_1.fastq.gz

# this would be to automate table creation, like that 23andMe thing I did
# cursor.execute("""CREATE TABLE Quake_Shell_Table(accession varchar(8) not null, file_type varchar(8) not null, meta_name varchar(10) null, constraint pk_example primary key (accession));""".format(table_name=table_name))
# THIS Is how I made the table (manually)
# CREATE TABLE Quake_Shell_Table(accession varchar(8) not null, file_type varchar(8) not null, meta_name varchar(10) null, file_name varchar(21), constraint pk_example primary key (accession));
