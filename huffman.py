import numpy
import queue

# Сортировка строки подсчетом и нахождение перестановки
def counting_sort_arg(S):
    N = len(S)
    M = 128
    T = [0 for _ in range(M)]
    T_sub = [0 for _ in range(M)]
    # Массив счетчиков символов
    for s in S:
        T[ord(s)] += 1
    # Массив индексов, с которым начинается последовательность повторяющихся символов
    for j in range(1,M):
        T_sub[j] = T_sub[j-1] + T[j-1]
    P = [-1 for _ in range(N)]
    P_inverse = [-1 for _ in range(N)]
    for i in range(N):
        P_inverse[T_sub[ord(S[i])]] = i
        P[i] = T_sub[ord(S[i])]
        T_sub[ord(S[i])] +=1
    return P_inverse

# Нахождение частот символов в строке
def count_symb(S):
    N = len(S)
    counter = numpy.array([0 for _ in range(128)])
    for s in S:
        counter[ord(s)] += 1
    return counter

# Нахождение вероятностей символов в строке
def prob_estimate(S):
    N = len(S)
    P = numpy.array([0 for _ in range(128)])
    for s in S:
        P[ord(s)] += 1
    P = P/N
    return P

# Вычисление энтропии строки
def entropy(S):
    P = prob_estimate(S)
    P = numpy.array(list(filter(lambda x: x!=0,P)))
    E = -sum(numpy.log2(P) * P)
    return E

# Наивная реализация преобразования движения к началу
def MTF(S):
    T = [chr(i) for i in range(128)]
    L = []
    S_new = ""
    for s in S:
        i = T.index(s)
        L.append(i)
        S_new += chr(i)
        T = [T[i]] + T[:i] + T[i+1:]
    return S_new

# Обратное преобразование
def iMTF(S):
    T = [chr(i) for i in range(128)]
    S_new = ""
    for s in S:
        i = ord(s)
        S_new += T[i]
        T = [T[i]] + T[:i] + T[i+1:]
    return S_new

# Класс узла для дерева Хаффмана
class Node():
    def __init__(self, symbol = None, counter = None, left = None, right =None, parent = None):
        self.symbol = symbol
        self.counter = counter
        self.left = left
        self.right = right
        self.parent = parent
    def __lt__(self, other):
        return self.counter < other.counter

# Статический алгоритм Хаффмана
def HA(S):
    C = count_symb(S)
    list_of_leafs = []
    Q = queue.PriorityQueue()
    for i in range(128):
        if C[i] != 0:
            leaf = Node(symbol=chr(i), counter=C[i])
            list_of_leafs.append(leaf)
            Q.put(leaf)
    while Q.qsize() >= 2:
        left_node = Q.get()
        right_node = Q.get()
        parent_node = Node(left=left_node,right=right_node)
        left_node.parent = parent_node
        right_node.parent = parent_node
        parent_node.counter = left_node.counter + right_node.counter
        print(left_node.symbol, right_node.symbol)
        Q.put(parent_node)
    codes = {}
    for leaf in list_of_leafs:
        node = leaf
        print(node.symbol, node.counter)
        code  = ""
        while node.parent != None:
            print(node.parent.left)
            if node.parent.left == node:
                code = "0" + code
            else:
                code = "1" + code
            node = node.parent
        codes[leaf.symbol] = code
    coded_message = ""
    for s in S:
        coded_message += codes[s]
    k = 8 - len(coded_message)%8
    coded_message += (8 - len(coded_message)%8)*"0"
    bytes_string = b""
    for i in range(0,len(coded_message),8):
        s = coded_message[i:i+8]
        x = string_binary_to_int(s)
        print(x)
        bytes_string += x.to_bytes(1,"big")
    print(codes, coded_message)
    return bytes_string

# Преобразование строки размером 8 из нулей и единиц в двоичное число
def string_binary_to_int(s):
    X = 0
    for i in range(8):
        if s[i] == "1":
            X = X + 2**(7-i)
    return X
# Средняя длина кода символа в строке при заданной кодировке
def mean_length_of_codes(codes,S):
    P = prob_estimate(S)
    L = 0
    for s in S:
        L += len(codes[s])
    L = L/len(S)
    return L

# Получение длин кодов Хаффмана
def codes_to_length(codes):
    symbol_lengths = {}
    for item in codes.items():
        symbol = item[0]
        symbol_lengths[symbol] = len(item[1])
    return symbol_lengths

# Преобразование длин кодов Хаффмана в канонические коды
def length_to_codes(symbol_lengths):
    symbol_lengths = dict(sorted(symbol_lengths.items(), key = lambda item: item[1]))
    # print(symbol_lengths)
    codes = {}
    i = 0
    for item in symbol_lengths.items():
        symbol = item[0]
        L = item[1]
        if i == 0:
            code = 0
        else:
            code = (prev_code + 1) * 2**(L-prev_L)
        new_s = f'0b{code:032b}'
        codes[symbol] = new_s[-L:]
        prev_code = code
        prev_L = L
        i += 1
    return codes

print(HA("banana"))