import heapq
from collections import defaultdict

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # Frequency of the symbol
        self.symbol = symbol  # Symbol or combination of symbols
        self.left = left  # Left child
        self.right = right  # Right child
        self.huff = ''  # Binary code (0 or 1) for the node

    def __lt__(self, other):
        return self.freq < other.freq  # Comparison based on frequency


def calculate_huffman_codes(node, val='', huffman_code={}):
    # Recursive function to calculate Huffman codes
    newVal = val + str(node.huff)
    if node.left:
        calculate_huffman_codes(node.left, newVal, huffman_code)
    if node.right:
        calculate_huffman_codes(node.right, newVal, huffman_code)
    if not node.left and not node.right:
        huffman_code[node.symbol] = newVal  # Assign the code to the symbol
    return huffman_code


def huffman_encoding(symbols, frequencies):
    nodes = []
    for symbol, frequency in zip(symbols, frequencies):
        heapq.heappush(nodes, Node(frequency, symbol))  # Add nodes to the priority queue
    while len(nodes) > 1:
        left = heapq.heappop(nodes)  # Node with smallest frequency
        right = heapq.heappop(nodes)  # Node with second smallest frequency
        left.huff = 0  # Assign 0 to the left child
        right.huff = 1  # Assign 1 to the right child
        # Create a new node combining left and right
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)
    return calculate_huffman_codes(nodes[0])  # Calculate Huffman codes


# User-friendly input
try:
    symbols = input("Enter symbols (separated by spaces): ").split()
    frequencies = list(map(int, input("Enter corresponding frequencies (separated by spaces): ").split()))
    
    if len(symbols) != len(frequencies):
        print("The number of symbols and frequencies must match!")
    else:
        huffman_code = huffman_encoding(symbols, frequencies)
        print("\nHuffman Codes:")
        for symbol, code in huffman_code.items():
            print(f"{symbol}: {code}")
except ValueError:
    print("Invalid input! Please ensure frequencies are integers.")
