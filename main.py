import  tkinter

from tkinter.filedialog import askopenfilename
filetypes = (
    ('Text files', '*.TXT'),
    ('All files', '*.*'),
)


#counting sort
def countingSort(array, d_num):
    size = len(array)

    #create array for result the same size as initial array and fill it with 0
    result_arr=[]
    for i in range(0, size):
        result_arr.append(0)

  # create auxiliary storage for maximum 10 digitis
    auxil_str=[]
    for i in range(0, 10):
        auxil_str.append(0)

    # get frequency of element in array
    for i in range(0, size):
        auxil_str[(array[i] // d_num) % 10] += 1

    # Get sum of previous element and current
    for i in range(1, 10):
        auxil_str[i] += auxil_str[i - 1]

    # Sorting
    i = size - 1
    while i >= 0:
        result_arr[auxil_str[array[i] // d_num % 10] - 1] = array[i]
        auxil_str[array[i] // d_num % 10] -= 1
        i -= 1

    return result_arr

#searching for max element
def getMaxElmnt(array):
    max = array[0];
    for i in range(1,len(array)):
      if (array[i] > max):
          max = array[i];
    return max


# Radix sort
def radixSort(array):
    # get maximum element
    max_element=getMaxElmnt(array)
    #to know how many digitis are in max element
    d_len = len(str(max_element))
    if d_len>4:
        return None
    #calling counting sort based on digit position  .
    else:
        d_num = 1
        while (d_len> 0 and d_num<=1000):
            curlist=countingSort(array, d_num)
            array=curlist;
            d_num *= 10
            d_len-=1
        return array


# reading from file
filename = askopenfilename(
    filetypes=filetypes,)

my_file = open(filename, "r")
source = my_file.read()
my_file.close()

#conver read string into the int array
source_arr=[int(x) for x in source.split()]

#checking the file
if len(source_arr) == 0:
    print("your file is empty.Nothing to sort. Try to add numbers into the file")
else:
    res = radixSort(source_arr)
    if res is None:
       print("it was promised that numbers are maximum 4-digit. You are trying enter greater number")
    else:
       print(res)
