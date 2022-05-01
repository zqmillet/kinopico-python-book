一等公民
========

这里的一等公民特指 Python 中的函数.

.. admonition:: 一等公民

    一等公民是指编程语言中满足如下特点的对象:

    - 可以在运行时创建,
    - 能够被赋值给变量,
    - 可以作为集合对象的元素,
    - 还能够作为函数的参数以及返回值.

为什么我在这里要强调 Python 中的函数是一等公民呢? 因为在很多其他诸如 C, C++, Java 等语言中, 函数和整数/字符串/字典/列表等对象地位并不是平等的. 这是 Python 一个非常重要的特点.

Python 中的函数之所以是一等公民, 是因为 Python 中的一切都是对象, 即 *everything in python is an object*. 换句话说:  Python 中函数是一等公民这一现象是 Python 一切皆对象的必然结果.

.. code_file:: examples/object/first_class_public/function_is_object.py

.. python:: examples/object/first_class_public/function_is_object.py

既然函数是一等公民, 那么他可以给起个别名, 或者是带入到函数的入参中. 如下面的代码, 函数 :py:`fib` 可以赋给 :py:`a`, 然后调用 :py:`a` 就等价于调用 :py:`fib`. :py:`fib` 也可以作为 :py:`map` 的入参, 这使得在 Python 当中, 很容易实现函数式编程.

.. code_file:: examples/object/first_class_public/name_a_function.py

.. python:: examples/object/first_class_public/name_a_function.py

.. hint::

    装饰器本身就是一个参数和返回值都是函数的函数.

除了 :py:`map` 之外, Python 中还有很多函数的参数都是函数, 比如:

- :py:`sorted` 函数的 :py:`key` 参数.
- :py:`filter` 函数的第一个参数.

.. caution::

    事实上, :py:`map` 和 :py:`filter` 并不是函数, 而是类. 比较严谨的说法是 :py:`filter` 初始化函数 :py:`__init__` 的第一个参数是一个函数.

在 Python 中, 还提供了匿名函数, 你可以像调用对象一样来调用匿名函数.

.. _lambda_expressions:

.. code_file:: examples/object/first_class_public/lambda_expressions.py

.. python:: examples/object/first_class_public/lambda_expressions.py

在 Python 中, 这被称为 Lambda 表达式, 考虑到函数也是对象, 本质上, Lambda 表达式是 Python 提供的一个语法糖. :numref:`lambda_expressions` 展开即\ :numref:`lambda_expressions_modified`. 根据他们的运行结果也可以看出二者是一样的.

.. _lambda_expressions_modified:

.. code_file:: examples/object/first_class_public/lambda_expressions_modified.py

.. python:: examples/object/first_class_public/lambda_expressions_modified.py

由于 Python 的 Lambda 表达式表达能力孱弱, 定义体本身只能使用纯表达式, 因此, 在 Lambda 表达式中:

- 不能有赋值语句.
- 不能有流程控制关键词, 比如 :py:`while`, :py:`try` 等关键词.

当某个函数满足:

- 作为参数传递给其他参数,
- 可以写成纯表达式,
- 其他地方不会再使用这个函数,
- 你实在是不知道给这个函数如何命名,

这四个条件时, 才建议使用匿名函数.

在 Python 中, 函数是一等公民, 是一个真正的对象, 同时, 对象也可以表现的像函数一样, 只需要实现对象的 :py:`__call__` 方法即可, 比方说, 可以像\ :numref:`callable_object` 一样实现一个 :py:`add` 函数.

.. _callable_object:

.. code_file:: examples/object/first_class_public/callable_object.py

.. python:: examples/object/first_class_public/callable_object.py

实际上, 普通函数也有 :py:`__call__` 方法, 在 99% 的情况下, 调用 :py:`__call__` 方法和直接调用函数是一样的.

.. code_file:: examples/object/first_class_public/define_a_function.py

.. python:: examples/object/first_class_public/define_a_function.py

那 1% 的情况是什么呢?

.. _modify_call_method:

.. code_file:: examples/object/first_class_public/modify_call_method.py

.. python:: examples/object/first_class_public/modify_call_method.py

我们可以看到, 在\ :numref:`modify_call_method` 中, 函数 :py:`add` 的 :py:`__call__` 方法已经被替换成了 :py:`sub` 的 :py:`__call__` 方法了. 此时直接调用 :py:`add` 方法和调用 :py:`add` 函数的 :py:`__call__` 方法得到的结果是不同的.

.. hint::

    在没有充分了解 Python 运作机制的情况下, 请不要像\ :numref:`modify_call_method` 中一样通过 MonkeyPatch 的方式修改 Python 的对象, 以防止不可预期的情况发生.
