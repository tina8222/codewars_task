def pattern(n):
    heart = []
    for i in range(n//2, n+1, 2):
        line = " " * ((n - i) // 2) + "$" * i + " " * (n - i) + "$" * i
        heart.append(line)

    for i in range(n, 0, -1):
        line = " " * (n - i) + "$" * (i * 2 - 1)
        heart.append(line)

    return "\n".join(heart)
print(pattern(6))