# Merge Sort
Merge Sort is a *devide and conquer* algorithm. The idea is to devide the given array or list recursively untill there's no need
for soritng. The recursion continues untill there's only one element in the array which doesn't require sorting. Then, the algorithm
compares the elements and sorts the array while merging the splited parts.
In this approach, just for the sake of practice, I have implemented the merging with recursion. However, this approach is slow and 
inefficient in python. Using loops infact is more convenient.
```
   |8|3|6|1|
 |8|3|   |6|1|
|8| |3| |6| |1|
   |1|3|6|8|
```
When merging, the algorithm tries to compare the left most element of the left array with the left most element of the right array. 
Why not compare the first and second elements of the first array? Valid question, but each array is a sorted one. How? We will devide
the arrays untill there's only one array in the algorithm. So again we will compare the first element of this length one array with 
the array on the right. We will keep the smallest element(if the sorting is ascending) and call the same process on the rest of the 
remaining elements.
So each side of the array gets it's own process line and connect once they're sorted.

In the method that envolves loops, however, the algorithm uses two pointers to compare the elements and once one pointer reaches the 
end of one array, it adds the remainings of the second array to the end of the array because the remainings are surely larger than 
the past elements.

## Complexity

  |      parts      |     Recursive  |   Loop-based   |<br>
  |    Merge  time  | ‍‍‍‍‍O‍($n^2$)   |     O(n)       |<br>
  |  Merge-Sort time|    O($n^2$)    |   O(n log n)   |

  |        | Recursive | Loop-based |
|:--------:|:--------:|:--------:|
| Merge  time     |  ‍‍‍‍‍O‍($n^2$)   |    O(n)    |
|  Merge-Sort time|  O($n^2$)   | O(n log n) |


