# Complexity
Algorithm complexity is the study of the resources required by the algorithm and it is represented as a function of the inputs. Using complexity we can analyze efficiency and algorithm behavior as the input size grows larger. 

The two primary resources considered in complexity are **time** and **space**. Time complexity provides a mathematical understanding of how the number of operations grows with the input size, while space complexity provides information on how the memory requirements grow. It allows us to compare algorithms independently.

In this directory, I have intended to explain the fundamentals of complexity computations. The practical examples of these concepts are provided in the last section of each algorithm's description within its respected directory.

Before we begin, I'd like to review some sequences of numbers and their attributes. 

## Numerical Sequences
Numerical sequences help us count the number of times an operation is performed.

Sum of natural numbers:

$$
\sum_{i=1}^n i = 1 + 2 + \dots + n = \frac{n(n + 1)}{2} = \frac{n^2 +n}{2} 
$$

Power of two:

$$
\sum_{i=1}^n i^2 = 1^2 + 2^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6} 
$$

power of three:

$$
\sum_{i=1}^n i^3 = 1^3 + 2^3 + \dots + n^3 = ({\frac{n(n + 1)}{2}})^2
$$

Sum of powers:

$$
\sum_{i=1}^n i^k = 1^k + 2^k + \dots + n^k = \frac{n^{k+1}}{k+1} 
$$

Harmonic Series:

$$
\sum_{i=1}^{n}\frac{1}{i}
= 1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}
\sim \ln n
= \Theta(\ln n)
$$

Geometric Series:

$$
\sum_{k=0}^{n-1} ax^k
= a+ax+ax^2+\cdots+ax^{n-1}
= a\frac{1-x^n}{1-x}
= a\frac{x^n-1}{x-1}
$$

For $|x|<1$ and $n\to\infty$:

$$
\sum_{k=0}^{\infty} ax^k
= a+ax+ax^2+\cdots
= \frac{a}{1-x}
$$

Arithmetic Series:

$$
\sum_{k=0}^{n-1}(a+kd)
= a+(a+d)+(a+2d)+\cdots+(a+(n-1)d)
$$

$$
= \frac{(a+a+(n-1)d)n}{2}
$$

Constant Series:

$$
\sum_{i=m}^{n} a
= a+a+\cdots+a
= (n-m+1)a
$$

Weighted Geometric Series:

$$
\sum_{k=0}^{\infty}kx^k
= \frac{x}{(1-x)^2},
\qquad |x|<1
$$

Telescoping Series:

$$
\sum_{k=1}^{n}(a_k-a_{k-1})
= a_n-a_0
$$

For example:

$$
\sum_{k=1}^{n-1}\frac{1}{k(k+1)}
= \sum_{k=1}^{n-1}\left(\frac{1}{k}-\frac{1}{k+1}\right)
= 1-\frac{1}{n}
$$

## Logarithm
Logarithm is one of the essential concepts we need to know while studying complexity.

Product Rule:

$$
\log_b(MN) = \log_b(M) + \log_b(N)
$$

Quotient Rule:

$$
\log_b\left(\frac{M}{N}\right)
= \log_b(M) - \log_b(N)
$$

Power Rule:

$$
\log_b\left(M^a\right)
= a\log_b(M)
$$

Change of Base Rule:

$$
\log_b(M)
= \frac{\log_c(M)}{\log_c(b)}
$$

Reciprocal Rule:

$$
\log_b(a)
= \frac{1}{\log_a(b)}
$$

Exponential-Logarithmic Rule:

$$
a^{\log_a(b)} = b
$$

Change of Base / Exponent Rule:

$$
a^{\log_c(b)}
= b^{\log_c(a)}
$$

Logarithm of 1:

$$
\log_b(1) = 0
$$

Logarithm of the Base:

$$
\log_b(b) = 1
$$

Inverse Property:

$$
\log_b\left(b^a\right) = a
$$

## Function Burst
Now we are checking to see which function bursts when we take n to the $\infty$. For this purpose we can use limit:

