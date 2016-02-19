#!/bin/python
def check(lst):
    for i in range(len(lst)-1):
        if lst[i+1] < lst[i]:
            return False
            break
    else:
        return True
def my_copy(ar):
    new_arr = []
    for j in ar:
        new_arr.append(j)
    return new_arr
    
    
def insertionSort(ar):
    repeat = True

    new_arr = []
    old_arr = []
    size = 5
    for j in ar:
        new_arr.append(j)
    i = 0
    k = 1000
    while(repeat):
        if i == 4:
            i = 0
            
        if new_arr[i]>new_arr[i+1]:
            ist_val = new_arr[i]
            sec_val = new_arr[i+1]
            new_arr[i+1]= ist_val
            new_arr[i] = sec_val
            
            if new_arr!=old_arr:
                print(new_arr)
                old_arr = my_copy(new_arr)
        if check(new_arr):
            repeat = False
            
        
        i+=1
        k-=1
    ist_val = new_arr[4]
    sec_val = new_arr[5]
    new_arr[5]= ist_val
    new_arr[4] = sec_val
    print(new_arr)
insertionSort([1, 4, 3, 5, 6, 2])
        

def test(li):   
 ap_test_1 = li[1] - li[0]
 ap_test_2 = li[2] - li[1]
 ap_test_3 = li[3] - li[2]
 gp_test_1 = li[1] / li[0]
 gp_test_2 = li[2] / li[1]
 gp_test_3 = li[3] / li[2]
 if ap_test_1 == ap_test_2 and ap_test_2 == ap_test_3:
   return "Arithmetic"
 elif gp_test_1 == gp_test_2 and gp_test_2 == gp_test_3:
   return "Geometric"
 else:
   return -1
  
def arith_geo(lis):
 if lis==[]:
     return 0
 else :
     return test(lis)




