.. _section_reference:

变量引用
========

在 Python 中, 所谓的变量, 只是对象的一个引用符号, 在赋值的过程中, 不存在对象的拷贝过程.

读者可以考虑一下\ :numref:`assignment_of_int_code` 会打印什么信息.

.. _assignment_of_int_code:

.. code_file:: examples/object/reference/assignment_of_int.py

相等自不必说, 第一个输出必然是 :py:`True`, 问题是第二个也是 :py:`True` 吗? 我们可以看一下这段代码的运行结果, 如下所示.

.. python:: examples/object/reference/assignment_of_int.py

我们可以发现, 第二个结果也是 :py:`True`. 这说明, 当执行 :py:`b = a` 时, 并不是将 :py:`a` 的值赋给新的变量 :py:`b`, 而是将引用符号 :py:`b` 的地址指向了引用符号 :py:`a` 所指向的内容. 所以, :py:`a` 和 :py:`b` 的地址是一样的.

如\ :numref:`symbol_and_objects_1` 所示, 蓝色的是引用符号, 绿色的是内存中的对象. 当执行 :py:`b = a` 的时候, 并没有重新构造一个 :py:`1` 的对象, 而是直接把 :py:`a` 所指的对象赋给了 :py:`b`.

.. _symbol_and_objects_1:

.. tikz:: 符号与对象

    \node[reference] (a)  at (0, 1.0) {a};
    \node[reference] (b)  at (0, 0.0) {b};
    \node[object]    (o1) at (3, 1.0) {1};
    \node[code]           at (4, 0.0) {>>> b = a};
    \node[code]           at (4, 1.0) {>>> a = 1};
    \node[plaintext]      at (0, 1.7) {symbol};
    \node[plaintext]      at (3, 1.7) {object};
    \node[plaintext]      at (5, 1.7) {code};

    \draw[ref] (a) -- (o1);
    \draw[ref] (b) -- (o1);

如果 :py:`a` 的地址和 :py:`b` 的地址是一样的, 我们修改 :py:`a` 的值, 那么 :py:`b` 会随着变化吗? 读者可以思考一下\ :numref:`change_value_code` 运行的结果是什么.

.. _change_value_code:

.. code_file:: examples/object/reference/change_reference_value.py

由于 :py:`a` 和 :py:`b` 指向同一个对象的地址, 修改 :py:`a` 的值, 那么 :py:`b` 的值也一定会发生更改, 因此, 此时输出 :py:`b` 的值应该是 :py:`2`. 然而事实上, 从如下显示的执行结果显示 :py:`b` 的值并没有发生变化. 这好像跟之前说的不太一样?

.. python:: examples/object/reference/change_reference_value.py

这个结果跟之前表述的观点并不矛盾, 原因在于, 当执行 :py:`a = 2` 时, 不是将 :py:`a` 所指的对象的值改为 :py:`2`, 而是将引用符号 :py:`a` 指向新的对象 :py:`2` 上了, 此时 :py:`b` 所指的对象仍然是 :py:`1`.

.. admonition:: 结论

    在 Python 中, 当执行赋值语句时, 并不是修改等号左边变量的值, 而是将等号左边的引用符号指向等号右边的对象.

这个结论有什么用吗? 我套用 C, C++ 等语言的赋值语句来理解 Python 的赋值语句不可以吗? 答案是: 可以, 但不完全可以. 读者可以思考一下\ :numref:`change_list_code` 的输出结果是什么.

.. _change_list_code:

.. code_file:: examples/object/reference/change_list.py

输出结果如下所示, 有没有跟你想的不一样呢?

.. python:: examples/object/reference/change_list.py

你会有这种疑问吗: :py:`a[0]` 的值指向了一个新的字符串, 为什么 :py:`b[0]` 的值也跟着变化了?

.. hint::

    :py:`a` 中的元素也并不是对象, 而是对象的引用.

上述问题, 读者可以自行思考.

.. admonition:: 深度思考

    在 Python 中, 可以创建出真正的常量吗? 即不可以作左值的对象.

至此, 我们回头看\ :numref:`section_implicit_type` 中最后的疑问, 是不是对如下代码有了更深的理解.

.. code-block:: python

   a = '1'
   a = 1 + 3

在上述代码中, 并不是变量 :py:`a` 的类型发生了变化, 而是引用符号 :py:`a` 指向了整数 :py:`4`. 整个过程中, 对象的类型没有任何隐式或者显式的转换. 因此, 再次重申: Python 是一门强类型语言.
