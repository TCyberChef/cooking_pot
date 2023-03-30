#Use the file users.db and find the students average score.


with open('users.db', 'r') as f:
    scores = []
    for line in f:
        parts = line.strip().split('\t')
        scores.append(int(parts[1]))
    average = sum(scores) / len(scores)
    print('The average score is:', average)
