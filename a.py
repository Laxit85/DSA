class solution:
    #def unianandintersection(self,a,b):
        
     #   set_a =set(a)
    #    set_b =set(b)
        
   #     unian_set = set(a) | set(b)
        
  #      intersection_set = set(a) & set(b)
        
 #       return list(unian_set), list(intersection_set)

#obj = solution()
#a = [1,2,2,1,3]
#b = [2,3,2]
#print(obj.unianandintersection(a,b))
    def rotatearrbyone(self,arr):
        
        a = arr[-1]
        
        for i in range(len(arr)-1,0,-1):
            arr[i] = arr[i-1]
        
        arr[0] = a
        
sol = solution()
arr = [1,2,3,4,5]
sol.rotatearrbyone(arr)        
print(arr)