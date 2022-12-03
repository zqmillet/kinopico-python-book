.. _section_reference:

变量引用
========

.. admonition:: 先提出一个爆论

    在 Python 中, 是不存在赋值操作的.

那么问题来了, 当执行 :py:`a = 1` 时, 这难道不是赋值操作吗?

确实不是赋值, 事实上 Python 在执行 :py:`a = 1` 时做了两个操作:

- 创建一个整数 :py:`1` 对象,
- 给这个对象起一个名字 :py:`a`.

而并不是:

- 创建一个整数变量 :py:`a`,
- 然后将 :py:`a` 赋值成 :py:`1`.

请读者细细体会这两种描述的区别, 这也是 Python 有别于其他语言的一个很重要的特征. 请看以下代码, 并判断最终的输出是什么.

.. _assignment_of_int_code:

.. literalinclude:: /examples/object/reference/assignment_of_int_1.py
   :caption: ``examples/object/reference/assignment_of_int_1.py``

按照我们的之前的解释, 在\ :numref:`assignment_of_int_code` 中:

- 创建了一个 :py:`int` 变量 :py:`1`,
- 给这个变量添加一个名字 :py:`a`,
- 创建了一个 :py:`int` 变量 :py:`1`,
- 给这个变量添加一个名字 :py:`b`.

由于 :py:`a` 和 :py:`b` 是两个不同的对象, 因此 :py:`a` 和 :py:`b` 的地址是不同的. 所以最终的输出应该是 :py:`a is not b`. 我们执行一下\ :numref:`assignment_of_int_code`, 其输出如下所示.

.. bash:: python3 examples/object/reference/assignment_of_int_1.py

好像哪里不对劲, 跟我们之前分析的有一些出入. 这是由于 Python 会将一些常用的整数缓存起来, 不会每次都重新构造一个新的对象. 笔者使用的 Python 版本为 |python_version|, 操作系统为 |os|, 在该版本中, 范围在 :math:`[-5, 256]` 之间的整数都会被缓存到内存中, 为了验证我们的结论, 我们将\ :numref:`assignment_of_int_code` 稍加改动, 执行结果就完全不一样了.

.. _assignment_of_int_code_257:

.. literalinclude:: /examples/object/reference/assignment_of_int_257.py
   :caption: ``examples/object/reference/assignment_of_int_257.py``

我们执行一下\ :numref:`assignment_of_int_code_257`.

.. bash:: python3 examples/object/reference/assignment_of_int_257.py

额, 结果非常出乎我们的意料. 读者们, 请听我解释, 是酱紫的. Python 在运行脚本的时候, 已经拿到了所有的信息, 会做一些性能上的优化工作. 于是两个 :py:`257` 就被优化成了一个对象. 如果用 Python 的交互模式来执行这段代码, 结果就不一样了.

.. python::

    a = 1
    b = 1
    if a is b:
        print('a is b')
    else:
        print('a is not b')

    a = 257
    b = 257
    if a is b:
        print('a is b')
    else:
        print('a is not b')

    exit()

如果 :py:`a` 的地址和 :py:`b` 的地址是一样的, 我们修改 :py:`a` 的值, 那么 :py:`b` 会随着变化吗? 读者可以思考一下\ :numref:`change_value_code` 运行的结果是什么.

.. _change_value_code:

.. literalinclude:: /examples/object/reference/change_reference_value.py
   :caption: ``examples/object/reference/change_reference_value.py``

由于 :py:`a` 和 :py:`b` 指向同一个对象的地址, 修改 :py:`a` 的值, 那么 :py:`b` 的值也一定会发生更改, 因此, 此时输出 :py:`b` 的值应该是 :py:`2`.

.. bash:: python3 examples/object/reference/change_reference_value.py

然而事实上, 执行结果显示 :py:`b` 的值并没有发生变化. 这好像跟之前说的不太一样? 这个结果跟之前表述的观点并不矛盾, 原因在于, 当执行 :py:`a = 2` 时, 不是将 :py:`a` 所指的对象的值改为 :py:`2`, 而创建了一个对象 :py:`2`, 然后给这个对象起名为 :py:`a`, 此时 :py:`a` 不再是对象 :py:`1` 的名字, 但是 :py:`b` 仍然是对象 :py:`1` 的名字, 当我们访问 :py:`b` 的值, 当然还是 :py:`1`.

知道这个有什么用吗? 我套用 C, C++ 等语言的赋值语句来理解 Python 的赋值语句不可以吗? 答案是: 可以, 但不完全可以. 读者可以思考一下\ :numref:`change_list_code` 的输出结果是什么.

.. _change_list_code:

.. literalinclude:: /examples/object/reference/change_list.py
   :caption: ``examples/object/reference/change_list.py``

输出结果如下所示, 有没有跟你想的不一样呢?

.. bash:: python3 examples/object/reference/change_list.py

.. admonition:: 你会有这种疑问吗?

    :py:`a[0]` 的值指向了一个新的字符串, 为什么 :py:`b[0]` 的值也跟着变化了?

.. hint::

    当执行 :py:`a = [1, 2, 3]` 时:

    - 创建了一个列表 :py:`[1, 2, 3]`,
    - 给这个列表起一个名字 :py:`a`.

    当执行 :py:`b = a` 时:

    - 等号的右边是一个已存在的对象, 直接加载这个对象, 而不是重新构造,
    - 给这个对象起了另一个名字 :py:`b`, 此时 :py:`b` 和 :py:`a` 的地址是相同的.

    当执行 :py:`a[0] = 'he'` 时:

    - 修改了 :py:`a` 所指对象中元素的值,
    - 由于 :py:`b` 也指的同一个对象, 因此 :py:`b[0]` 的值也发生了变化.

至此, 我们回头看\ :numref:`section_implicit_type` 中最后的疑问, 是不是对如下代码有了更深的理解.

.. code-block:: python

   a = '1'
   a = 1 + 3

在上述代码中, 并不是变量 :py:`a` 的类型发生了变化, 而是:

- 创建字符串对象 :py:`'1'`,
- 将其起名为 :py:`a`,
- 创建整数对象 :py:`4`,
- 将其起名为 :py:`a`,

整个过程中, 对象的类型没有任何隐式或者显式的转换. 因此, 再次重申: Python 是一门强类型语言.

有人要问, 你讲了这么多, 有什么证据吗? 有的, 我们通过分析 Python 字节码的反汇编就可以看出 Python 底层的运行逻辑. 以下两段代码分别是 Python 源代码以及对应的反汇编.

.. literalinclude:: /examples/object/reference/assignments.py
   :caption: ``examples/object/reference/assignments.py``
   :linenos:

.. bash:: cat examples/object/reference/assignments.py | python3 -m dis

其中:

- :py:`LOAD_CONST` 用于构造一个整数,
- :py:`LOAD_NAME` 用于从名字中加载对象,
- :py:`STORE_NAME` 用于给一个对象起名字.

.. admonition:: 思考题

    在 Python 中, 可以定义一个常量吗? 即只可以被定义, 不可以被修改的变量.

.. mutable, immutable

