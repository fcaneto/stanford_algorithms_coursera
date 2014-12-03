import heapq

def k_way_merge(*args):
    """
    A function that gets k sorted lists and returns a merged sorted list with all elements from all lists.
    
    Solution: considering descending order, to get the next element of the resulting list we have to get
    max(list_1[0], list_2[0], ...., list_tk[0]). A heap is used here, reducing from O(k) to O(logk) operations   
    (a push and a pop to the heap, limiting its size to k elements).
    
    Total complexity of solution is O(nklogk).
    """
    heads_heap = IterableHeap()

    for index, l in enumerate(args):
        if l:
            heads_heap.push(ListItem(l.pop(0), index))
            
    for next in heads_heap:
        print("next is %s from list %s" % (next.value, next.index))
        if args[next.index]:
            heads_heap.push(ListItem(args[next.index].pop(0), next.index))

        yield next.value


class ListItem(object):
    """
    Stores the value os a list item and from which list it came from (index).
    """
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value <= other.value


class IterableHeap(object):
    """
    Iterator wrapper for heapq module just for fun.
    """
    def __init__(self, key=lambda x:x): 
        self.key = key
        self.heap = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.heap:
            return self.pop()
        else:
            raise StopIteration

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [2, 3, 4, 5]

print(list(k_way_merge(a, b, c)))

