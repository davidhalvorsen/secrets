#!/usr/bin/env python

# I didn't think of this cool code on my own :(
# I edited a thing from StackOverflow
# https://stackoverflow.com/questions/19309667/recursive-os-listdir

analysis_list = "/media/david/Terabyte/Altering_CIRM_Scripts/quakeBranGeo1/Submitted_Many_Directories/analysis"
raw_list = "/media/david/Terabyte/Altering_CIRM_Scripts/quakeBranGeo1/Submitted_Many_Directories/raw"
summary_list = "/media/david/Terabyte/Altering_CIRM_Scripts/quakeBranGeo1/Submitted_Many_Directories/summary"
import os
analysis_sum = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(analysis_list)) for f in fn]
raw_sum = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(raw_list)) for f in fn]
summary_sum = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(summary_list)) for f in fn]
print len(analysis_sum + raw_sum + summary_sum)
