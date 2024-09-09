class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def __len__(self):
        count = 1
        itr = self.head
        while itr.next:
            count = count + 1
            itr = itr.next
        return count

    def insert_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert(self, position, data):
        if position > len(self) or position < 0:
            raise Exception("Invalid Index")

        if position == 0:
            self.insert_first(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == position - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_last(data)

    def delete(self, position):
        if position < 0 or position > len(self):
            raise Exception("Invalid index")

        if position == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if position - 1 == count:
                itr.next = itr.next.next
            count += 1
            itr = itr.next

    def get_index(self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                return count
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        index = self.get_index(data_after)
        if index is None:
            print("Your data is not present so i added it in the last")
            self.insert_last(data_to_insert)
            return
        self.insert(index + 1, data_to_insert)

    def remove_by_value(self, data):
        index = self.get_index(data)
        if index is None:
            print("Data is not available")
            return
        self.delete(index)

    def print_all_nodes(self):
        if self.head is None:
            print("List is Empty")

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->" if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ls = LinkList()
    ls.insert_first(12)
    ls.insert_first(13)
    ls.insert_first(14)
    ls.insert_last(19)
    ls.insert(2, 29)
    ls.print_all_nodes()
    # ls.delete(2)
    # ls.print_all_nodes()
    ls.insert_after_value(29, 16)
    ls.print_all_nodes()
    ls.remove_by_value(18)
    ls.print_all_nodes()
    print(ls.get_index(20))
    print(len(ls))
