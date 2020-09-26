"""
常用排序算法：
1.插入排序
2.选择排序
3.冒泡排序
4.快速排序
5.归并排序
"""

# 插入排序
# 算法思想：
"""从第二个元素开始和前面的元素进行比较，如果前面的元素比当前元素大，则将前面元素后移，当前元素依次往前，直到找到比它小或等于它的元素插入在其后面，然后选择第三个元素，重复上述操作，进行插入，依次选择到最后一个元素，插入后即完成所有排序。"""

def insertion_sort(arr):
    #插入排序
    # 第一层for表示循环插入的遍数
    for i in range(1, len(arr)):
        # 设置当前需要插入的元素
        current = arr[i]
        # 与当前元素比较的比较元素
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            arr[pre_index + 1] = arr[pre_index]
            # 往前选择下一个比较元素
            pre_index -= 1
        # 当比较元素小于当前元素，则将当前元素插入在其后面
        arr[pre_index + 1] = current
    return arr
	

arr = [-5,3,1,5,2,4,-1,-5]	
print(insertion_sort(arr))



# 选择排序
# 算法思想
"""
设第一个元素为比较元素，依次和后面的元素比较，比较完所有元素找到最小的元素，将它和第一个元素互换，重复上述操作，我们找出第二小的元素和第二个位置的元素互换，以此类推找出剩余最小元素将它换到前面，即完成排序。"""

def selection_sort(arr):
    #选择排序
    # 第一层for表示循环选择的遍数
    for i in range(len(arr) - 1):
        # 将起始元素设为最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
        # 查找一遍后将最小元素与起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr
	
arr = [-5,3,1,5,2,4,-1,-5]
print(selection_sort(arr))



# 冒泡排序
# 算法思想
"""
从第一个和第二个开始比较，如果第一个比第二个大，则交换位置，然后比较第二个和第三个，逐渐往后，经过第一轮后最大的元素已经排在最后，
所以重复上述操作的话第二大的则会排在倒数第二的位置。，那重复上述操作n-1次即可完成排序，因为最后一次只有一个元素所以不需要比较。"""

def bubble_sort(arr):
    #冒泡排序
    # 第一层for表示循环的遍数
    for i in range(len(arr) - 1):
        # 第二层for表示具体比较哪两个元素
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # 如果前面的大于后面的，则交换这两个元素的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [-5,3,1,5,2,4,-1,-5]	
print(bubble_sort(arr))


# 快速排序
# 算法思想
"""
找出基线条件，这种条件必须尽可能简单，不断将问题分解（或者说缩小规模），直到符合基线条件。"""

def quick_sort(arr):
  if len(arr) < 2:
    # 基线条件：为空或只包含一个元素的数组是“有序”的
    return arr
  else:
    # 递归条件
    pivot = arr[0]
    # 由所有小于基准值的元素组成的子数组
    less = [i for i in arr[1:] if i <= pivot]
    # 由所有大于基准值的元素组成的子数组
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [-5,3,1,5,2,4,-1,-5]
print(quick_sort(arr))	


# 归并排序
# 算法思想
"""
归并排序是分治法的典型应用。分治法（Divide-and-Conquer）：将原问题划分成n个规模较小而结构与原问题相似的子问题；递归地解决这些问题，然后再合并其结果，就得到原问题的解，分解后的数列很像一个二叉树。
具体实现步骤：
1.使用递归将源数列使用二分法分成多个子列
2.申请空间将两个子列排序合并然后返回
3.将所有子列一步一步合并最后完成排序
4.注：先分解再归并"""
def merge_sort(arr):
    #归并排序
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 使用递归运算
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    #排序合并两个数列
    result = []
    # 两个数列都有值
    while len(left) > 0 and len(right) > 0:
        # 左右两个数列第一个最小放前面
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只有一个数列中还有值，直接添加
    result += left
    result += right
    return result


arr = [-5,3,1,5,2,4,-1,-5]
print(merge_sort(arr))
	
	
	
	
	
	
	
	
	
	
	
	
	









