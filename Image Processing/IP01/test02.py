i = 10
f = 29.8
s = 'str'

print('int:%d, float:%f, string:%s' %(i,f,s))
print('float:{1}, int:{0}, string:{2}'.format(i,f,s))
print('float:{ff}, int:{ii}, string:{ss}'.format(ii=i,ff=f,ss=s))

#

test = [3,6,9,12]
for index, value in enumerate(test):
    print(index, value)