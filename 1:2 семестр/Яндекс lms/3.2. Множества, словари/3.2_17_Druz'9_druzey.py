def main():
    friends = {}
    while x := input().split():
        if x[0] not in friends:
            friends[x[0]] = {x[1]}
        else:
            friends[x[0]].add(x[1])
        if x[1] not in friends:
            friends[x[1]] = {x[0]}
        else:
            friends[x[1]].add(x[0])
    friends_2 = dict.fromkeys(friends, set())
    for friend in friends:
        for n in friends[friend]:
            friends_2[friend] = friends_2[friend].union(friends[n])
        friends_2[friend].discard(friend)
        for z in friends[friend]:
            friends_2[friend].discard(z)
    res = []
    for friend in friends_2:
        res.append(f'{friend}: {", ".join(sorted(friends_2[friend]))}')
    res.sort()
    for string in res:
        print(string)


if __name__ == "__main__":
    main()