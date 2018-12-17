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
test_file = open("quakebrainName files as submitted and put into subdirectories.sh")
test_lines = test_file.readlines()

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
        print "david is a bad programmer, lol :P"

    ##################################################################################
    # VARIABLE NAMES
    if "reads" in line:
        # get meta
        meta_start = line.find("SRX995-")+17
        meta_end = meta_start + 10
        meta_name = line[meta_start:meta_end]
    elif "analysis" in line:
        if "kallistoOut" in line:
            meta_start = line.find("SRR")
            meta_end = meta_start + 10
            meta_name = line[meta_start:meta_end]
        else:
            meta_name = "NULL"
    else:
        # print "david is a bad programmer"
        pass

    print "test line was: " + line.rstrip()
    print "accession: " + accession_name
    print "file_type: " + file_type
    print "meta_name: " + meta_name
    print "file_name: " + file_name
    print "\n"
