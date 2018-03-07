# Data deduplication

## Description
The Python Record Linkage Toolkit is a library to link records in or between data sources. The toolkit provides
most of the tools needed for record linkage and deduplication. The package contains indexing methods, functions
to compare records and classifiers. Record linkage is used to link data from multiple data sources or to find
duplicates in a single data source.The given dataset has the similar problem of data deduplication having the fields as
last_name(ln),date_of_birth(dob), gender(gn), first_name(fn).

## Procedure

###### 1. Importing Modules
Import the recordlinkage module with all important tools for record linkage , the data manipulation framework pandas and the scientific computing package numpy.
###### 2. Indexing
The indexing module is used to make pairs of records-candidate links. The indexing method -blocking is used which includes only record pairs that are identical on one or more stored attributes of the person (or entity in general).
###### 3. Comparing Records
Each record pair is a candidate match. To classify the candidate record pairs into matches and non-matches, the records are compared on all attributes they have in common. The recordlinkage module has a class named Compare.
###### 4. Classifying Records
The K-means classifier in the Python Record Linkage Toolkit package is configured in such a way that it can be used for linking records.


## Dependencies and Installation

Install the Python Record Linkage Toolkit easily with pip
```
pip install recordlinkage
```

The toolkit depends on Pandas (>=18.0), Numpy, Scikit-learn, Scipy and Jellyfish.

## Libraries used
- RecordLinkage
- Pandas
- Numpy
