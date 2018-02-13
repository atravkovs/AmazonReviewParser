import gzip
import re
import sys
import html


def parse(path: str) -> dict:
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)


def getMark(mymark: str) -> int:
    if int(mymark) < 3:
        return 0
    else:
        return 1


path = sys.argv[1]
dataCountPerCategory = int(sys.argv[2])

print("File: " + path)
print("Data Count Per Category: " + str(dataCountPerCategory))

print("Starting training data generation...")

p = re.compile('[\S]+')

maxReviewsCount = dataCountPerCategory*2
f = open("data/train-" + str(dataCountPerCategory) + ".txt", 'w+')

i = 0
positive = 0
negative = 0

for mReview in parse(path):
    i = negative + positive
    if i >= maxReviewsCount:
        break
    if p.search(str(mReview['reviewText'])):
        mark = getMark(mReview['overall'])
        if mark == 1:
            if positive >= dataCountPerCategory:
                continue
            positive += 1
        elif mark == 0:
            if negative >= dataCountPerCategory:
                continue
            negative += 1
        try:
            f.write(str(mark) + "\t"
                    + html.unescape(mReview['reviewText']).lower() + "\n")
        except UnicodeEncodeError:
            f.write(str(mark) + "\t" + mReview['reviewText'] + "\n")

print("End parsing training data!")
f.close()
