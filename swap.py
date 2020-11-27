def swap(arr, pos_1, pos_2):
  tmp = arr[pos_1]
  arr[pos_1] = arr[pos_2]
  arr[pos_2] = tmp
  return arr

arrList = [19,65, 88, 353, 225, 332]

pos11 = 0
pos22 = 2

print(swap(arrList,pos11,pos22))

