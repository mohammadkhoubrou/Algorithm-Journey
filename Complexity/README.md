# Complexity
Algorithm complexity is the study of the resources required by the algorithm and it is represented as a function of the inputs. Using complexity we can analyze efficiency and algorithm behavior as the input size grows larger. 

The two primary resources considered in complexity are **time** and **space**. Time complexity provides a mathematical understanding of how the number of operations grows with the input size, while space complexity provides information on how the memory requirements grow. It allows us to compare algorithms independently.

In this directory, I have intended to explain the fundamentals of complexity computations. The practical examples of these concepts are provided in the last section of each algorithm's description within its respected directory.

Before we begin, I'd like to review some sequences of numbers and their attributes.

## Numerical Sequences

$$
\sum_{i=1}^n i = 1 + 2 + \dots + n = \frac{n(n + 1)}{2} = \frac{n^2 +n}{2} 
$$

$$
\sum_{i=1}^n i^2 = 1^2 + 2^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6} 
$$


$$
\sum_{i=1}^n i^3 = 1^3 + 2^3 + \dots + n^3 = ({\frac{n(n + 1)}{2}})^2
$$


$$
\sum_{i=1}^n i^k = 1^k + 2^k + \dots + n^k = \frac{n^{k+1}}{k+1} 
$$