$$
lim_{\rightarrow \infty} \frac{4n^2}{n^3} = \frac{4}{n} = 0
$$

$4n^2$ is less than $n^3$. How do we determine that?

$$
lim_{\rightarrow \infty} \frac{f(n)}{g(n)} =
\begin{cases}
0, & f(n) < g(n) \\
\infty, & f(n) > g(n) \\
0 < k < \infty, & f(n) = g(n)
\end{cases}
$$

Based on the rules above, we can determine the growth of a function when compared with another one. Here are some tips you should remember:
- Coefficient has no effect on growth.
- Growth of a polynomial is equal to the growth of its highest rank element.

$$
a_p n^p + a_p n^p + \dots + a_0 \longrightarrow a_p n^p = n^p
$$

- Growth of $log_b ^n$ = $log_a ^ n$.
- Growth of an exponential function is larger than polynomials.

$$
a^n > n^b$$

- Log Log n grows extremely slow.
- Log^4 n grows faster than Log Log n, but still much slower than n.

## Asymptotic Notations
We use $O, \Omega, \theta, o, \omega$ to emphesize the growth of  a function or the complexity of an algorithm.

### O(g(n))
We use *big O* notation, when the complexity of f(n) is less or equal to g(n). For example,
$$3n^2 + n + 4 \in O(n^2)$$</br>
$$3n^2 + n + 4 \notin O(n)$$</br>
$${3n^2, 5n, ln n ^4, \sqrt{n}, lglg n} \in O(n^2)$$

### $\Omega(g(n))$
If the growth of f(n) is larger or equal to g(n), then f(n) $\in \Omega(g(n))$.
$${n^2, 3n^2 + n, n^3 - n, 2^n, n!} \in \Omega(n^2)$$

### $\theta(g(n)$
When the growth of f(n) and g(n) are equal, we use $theta$. This in fact is the intersection of $\Omega$ and O.

$$3n^2 + n + 4 \in g(n^2)$$</br>
$$3n^2 + n + 4 \notin g(n)$$</br>
$$3n^2 + n + 4 \notin g(n^3)$$</br>

### o(g(n))
If the growth of f(n) is less than g(n).

$$f(n) \in o(g(n))$$</br>
$$3n^2 \in o(n^3)$$</br>
$$3n^2 \notin o(n^2)$$ because it is equal.

$${3n + 4, log n, log^5 n, \sqrt{n}, \frac{1}{n}} \in o(n^2)$$

### $\omega(g(n))$
When f(n) is larger than g(n). $\omega(g(n))$ and o(g(n)) do not have an intersection.
$$3n^2 + n + 4 \in g(n)$$</br>
$$3n^2 + n + 4 \notin g(n^2)$$</br>

## Attributes of Symbols
1. Reflective:
$O, \Omega, \theta$ are reflective, meaning:</br>
$$f(n) \in O(f(n))$$</br>
$$f(n) \in \theta(f(n))$$</br>
$$f(n) \in \Omega(g(n))$$</br>

2. Symmetric:
$\theta$ is symmetric.</br>
$$g(n) \in \theta(f(n))$$ and $$f(n) \in \theta(g(n))$$</br>

3. Transpose Symmetric: $O, \Omega, \omega, o$</br>
$$f(n) \in O(g(n))$$ and $$g(n) \in \Omega(f(n))$$</br>
$$f(n) \in o(g(n))$$ and $$g(n) \in \omega(f(n))$$

## Calculating Time Complexity

As it was mentioned before, time complexity is explained through the total number of execution of each component.

```
for (i=1 to n) --> n + 1 times
  write("*") --> n times
```
So the condition of i <= n is checked n + 1 times, n times execution and True condition, once i is passed n.

| Iteration | `i` | Condition `i ≤ n` (`n = 5`) | `write("*")` |
|---:|---:|:---:|:---:|
| 1 | 1 | True | `*` |
| 2 | 2 | True | `*` |
| 3 | 3 | True | `*` |
| 4 | 4 | True | `*` |
| 5 | 5 | True | `*` |
| 6 | 6 | False | — |

