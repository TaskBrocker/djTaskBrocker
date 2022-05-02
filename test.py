import sys

print('Number of argument',len(sys.argv),'test')
print(sys.argv);

for i in range(len(sys.argv)-1):
    print(sys.argv[i+1])