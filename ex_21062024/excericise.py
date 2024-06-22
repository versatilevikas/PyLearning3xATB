#Right triangle star pattern

def star_pattern(n):
    for i in range(n+1):
        if i!=0:
            print("")
        for j in range(i):
            print("*",end=' ')


#star_pattern(5)

#palindrome string
#method1
def palindrome_check1():
    s=input(r'i/p=')
    s=s.lower()
    rev=""
    i=len(s)-1
    while(i>=0):
        #print(i)
        rev+=s[i]
        i-=1
    #print(rev)
    if rev==s:
        return True
    return False

# x=palindrome_check()
# print(x)

def palindrome_check2():
    s=input(r'i/p=')
    t=s[::-1]
    if s==t:
        return True
    return False

# x=palindrome_check2()
# print(x)

def palindrome_check3():
    s=input(r'i/p =')
    rev="".join(reversed(s))
    if s==rev:
        return True
    return False

# x=palindrome_check3()
# print(x)

#Anagram Check

def check_anagram(word,word1):
    d={}
    for j in word:
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
    for k in word1:
        if k in d.keys():
            d[k]-=1
        else:
            d[k]=1

    for x in d:
        if d[x]!=0:
            return False
    return True

y=check_anagram("raam","mara")
print(y)