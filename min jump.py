class solution:
    def minjumps(self,arr):
        
        if len(arr) <= 1:
            return 0
        
        if arr[0] == 0:
            return -1
        
        maxreach = arr[0]
        
        steps = arr[0]
        
        jumps = 1
        
        for i in range(1,len(arr)):
            if i ==len(arr)-1:
                return jumps 
            
            maxreach = max(maxreach , i+arr[i])
            steps -= 1
            
            if steps == 0:
                jumps += 1
                
                if i >= maxreach:
                    return -1
                
                steps = maxreach - i
        return -1 
    
Sol = solution()
arr = [2,3,1,1,4,4,5,6,7,7,8,8]
print(Sol.minjumps(arr))