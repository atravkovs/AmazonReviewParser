import gzip
import time
import re
import html


def parse(path: str) -> dict:
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)


def getMark(mark: int) -> str:
    if mark < 3:
        return str(-1)
    elif mark == 3:
        return str(0)
    else:
        return str(1)


print("Starting training data generation...")
print("------------")

timestamp = int(time.time())

p = re.compile('[\S]+')

# maxReviewsCount = 1266891
maxReviewsCount = 10
f = open("data/train-" + str(maxReviewsCount) + "-" + str(timestamp) + ".txt", 'w+')
i = 1

for mReview in parse("D:\\amazon_data\\reviews_Electronics_5.json.gz"):
    if i > maxReviewsCount:
        break
    if (i % 100 == 0) or (i < 100 and i % 10 == 0):
        print(i)
    if p.search(str(mReview['reviewText'])):
        try:
            f.write(getMark(int(mReview['overall'])) + "\t"
                    + html.unescape(mReview['reviewText']).lower() + "\n")
        except UnicodeEncodeError:
            f.write(getMark(int(mReview['overall'])) + "\t" + mReview['reviewText'] + "\n")
    i = i + 1

print("------------")
print("End parsing training data!")
f.close()
