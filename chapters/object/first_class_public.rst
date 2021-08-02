一等公民
========

这里的一等公民特指 python 中的函数.

.. admonition:: 一等公民

    一等公民是指编程语言中满足如下特点的对象:

    - 可以在运行时创建,
    - 能够被赋值给变量,
    - 可以作为集合对象的元素,
    - 还能够作为函数的参数以及返回值.

为什么我在这里要强调 python 中的函数是一等公民呢? 因为在很多其他诸如 C, C++, Java 等语言中, 函数和整数/字符串/字典/列表等对象地位并不是平等的. 这是 python 一个非常重要的特点.

python 中的函数之所以是一等公民, 是因为 python 中的一切都是对象, 即 *everything in python is an object*. 换句话说:  python 中函数是一等公民这一现象是 python 一切皆对象的必然结果.

:py:`import pdb; pdb.set_trace()`
