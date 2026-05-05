history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)
    return history_array

print('isi history array')
print(history_array)
tambah_pencarian_array('Wikipedia')
tambah_pencarian_array('w3skul')
print('\nisi history array setelah ditambahkan: ', end='')
print(', '.join(history_array))
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None
        
    def tampilkan_histori(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('null')
        
    def tambah_pencarian_linked(self, keyword):
        newNode = Node(keyword)
        if not self.head:
            self.head =newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        
histori = HistoryLinkedList()
histori.tambah_pencarian_linked('Google.com')
histori.tambah_pencarian_linked('Python.org')
histori.tambah_pencarian_linked('wikipedia')

print("list Awal:", end=' ')
histori.tampilkan_histori()

histori.tambah_pencarian_linked('github')

print("\nList setelah ditambahkan:", end=' ')
histori.tampilkan_histori()