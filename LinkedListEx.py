#A single elemet list , next , is initialized with null value
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

#All the funtions of link list
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

# append" returns add elements to the list
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

# get_position" returns the element at a certain position.
    def get_position(self, position):
        """Get an element from a particular position.
        Assumeing the first position is "1".
        Return "None" if position is not in the list."""
        current=self.head
        count=1
        if position < 1:
            return None
        if self.head:
            while ((current.next )and (count<= position)):
                if count == position:
                    return current
                current = current.next
                count=count+1

        return current.value

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assumeing the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        count = 1
        if position > 1:
            while ((current)and (count < position)):
                if(count == position-1):

                    new_element.next=current.next
                    current.next = new_element
                    break
                #print("count",count)
                current = current.next
                count = count + 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

        pass
#"delete" will delete the first element with that
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
        pass


# Test cases
# Set up some Elements
e1 = Element("one")
e2 = Element("two")
e3 = Element("three")
e4 = Element("four")

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print(ll.head.next)
print(ll)


print ("Value at position 3---- ", ll.get_position(3))

ll.insert(e4, 3)
# Should print 4 now
print ("Value at position 3---- ", ll.get_position(3))

ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)
