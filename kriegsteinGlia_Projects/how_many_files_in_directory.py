#!/usr/bin/env python

# I didn't think of this cool code on my own :(
# I edited a thing from StackOverflow
# https://stackoverflow.com/questions/19309667/recursive-os-listdir

kallisto_list = "/media/david/Terabyte/Altering_CIRM_Scripts/kriegsteinRadialGliaStudy1/Submitted_Many_Directoies/kallistoOut"
summary_list = "/media/david/Terabyte/Altering_CIRM_Scripts/kriegsteinRadialGliaStudy1/Submitted_Many_Directoies/summary"

import os
kallisto_sum = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(kallisto_list)) for f in fn]
summary_sum = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(summary_list)) for f in fn]
print len(kallisto_sum + summary_sum)
