from operator import truediv
def hello_world():
    print("hello world")
    return True

def get_minimum(my_list):
    min_value = my_list[0]
    for element in my_list:
        if min_value >= element:
            min_value = element
    return min_value

def get_max(my_list):
    max_value = my_list[0]
    for element in my_list:
        if max_value <= element:
            max_value = element
    return max_value

def get_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

def comun_lists(list1, list2):
    common_elements =[]
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    common_elements.sort()
    return common_elements

def goldbach(n):
    def prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if n <= 2 or n % 2 != 0:
        return False
    for i in range(2, n):
        if prime(i) and prime(n - i):
            return f"{i} + {n - i}"
    return False


def maxarea(h):
    l = 0
    r = len(h) - 1
    m_w= 0
    while l < r:
        w = r - l
        h_c = min(h[l], h[r])
        a_c = w * h_c
        m_w= max(m_w, a_c)
        if h[l] < h[r]:
            l += 1
        else:
            r -= 1
    return m_w

hello_world()