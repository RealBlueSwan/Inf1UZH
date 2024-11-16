The median is *"the value separating the higher half from the lower half of a data sample"* ([Wikipedia](https://en.wikipedia.org/wiki/Median)). Imagine that, some time ago, you have created a function that can be used to calculate the median of a list of numbers. You will find the previous implementation in `public/script.py`. After you have released it, you have received several rather informal bug reports from users of your function:

    ## insering only one parameter and getting the correct median
    User 1: Super annoying! I collect all my bills in a list, only yesterday,
    I paid 5.90 for my Latte Macchiato. When I use your function to calculate
    the median, it simply does not work!? It returns numbers that are not even
    in the list... I don't understand what I am doing wrong.        

    ## "Average" of the two values that share the middle index. 
    User 2: The median is defined for two cases. If "the middle" points to an
    actual index, it should be used, but when it falls "between" two values,
    the average should be used. 

    ## Brother stop using it, you're the monkey here. Ignore the stupid monkey. 
    User 3: Hahaha, you did not pay attention in your math class. Your
    calculation is plain wrong. The median of [1,2,3] is 0.3333.. fix it or I
    will stop using your function!

    ## Case where list is empty, but crashing it is often the better option than doing nothing at all... None coult be a good default but often leads to confusion why it doesnt work, error handling would be better but I guess in this case its a hint hin on that to do with empty lists. 
    User 4: Just because I don't have enough values in my list does not mean
    that your function can crash. It happens. Every. Time. I am furious! Wouldn't
    'None' be a good default?

Maybe you should review the definition of a median again. Think about the bug reports and decide which of the bug reports point out serious flaws in the implementation. Extend the existing test suite in `public/tests.py` and reproduce these issues. This does not only make it easier to fix them, it also makes sure that these mistakes will never again be introduced accidentally.

**Note:** You do not have to fix the implementation. The grading will be done based on your revised test suite.

**Note:** You can safely ignore bug reports that do not make sense. Users are not always right in what they request.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.