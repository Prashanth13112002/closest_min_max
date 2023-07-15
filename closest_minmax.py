class minmax:
    def closest_minmax(self,array):
        minimum=float("inf")
        maximum=float("-inf")
        for i in array:
            if(i<minimum):
                minimum=i
            if(i>maximum):
                maximum=i
        last_min_index=-1
        last_max_index=-1
        result=len(array)
        for i in range(len(array)):
            if array[i]==minimum:
                last_min_index=i
                if last_max_index>=0:
                    result=min(result,i-last_max_index+1)
            if array[i]==maximum:
                last_max_index=i
                if last_min_index>=0:
                    result=min(result,i-last_min_index+1)
        return result
a=list(map(int,input().split()))
array1=minmax()
print(array1.closest_minmax(a))