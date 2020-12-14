

# for i in range(1, 10):
#     for j in range(i, 10):
#         print("%s * %s = %s" % (i, j, i*j))
#     print()

print(
    "\n".join([" ".join(["%s * %s = %s" % (i, j, i*j) for j in range(1, i+1)]) for i in range(1, 10)])
)