.. _find_variable:

查找对象
========

Python 在执行的过程中, 是怎么根据名字来查找变量的. 为了搞清楚这个问题, 我们写三段代码, 分别是 :numref:`define_a_function_with_local_code`, :numref:`define_a_function_with_global_code` 和 :numref:`define_a_function_with_closure_code`.

.. _define_a_function_with_local_code:

.. literalinclude:: /examples/object/decorator/define_a_function_with_local.py
   :caption: ``examples/object/decorator/define_a_function_with_local.py``

.. _define_a_function_with_global_code:

.. literalinclude:: /examples/object/decorator/define_a_function_with_global.py
   :caption: ``examples/object/decorator/define_a_function_with_global.py``

.. _define_a_function_with_closure_code:

.. literalinclude:: /examples/object/decorator/define_a_function_with_closure.py
   :caption: ``examples/object/decorator/define_a_function_with_closure.py``

这三段代码的反汇编分别是 :numref:`define_a_function_with_local_dis`, :numref:`define_a_function_with_global_dis` 和 :numref:`define_a_function_with_closure_dis`.

.. _define_a_function_with_local_dis:
.. python-disassembly:: /examples/object/decorator/define_a_function_with_local.py
   :caption: ``examples/object/decorator/define_a_function_with_local.py``

.. _define_a_function_with_global_dis:
.. python-disassembly:: /examples/object/decorator/define_a_function_with_global.py
   :caption: ``examples/object/decorator/define_a_function_with_global.py``

.. _define_a_function_with_closure_dis:
.. python-disassembly:: /examples/object/decorator/define_a_function_with_closure.py
   :caption: ``examples/object/decorator/define_a_function_with_closure.py``

- 根据 :numref:`define_a_function_with_local_code` 和 :numref:`define_a_function_with_local_dis` 可以看出, 在引用 :py:`a` 时, Python 使用的是 :py:`LOAD_FAST`.
- 根据 :numref:`define_a_function_with_global_code` 和 :numref:`define_a_function_with_global_dis` 可以看出, 在引用 :py:`a` 时, Python 使用的是 :py:`LOAD_GLOBAL`.
- 根据 :numref:`define_a_function_with_closure_code` 和 :numref:`define_a_function_with_closure_dis` 可以看出, 在引用 :py:`a` 时, Python 使用的是 :py:`LOAD_DEREF`.

那么问题来了, :py:`LOAD_FAST`, :py:`LOAD_GLOBAL` 和 :py:`LOAD_DEREF` 各是做什么的呢? 这个在 Python 的\ `官方文档 <https://docs.python.org/3/library/dis.html>`_\ 中是有说明的:

- :py:`LOAD_FAST(var_num)`: Pushes a reference to the local :py:`co_varnames[var_num]` onto the stack.
- :py:`LOAD_GLOBAL(namei)`: Loads the global named :py:`co_names[namei]` onto the stack.
- :py:`LOAD_DEREF(i)`: Loads the cell contained in slot :py:`i` of the cell and free variable storage. Pushes a reference to the object the cell contains on the stack.

其中 :py:`LOAD_FAST(var_num)` 和 :py:`LOAD_GLOBAL(namei)` 都很好理解, 分别是加载局部变量和加载全局变量. 我们注意到, 在 :numref:`define_a_function_with_closure_dis` 中除了 :py:`LOAD_DEREF(i)` 还有一个特殊的操作 :py:`STORE_DEREF(i)`, 关于这个操作在 Python 的官方文档中也有说明:

- :py:`STORE_DEREF(i)`: Stores TOS into the cell contained in slot i of the cell and free variable storage.

实际上 :py:`LOAD_DEREF(i)` 和 :py:`STORE_DEREF(i)` 这两个操作就是用来实现闭包特性的.

那什么时候 Python 会使用闭包呢? 为了搞清楚这个问题, 我们又写了一段代码, 如 :numref:`load_order_code` 所示, 其反汇编代码如 :numref:`load_order_dis` 所示.

.. _load_order_code:
.. literalinclude:: /examples/object/decorator/load_order.py
   :caption: ``examples/object/decorator/load_order.py``

在 :numref:`load_order_code` 第 11 行中的 4 个变量:

- :py:`a` 只在全局被定义.
- :py:`b` 在全局以及函数 :py:`get_function` 内部被定义.
- :py:`c` 在全局, 函数 :py:`get_function`, 以及 :py:`function` 内部被定义.
- :py:`d` 在任何地方都没用被定义.

.. _load_order_dis:
.. python-disassembly:: /examples/object/decorator/load_order.py
   :caption: ``examples/object/decorator/load_order.py``

通过 :numref:`load_order_dis`, 即对 :numref:`load_order_code` 的反编译代码可以看出:

- :py:`a` 使用的是 :py:`LOAD_GLOBAL`,
- :py:`b` 使用的是 :py:`LOAD_DEREF`,
- :py:`c` 使用的是 :py:`LOAD_FAST`,
- :py:`d` 使用的是 :py:`LOAD_GLOBAL`.

这样的话, 我们可以得出 Python 根据变量名字查找变量值的优先级.

- Python 会优先使用局部变量;
- 如果在局部变量中找不到, 会在闭包中进行查找;
- 如果在局部变量和闭包中都找不到, 则在全局变量中进行查找.

.. hint::

    Python 选择使用何种方式来查找变量是在运行前就已经确定了.

.. hint::

    我们注意到, 变量 :py:`d` 并没有在任何地方被定义, 但是 Python 也会使用 :py:`LOAD_GLOBAL` 查找其值. :py:`LOAD_FAST` 可以看作是一种兜底策略, 如果在全局当中也找不到, 则抛出 :py:`NameError`.
