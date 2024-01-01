class Solution:
    def minMutation(self, start, end, bank):
        bank = set(bank)
        if end not in bank:
            return -1
        
        q = deque()
        q.append([start, 0])
        vis = set(start)
        
        while q:
            gene, level = q.popleft()
            if gene == end :
                return level
            else:
                for i in range(len(gene)):
                    for letter in 'ACGT':
                        new_gene = gene[:i] + letter + gene[i+1:]
                        if new_gene not in vis and new_gene in bank:
                            q.append([new_gene, level + 1])
                            vis.add(new_gene)
        return -1
                     
