装饰器
======

装饰器说白了, 就是一个加工函数的函数. 我们通常用的 :py:`@` 操作符是一个语法糖. :numref:`decorator_demo_1` 和\ :numref:`decorator_demo_2` 的含义是相同的.

.. _decorator_demo_1:

.. code_file:: examples/object/decorator/demo_1.py

.. _decorator_demo_2:

.. code_file:: examples/object/decorator/demo_2.py

:numref:`decorator_demo_1` 和\ :numref:`decorator_demo_2` 反汇编代码如\ :numref:`decorator_demo_1_dis` 和\ :numref:`decorator_demo_2_dis` 所示, 可以看出, 二者都是通过 :py:`CALL_FUNCTION` 调用函数 :py:`decorator` 修饰器, 并且通过 :py:`STORE_NAME` 将 :py:`decorator` 的返回值保存到 :py:`function` 中.

.. _decorator_demo_1_dis:

.. dis:: examples/object/decorator/demo_1.py

.. _decorator_demo_2_dis:

.. dis:: examples/object/decorator/demo_2.py

装饰器有很多应用场景, 比如, 我想打印函数的执行时间, 那么可以定义一个装饰器, 如\ :numref:`time_decorator` 所示.

.. _time_decorator:

.. code_file:: examples/object/decorator/time_decorator.py

.. python:: examples/object/decorator/time_decorator.py

通常情况下, 修饰器并不会这么简单, 而是会携带一些可配置的参数, 比如, 我们要在\ :numref:`time_decorator` 的基础上添加一个消息模板的参数, 实现代码如\ :numref:`time_decorator_with_arguments` 所示.

.. _time_decorator_with_arguments:

.. code_file:: examples/object/decorator/time_decorator_with_arguments.py

.. python:: examples/object/decorator/time_decorator_with_arguments.py

我们都知道, 在 Python 中, 局部变量的生命周期与所在函数的生命周期一致, 如果函数结束了, 那么局部变量的生命周期也结束了. 这个特性如果作用在装饰器上就会出现问题, 比如在\ :numref:`time_decorator_with_arguments` 中, 函数 :py:`_print_time` 用到了 :py:`message` 变量, 这个变量是来自函数 :py:`print_time` 的, 当调用 :py:`_print_time` (也就是 :py:`add` 函数) 时, 函数 :py:`print_time` 已经结束运行了, 按理说变量 :py:`message` 也一同消失了, 但是根据执行结果可以看出在调用 :py:`_print_time` 时变量 :py:`message` 仍然存在.

那么 Python 是怎么解决这个问题的呢? 我们来看一下\ :numref:`time_decorator_with_arguments` 的反汇编代码, 如\ :numref:`time_decorator_with_arguments_dis` 所示.

.. _time_decorator_with_arguments_dis:

.. dis:: examples/object/decorator/time_decorator_with_arguments.py
   :begin: 4
   :end: 13

通过\ :numref:`time_decorator_with_arguments` 和\ :numref:`time_decorator_with_arguments_dis` 对照, 我们可以看出:

- 在第 5 行, 在定义函数 :py:`wrapper` 时, 执行 :py:`LOAD_CLOSURE` 将变量 :py:`message` 保存在函数 :py:`wrapper` 中.
- 在第 7 行, 在定义函数 :py:`_print_time` 时, 执行 :py:`LOAD_CLOSURE` 将变量 :py:`message` 保存在函数 :py:`_print_time` 中.
- 在第 10 行, 在调用变量 :py:`message` 时, 执行 :py:`LOAD_DEREF` 将变量 :py:`message` 加载回来.

.. hint::

    在 Python 的\ `官方文档 <https://docs.python.org/3/library/dis.html>`_\ 中, 有关于 :py:`LOAD_CLOSURE` 和 :py:`LOAD_DEREF` 的解释.

    - :py:`LOAD_CLOSURE(i)`: Pushes a reference to the cell contained in slot :py:`i` of the cell and free variable storage. The name of the variable is :py:`co_cellvars[i]` if :py:`i` is less than the length of :py:`co_cellvars`. Otherwise it is :py:`co_freevars[i - len(co_cellvars)]`.
    - :py:`LOAD_DEREF(i)`: Loads the cell contained in slot :py:`i` of the cell and free variable storage. Pushes a reference to the object the cell contains on the stack.

修饰器中的参数或者状态变量, 会通过闭包的方式逐层的传递到内层的函数, 从而解决变量生命周期提前结束的问题.

.. :py:`message` 参数, 而在这个 :py:`function` 中, 又引用了局部变量 :py:`a`. 如果这个局部变量 :py:`a` 在函数 :py:`get_function` 结束的时候被销毁了, 那么调用 :py:`function` 的时候就会出现找不到 :py:`a` 的错误. 为了解决这个问题, 所以必须将 :py:`a` 保存起来, 考虑到 :py:`a` 既不是全局变量, 也不能是局部变量, 因此只能将 :py:`a` 这个对象保存在函数 :py:`function` 的的某个空间下, 这个特性就是闭包.

.. 在\ :numref:`find_variable` 中, 我们用了大段的篇幅来讨论在 Python 中如何查找一个变量的值, 目的是为了引出函数闭包的概念. 那为什么会存在闭包这个特性呢?

.. 函数 :py:`function` 有一个名为 :py:`__closure__` 的属性, 如\ :numref:`print_closure_code` 所示.

.. .. _print_closure_code:

.. .. code_file:: examples/object/decorator/print_closure.py

.. 其运行结果如下所示, 根据运行结果, 我们可以得到几个结论:

.. - 如果一个函数存在闭包, 那么它的 :py:`__closure__` 是一个 :py:`tuple` 类型, 否则 :py:`__closure__` 的值为 :py:`None`.
.. - :py:`__closure__` 中元素的类型是 :py:`cell`, 元素个数为闭包变量的数量.
.. - :py:`__closure__` 中元素的 :py:`cell_contents` 属性为闭包变量的值.

.. .. python:: examples/object/decorator/print_closure.py

.. :numref:`print_closure_code` 的反汇编代码如\ :numref:`print_closure_dis` 所示. 注意其中的第 2, 3, 5 行反汇编的内容, 可以看出 Python 分别在第 2 行和第 3 行调用了两次 :py:`STORE_DEREF`, 将 :py:`a` 和 :py:`b` 保存到函数的 :py:`__closure__` 字段中. 在第 5 行调用两次 :py:`LOAD_DEREF` 将 :py:`__closure__` 中的变量加载到内存中进行计算.

.. .. _print_closure_dis:

.. .. dis:: examples/object/decorator/print_closure.py
..    :end: 6

.. 所谓的函数的闭包, 只是函数内部引用了外部的一些变量, 这些变量会被保存在函数的 :py:`__closure__` 成员中, 其生命周期与函数的生命周期一致. 闭包的存在, 使得函数有了状态.
