# Queue
Before we jump into queues, it is important to know what stacks are, because in this section we will be implementing queues with stacks.
## Stacks
Stacks are data structures that obey the FILO rule which is short for first in last out. It simply means that the first data stored, will be the last one to be removed. If you still don't get it, don't worry because there's a simple example of this in real life. Imagine a tube that you can put marbles in (obviously the diameter of the tube is just slightly larger than the marbles so the marbles go on top of the eachother).
Now imagine you have 5 marbles in the tube. And if you want to access the first marble that you put in the tube, you must get the ones on top one by one first. Simply because the first ball is at the bottom of the tube.
```text
TOP
       │
    ┌──┴──┐
    │  5  │ ← Last in, first out
    ├─────┤
    │  4  │
    ├─────┤
    │  3  │
    ├─────┤
    │  2  │
    ├─────┤
    │  1  │ ← First in, last out
    └─────┘
       │
    BOTTOM
```   
### stacks in python
Although lists can do more than what stacks are capable of, we consider them similar structures to stacks. Abilities such as offering to remove or add data from and to any position in the list and not just head and tail, pushes the barriers far behind.
In order to push(add an item to the stack in python) we use ```append()``` which adds the item to the top of the list. And to remove an item we will use ```pop()``` which removes the item from the the item from the top. These methods also take an "index" argument which specifies the position where we want the item poped or appended.
We can also store the poped item in a variable for later use.
````
My_list = []
My_list.append(1)
My_list.append(2)

poped_item = My_list.pop()
````
Now with these information in mind, let's dive into queues.

## *Queue*
queues are data structures used similarly to store data and organize them. What makes queues different though, is their certain attributes. Unlike stacks, lists don't follow FILO rule. Instead, they have their own characteristics. In a queue first added item is the first item to be removed giving us the FIFO or first in first out rule. Simply imagine a people standing in a grocery store line or people in line for the new product of a shop. People in the front(head) will get served before those behind them and new people will join them in the back(tail) of the line,
```
Grocery Store Queue

Front                              Rear
  ↑                                  ↑
🚶  🚶  🚶  🚶  🚶
 │                   │
Leaves           New person
first             joins here

First Come → First Served

FIFO (First In, First Out)
```
```
QUEUE

Front (Head)                    Rear (Tail)
     ↑                               ↑
     │                               │
+------+------+------+------+------+
|  1   |  2   |  3   |  4   |  5   |
+------+------+------+------+------+
     │                               │
 Remove                        Add

First In  → 1
Last In   → 5
First Out → 1
Last Out  → 5

FIFO (First In, First Out)
```
### Code explanation
In the following illustration we are using two stacks corresponding to one side of a queue. Once the head is empty, it is replaced by the tail stack (ultimately reversing the queue).

##Complexity
The idea is to append elements into the stak_in using ```push()``` method. Here the complexity is simply ```O(1)```.
Now about ```pop()``` if the stack_out is not empty, the function will simply remove the items in it. So the complexity is ```O(1)```. However, if stack_out is empty, we will have to reverse the stack_in and store it in stack_out, then pop the items. Reversing goes through the list n times. So the complexity of this condition is O(n). Worst case 
```
push    O(1)
pop     O(n)
```
