import gzip
import time
import re
import sys
import html


def parse(path: str) -> dict:
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)


def getMark(mark: int) -> str:
    if mark < 3:
        return str(0)
    else:
        return str(1)


path = sys.argv[1]
startFrom = int(sys.argv[2])

print("Path: " + path)
print("Start From: " + str(startFrom))

print("Starting test data generation...")
print("------------")

timestamp = int(time.time())

p = re.compile('[\S]+')

f = open("data/test-" + str(timestamp) + ".txt", 'w+')
i = 1

for mReview in parse(path):
    if i > startFrom:
        if i % 100 == 0:
            print(i)
        if p.search(str(mReview['reviewText'])):
            try:
                f.write(getMark(int(mReview['overall'])) + "\t"
                        + html.unescape(mReview['reviewText']).lower() + "\n")
            except UnicodeEncodeError:
                f.write(getMark(int(mReview['overall'])) + "\t" + mReview['reviewText'] + "\n")
    i += 1

print("------------")
print("End parsing test data!")
f.close()
