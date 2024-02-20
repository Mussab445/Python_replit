# whli and for loop
# 1
# x=0
# while (x<19):
#     x=x+1
#     print(x)

# for x in range(2, 7):
#     print(x)    
days=["mon", "tue", "wed", "thu", "fri"]

for d in days:
    # if (d=="wed"):break
    if (d=="wed"):continue
    print(d)