$$\theta(n)$$
---------------------------------------
```
for (i=a to b) --> b - a + 2 times
  write("*") --> b - a + 1 times
```
| Iteration | `i` | Condition `i ≤ b` | `write("*")` |
| --------: | --: | :---------------: | :----------: |
|         1 |   2 |        True       |      `*`     |
|         2 |   3 |        True       |      `*`     |
|         3 |   4 |        True       |      `*`     |
|         4 |   5 |        True       |      `*`     |
|         5 |   6 |       False       |       —      |

$$\theta(b - a + 1)$$
-------------------------------------------

```
for (i = 1 to n)
  for (i = 1 to n)
    write("*")
```
| Outer Iteration | `i` | Inner Iteration | `j` | Inner Condition `j ≤ n` | `write("*")` |
| --------------: | --: | --------------: | --: | :---------------------: | :----------: |
|               1 |   1 |               1 |   1 |           True          |      `*`     |
|               1 |   1 |               2 |   2 |           True          |      `*`     |
|               1 |   1 |               3 |   3 |           True          |      `*`     |
|               1 |   1 |               4 |   4 |          False          |       —      |
|               2 |   2 |               1 |   1 |           True          |      `*`     |
|               2 |   2 |               2 |   2 |           True          |      `*`     |
|               2 |   2 |               3 |   3 |           True          |      `*`     |
|               2 |   2 |               4 |   4 |          False          |       —      |
|               3 |   3 |               1 |   1 |           True          |      `*`     |
|               3 |   3 |               2 |   2 |           True          |      `*`     |
|               3 |   3 |               3 |   3 |           True          |      `*`     |
|               3 |   3 |               4 |   4 |          False          |       —      |
|               4 |   4 |               — |   — |          False          |       —      |

$$
\sum_{i=1}^{n}n=n^2$$

$$\theta(n^2)$$
-----------------------------------


```
for (i = 1 to n)
  for (j = 1 to i)
    write("*")
```
| Outer Iteration | `i` | Inner Iteration | `j` | Condition `j ≤ i` | `write("*")` |
| --------------: | --: | --------------: | --: | :---------------: | :----------: |
|               1 |   1 |               1 |   1 |        True       |      `*`     |
|               1 |   1 |               2 |   2 |       False       |       —      |
|               2 |   2 |               1 |   1 |        True       |      `*`     |
|               2 |   2 |               2 |   2 |        True       |      `*`     |
|               2 |   2 |               3 |   3 |       False       |       —      |
|               3 |   3 |               1 |   1 |        True       |      `*`     |
|               3 |   3 |               2 |   2 |        True       |      `*`     |
|               3 |   3 |               3 |   3 |        True       |      `*`     |
|               3 |   3 |               4 |   4 |       False       |       —      |
|               4 |   4 |               1 |   1 |        True       |      `*`     |
|               4 |   4 |               2 |   2 |        True       |      `*`     |
|               4 |   4 |               3 |   3 |        True       |      `*`     |
|               4 |   4 |               4 |   4 |        True       |      `*`     |
|               4 |   4 |               5 |   5 |       False       |       —      |
|               5 |   5 |               — |   — |       False       |       —      |

$$
\sum_{i=1}^{n}i=\frac{n(n+1)}{2}$$

$$\theta(n^2)$$
-----------------------------------------

```
for (i = 1 to n)
  for (j = 1 to i)
    for (k = 1 to j)
      write("*")
```
for n = 4:

