class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python
    def is_empty(self):
        return len(self.items) == 0
    def push(self, url):
        self.items.append(url)
    def pop(self):
        if self.is_empty():
            return 'Kosong'
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return 'Kosong'
        return self.items[-1]
    def size(self):
        return len(self.items)

# progaram utama
stack = StackList()
stack.push('A')
stack.push('B')
stack.push('C')

print("isEmpty: ", stack.is_empty())
print("Stack: ", stack.items)
print("Pop: ", stack.pop())
print("Stack setelah Pop: ", stack.items)
print("Peek: ", stack.peek())
print("Size: ", stack.size())

# dengan linked list
print('\ndengan linked list')
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran
        
    def is_empty(self):
        return self.count == 0
        
    def push(self, url):
    # Tulis kode di sini
    # 1. Buat Node baru
    # 2. Hubungkan 'next' node baru ke 'top' saat ini
    # 3. Jadikan node baru sebagai 'top' yang baru
    # 4. Tambahkan nilai 'count'
        baru = Node(url)
        if self.top:
            baru.next = self.top
        self.top = baru
        self.count += 1
        
    def pop(self):
    # Tulis kode di sini
    # 1. Periksa is_empty()
    # 2. Simpan url dari 'top' saat ini
    # 3. Geser 'top' ke node berikutnya (top = top.next)
    # 4. Kurangi nilai 'count'
    # 5. Kembalikan url yang disimpan
        if self.is_empty():
            return "kosong"
        data = self.top.url
        self.top = self.top.next
        self.count -= 1
        return data
    
    def peek(self):
        if self.is_empty():
            print('Kosong')
        return self.top.url
    
    def size(self):
        return self.count
    
    def cetak(self):
        curr = self.top
        while curr:
            print(curr.url, end=" -> ")
            curr = curr.next
        print("Null")

myStack = StackLinkedList()

myStack.push('1')
myStack.push('2')
myStack.push('3')

print("LinkedList: ", end="")
myStack.cetak()
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())