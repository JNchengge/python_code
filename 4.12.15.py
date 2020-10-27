def bin_sum(a,b):
    if b==0:
        return a
    return bin_sum(a^b,(a&b)<<1)

a=100
b=200
print(bin_sum(a,b))
