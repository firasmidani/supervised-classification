#!/usr/bin/env python

# ___author___ = Firas Said Midani
# ___e-mail___ = firas.midani@duke.edu
# ___date_____ = 2015.12.07
# ___version__ = 1.0

#####################################
# INITIALIZATION
#####################################
import sys, imp, os

#####################################
# in-house tools
#####################################

pypath = os.path.dirname(os.path.realpath(sys.argv[0]));
foo = imp.load_source('classification_library',pypath+'/class.library.py')
from classification_library import *

#######################################################################
## Model parameters
#######################################################################
feature_options  = {'description':['phylum', 'class', 'order', 'family', 'genus', 'species', 'OTU']}
#feature_options  = {'description':['phylum', 'class', 'order', 'family', 'genus', 'species']}
#feature_options  = {'description':['species']}

holdin_flag1     = {'color':[1,2],'day':[2],'Batch':[1]}
holdin_flag2     = {'color':[3,4],'day':[2],'Batch':[1]}

holdout_flag1     = {'color':[1,2],'day':[2],'Batch':[2]}
holdout_flag2     = {'color':[3,4],'day':[2],'Batch':[2]}

outcomes_dict    = {1:1,2:1,3:0,4:0}
outcomes_dict    = {1:1,2:1,3:0,4:0}

frequency_cutoff = 0.45;

num_features_1   = 350;
coarse_steps_1   = 100;
coarse_steps_2   = 1;
fine_steps       = 1;
internal_cv      = 10;
normalize        = 1;
include_otus     = 1;
include_static   = 0;
pickle_model     = 0;

# CHOOSE VALIDATION SCHEME

#CVS = 'LOO';
#CVS = 'holdout_validation';
#CVS = 'SKF.10';
CVS = 'SSS.250.10';

## CHOOSE CLASSIFIER

#CVCLFS   = SVC(kernel='linear',probability=True,shrinking=True,cache_size=2000,C=100,random_state=24289074);
CVCLFS   = LogisticRegression('l2',C=100)
CLFS     = CVCLFS;
