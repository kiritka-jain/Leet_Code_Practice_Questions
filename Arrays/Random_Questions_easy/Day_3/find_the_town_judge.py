"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
eg:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

"""
n = int(input())
trust = [[1,3],[2,3],[3,1]]

trust_dict = {}
for people in trust:
    if people[1] not in trust_dict.keys():
        trust_dict[people[1]] = [people[0]]
    else:
        trust_dict[people[1]].append(people[0])
persons = []
for person in trust:
    persons.append(person[0])
for judge,person in trust_dict.items():
    if len(person) == n-1 and judge not in persons:
        print(judge)
    else:
        print(-1)


