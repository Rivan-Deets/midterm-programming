# CMPSC 202 - Midterm Programming Assignment

Name: Rivan

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository as a private repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

*list your methodological errors and fixes here*
`ERRORS`
It tested only one size: n = 1000
It generated a different random list for each algorithm, so the comparison was unfair
It timed data creation as part of the algorithm run
It did only one timing run, which is noisy and unreliable
It used time.time(), which is less precise than time.perf_counter() 
`fixes`
made it use the same data for both algorithms 
used a fixed set of random seeds so it can be reproduced
tested multiple input sizes 
repeated every timing multiple times and got an average of the results 
intsetad of time.time changed it to time.perf_counter() to have it more accurate 
got a compact table to get the gap between the two algorithms
       n   slow avg (s)   fast avg (s)      ratio
----------------------------------------------------
     100     0.00049512     0.00002682      18.46x
     200     0.00224456     0.00004864      46.15x
     500     0.01892172     0.00016444     115.07x
    1000     0.05631238     0.00024520     229.66x
    2000     0.18567952     0.00037782     491.45x
2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.



