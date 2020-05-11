# Print out all of the strings in the following array in alphabetical order, each
# on a separate line.
arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot',
       'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# The expected output is:

# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'

# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


def print_sort(arr):
    arr.sort()
    print(arr)
    for i in range(len(arr)):
        print(arr[i])


print_sort(arr)
