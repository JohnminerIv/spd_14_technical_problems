"""

import LinkedList from "LinkedList.py"

class Stack:
  def _init_() :
      this.List = new LinkedList();

  def push(newItem):
      "insert item on top of the stack"
      // prepend item before head node
      this.List.prepend(newItem, index = 0);


  def peak() :
    if( this.List.head !== none ) {
        return(this.List.head.data[ 0 ]);
      }else{ return none; }

  def pop() :
    "Remove and return the item on top of this stack"
    topItem=this.peak();
    this.List.delete(topItem);
    return(topItem);

"""

from LinkedList import LinkedList


class Stack():
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        """Insert item on top of the stack"""
        # prepend item before head node
        self.list.prepend(new_item)

    def peak(self):
        if self.List.head is not None:
            return self.List.head.data[0]
        else:
            return None

    def pop(self):
        """Remove and return the item on top of this stack"""
        top_item = self.peak()
        self.list.delete(top_item)
        return(top_item)
