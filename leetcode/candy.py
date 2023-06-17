ratings = [1, 2, 2]
candies = [1]*len(ratings)

for i in range(1, len(candies)):
    if ratings[i] > ratings[i-1]:
        candies[i] += candies[i-1]
res = candies[-1]

for i in range(len(ratings)-2, -1, -1):
    if ratings[i] > ratings[i+1]:
        candies[i] = max(candies[i], candies[i+1]+1)
    res += candies[i]
print(res)