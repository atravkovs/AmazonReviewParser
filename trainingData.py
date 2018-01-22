import gzip
import time
import re
import html


def parse(path: str) -> dict:
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)


def getMark(mymark: str) -> int:
    if int(mymark) < 3:
        return -1
    elif int(mymark) == 3:
        return 0
    else:
        return 1


print("Starting training data generation...")
print("------------")

timestamp = int(time.time())

p = re.compile('[\S]+')

rowsPerCat = 83183
maxReviewsCount = rowsPerCat*3
f = open("data/train-" + str(rowsPerCat) + "-" + str(timestamp) + ".txt", 'w+')
i = 1

positive = 0
neutral = 0
negative = 0

for mReview in parse("D:\\amazon_data\\reviews_Electronics_5.json.gz"):
    if i > maxReviewsCount:
        break
    if (i % 100 == 0) or (i < 100 and i % 10 == 0):
        print(i)
    if p.search(str(mReview['reviewText'])):
        mark = getMark(mReview['overall'])
        if mark == 1:
            if positive >= rowsPerCat:
                continue
            positive += 1
        elif mark == 0:
            if neutral >= rowsPerCat:
                continue
            neutral += 1
        elif mark == -1:
            if negative >= rowsPerCat:
                continue
            negative += 1
        try:
            f.write(str(mark) + "\t"
                    + html.unescape(mReview['reviewText']).lower() + "\n")
        except UnicodeEncodeError:
            f.write(str(mark) + "\t" + mReview['reviewText'] + "\n")
    i += 1

print("------------")
print("End parsing training data!")
f.close()
