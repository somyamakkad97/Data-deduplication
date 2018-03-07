
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This code demonstrates how to use recordlinkage module with a comma separated values
(CSV) file.We start with a CSV file containing our messy data. In this example,
it is listings of patient information having ln,dob,gn,fn as its fields
compiled from several different sources.
The output will be a CSV with our clustered results.
"""

import recordlinkage as rl
import pandas as pd
import numpy as np

# The CSV file is read into a dataframe dfA
dfA = pd.read_csv("Deduplication Problem - Sample Dataset.csv",encoding="utf8")

# Making record pairs using indexing method- blocking
# Returns record pairs having same values for gender and date_of_birth
indexer = rl.BlockIndex(on=['dob','gn'])
pairs = indexer.index(dfA)

# The record pairs are compared using various methods for corresponding fields
# Attribute comparisons are stored in a DataFrame-features thereafter
compare_cl = rl.Compare()
compare_cl.string('fn', 'fn', method='jarowinkler', threshold=0.85,label='fn')
compare_cl.string('ln', 'ln', method='jarowinkler', threshold=0.85, label='ln')
compare_cl.exact('dob', 'dob', label='dob')
compare_cl.exact('gn', 'gn', label='gn')
features = compare_cl.compute(pairs, dfA)

# To decide which record belong to the same person
matches = features[features.sum(axis=1) > 3]

# To produce the CSV file having no duplicate/similar entries
dfA1=pd.DataFrame(dfA)
matches.index.names=['key1','key2']
result=matches.index.get_level_values('key2')
result1=np.array(result)
result1=np.unique(result1)
dfA1.drop(result1,inplace=True)
dfA1.to_csv('output.csv',sep=',',encoding='utf-8')

