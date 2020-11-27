def swap(arr, pos_1, pos_2):
  tmp = arr[pos_1]
  arr[pos_1] = arr[pos_2]
  arr[pos_2] = tmp
  return arr

arrList = [19,65, 88, 353, 225, 332]
print("Original" , arrList)
arrList.append(22)
arrList.remove(225)

pos11 = 0
pos22 = 1
print("\nAfter operations")
print(swap(arrList,pos11,pos22))

