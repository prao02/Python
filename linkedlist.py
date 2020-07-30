class node:
    def __init__(self,d,n=None,p=None):
        self.data=d
        self.next_node=n
        self.prev_node=p
    def __str__(self):
        return ('(' + str(self.data)+ ')')
class Linklist:
    def __init__(self,r=None):
        self.root=r
        self.size=0
    def add(self,d):
        new_node=node(d,self.root)
        self.root= new_node
        self.size +=1
    def find(self,d):
        this_node=self.root
        while this_node is not None:
            if this_node.data==d:
                return d
            else:
                this_node=this_node.next_node
        return None
    def remove(self,d):
        this_node=self.root
        prev_node=None
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None: #not in root node then
                    prev_node.next_node=this_node.next_node
                else:
                    self.root=this_node.next_node
                self.size -=1
                return True
            else:
                prev_node=this_node
                this_node=this_node.next_node
        return False
    def print_list(self):
        this_node=self.root
        while this_node is not None:
            print(this_node,end='->')
            this_node=this_node.next_node
        print('None')

link=Linklist()
link.add(5)
link.add(3)
link.add(2)
link.print_list()
print(link.find(5))
link.remove(3)
link.print_list()
print(link.find(3))