| Outer `i` | Middle `j` | Inner `k` | Condition `k ≤ j` | `write("*")` |
| --------: | ---------: | --------: | :---------------: | :----------: |
|         1 |          1 |         1 |        True       |      `*`     |
|         1 |          1 |         2 |       False       |       —      |
|         2 |          1 |         1 |        True       |      `*`     |
|         2 |          1 |         2 |       False       |       —      |
|         2 |          2 |         1 |        True       |      `*`     |
|         2 |          2 |         2 |        True       |      `*`     |
|         2 |          2 |         3 |       False       |       —      |
|         3 |          1 |         1 |        True       |      `*`     |
|         3 |          1 |         2 |       False       |       —      |
|         3 |          2 |         1 |        True       |      `*`     |
|         3 |          2 |         2 |        True       |      `*`     |
|         3 |          2 |         3 |       False       |       —      |
|         3 |          3 |         1 |        True       |      `*`     |
|         3 |          3 |         2 |        True       |      `*`     |
|         3 |          3 |         3 |        True       |      `*`     |
|         3 |          3 |         4 |       False       |       —      |
|         4 |          1 |         1 |        True       |      `*`     |
|         4 |          1 |         2 |       False       |       —      |
|         4 |          2 |         1 |        True       |      `*`     |
|         4 |          2 |         2 |        True       |      `*`     |
|         4 |          2 |         3 |       False       |       —      |
|         4 |          3 |         1 |        True       |      `*`     |
|         4 |          3 |         2 |        True       |      `*`     |
|         4 |          3 |         3 |        True       |      `*`     |
|         4 |          3 |         4 |       False       |       —      |
|         4 |          4 |         1 |        True       |      `*`     |
|         4 |          4 |         2 |        True       |      `*`     |
|         4 |          4 |         3 |        True       |      `*`     |
|         4 |          4 |         4 |        True       |      `*`     |
|         4 |          4 |         5 |       False       |       —      |

$$
\sum_{i=1}^{n}\sum_{j=1}^{i}j=\frac{n(n+1)(n+2)}{6}$$

$$\theta(n^3)$$
--------------------------------------------

```
i = n
while (i > 1)
  write("*")
  i = i - 2
```
| Iteration | `i` (before) | Condition `i > 1` | `write("*")` | `i` (after) |
| --------: | -----------: | :---------------: | :----------: | ----------: |
|         1 |            7 |        True       |      `*`     |           5 |
|         2 |            5 |        True       |      `*`     |           3 |
|         3 |            3 |        True       |      `*`     |           1 |
|         4 |            1 |       False       |       —      |           — |

$$
\frac{n-1}{2}$$

$$\theta(n)$$
---------------------------------------------

```
i = n
while (i > 1)
  write("*")
  i = i // 2
```
| Iteration | `i` (before) | Condition `i > 1` | `write("*")` | `i` (after) |
| --------: | -----------: | :---------------: | :----------: | ----------: |
|         1 |           20 |        True       |      `*`     |          10 |
|         2 |           10 |        True       |      `*`     |           5 |
|         3 |            5 |        True       |      `*`     |           2 |
|         4 |            2 |        True       |      `*`     |           1 |
|         5 |            1 |       False       |       —      |           — |

$$
\log_2 n$$

$$\theta(log n)$$
------------------------------------------------
```
i = 1
while (i < n)
  write("*")
  i = i * 2
```
| Iteration | `i` (before) | Condition `i < n` | `write("*")` | `i` (after) |
| --------: | -----------: | :---------------: | :----------: | ----------: |
|         1 |            1 |        True       |      `*`     |           2 |
|         2 |            2 |        True       |      `*`     |           4 |
|         3 |            4 |        True       |      `*`     |           8 |
|         4 |            8 |        True       |      `*`     |          16 |
|         5 |           16 |        True       |      `*`     |          32 |
|         6 |           32 |       False       |       —      |           — |

$$
\log_2 n$$

$$\theta(log n)$$
------------------------------------------------
```
i = 2
while (i < n)
  write("*")
  i = i * i
```
| Iteration | `i` (before) | Condition `i < n` | `write("*")` | `i` (after) |
| --------: | -----------: | :---------------: | :----------: | ----------: |
|         1 |            2 |        True       |      `*`     |           4 |
|         2 |            4 |        True       |      `*`     |          16 |
|         3 |           16 |        True       |      `*`     |         256 |
|         4 |          256 |       False       |       —      |           — |

$$
\log_2\log_2 n$$

$$\theta(log log n)$$
--------------------------------------------------
