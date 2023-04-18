import sys
'''evenNumbers = [element
               for element in range(100)
               if (element % 2 == 0)
]
'''
evenNumbersGenerator = (element
               for element in range(100)
               if (element % 2 == 0)
)

for item in evenNumbersGenerator:
    print(item)

#print(evenNumbersGenerator)
print(sum(evenNumbersGenerator))

print(sys.getsizeof(evenNumbersGenerator))
#print(sys.getsizeof(evenNumbers))
