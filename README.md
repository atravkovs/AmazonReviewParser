# Amazon Review Parser
It is set of two scripts, which prepare Amazon reviews data for Apache OpenNLP model training and checking.

## Test Data
This script prepares data for checking the model. It has two params:
* __path__ - path to the json file with reviews (It accepts [complete review data format](http://jmcauley.ucsd.edu/data/amazon/))
* __offset__ - number of lines to skip before starting parsing

Program output after execution will be in `data/test.txt` file.
Data format for each line in results file is: `mark[Tab]review`.

## Training Data
This script prepares data for training the model. It also normalizes Amazon user marks as follows: 1 - 2 is negative (0)
and 3 - 5 is positive (1) tonality. The script has two params:
* __path__ - path to the json file with reviews (It accepts [complete review data format](http://jmcauley.ucsd.edu/data/amazon/))
* __dataCountPerCategory__ - data count in each category (in positive and negative)

Program output after execution will be in `data/train-*dataCountPerCategory*.txt` file.
Data format for each line in results file is: `mark[Tab]review`.