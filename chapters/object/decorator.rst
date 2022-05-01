装饰器
======

装饰器说白了, 就是一个加工函数的函数.

比如, 我想打印函数的执行时间, 那么可以定义一个装饰器, 如\ :numref:`time_decorator` 所示.

.. _time_decorator:

.. code_file:: examples/object/decorator/time_decorator.py

.. python:: examples/object/decorator/time_decorator.py

装饰器说难很难, 说简单也很简单, 关键在于理解 Python 的闭包. 如果要理解闭包, 要明白 Python 在执行的过程中, 是怎么根据名字来查找变量的. 为了搞清楚这个问题, 我们写三段代码, 分别是\ :numref:`define_a_function_with_local_code`, :numref:`define_a_function_with_global_code` 和\ :numref:`define_a_function_with_closure_code`.

.. _define_a_function_with_local_code:

.. code_file:: examples/object/decorator/define_a_function_with_local.py

.. _define_a_function_with_global_code:

.. code_file:: examples/object/decorator/define_a_function_with_global.py

.. _define_a_function_with_closure_code:

.. code_file:: examples/object/decorator/define_a_function_with_closure.py

这三段代码的反汇编分别是\ :numref:`define_a_function_with_local_dis`, :numref:`define_a_function_with_global_dis` 和\ :numref:`define_a_function_with_closure_dis`.

.. _define_a_function_with_local_dis:

.. dis:: examples/object/decorator/define_a_function_with_local.py

.. _define_a_function_with_global_dis:

.. dis:: examples/object/decorator/define_a_function_with_global.py

.. _define_a_function_with_closure_dis:

.. dis:: examples/object/decorator/define_a_function_with_closure.py

- 根据\ :numref:`define_a_function_with_local_code` 和 :numref:`define_a_function_with_local_dis` 可以看出, 在引用 :py:`a` 时, Python 使用的是 :py:`LOAD_FAST`.
- 根据\ :numref:`define_a_function_with_global_code` 和 :numref:`define_a_function_with_global_dis` 可以看出, 在引用 :py:`a` 时, Python 使用的是 :py:`LOAD_GLOBAL`.
- 根据\ :numref:`define_a_function_with_closure_code` 和 :numref:`define_a_function_with_closure_dis` 可以看出, 在引用 :py:`a` 时, Python 使用的是 :py:`LOAD_DEREF`.

那么问题来了, :py:`LOAD_FAST`, :py:`LOAD_GLOBAL` 和 :py:`LOAD_DEREF` 各是做什么的呢? 这个在 Python 的\ `官方文档 <https://docs.python.org/3/library/dis.html>`_\ 中是有说明的:

- :py:`LOAD_FAST(var_num)`: Pushes a reference to the local :py:`co_varnames[var_num]` onto the stack.
- :py:`LOAD_GLOBAL(namei)`: Loads the global named :py:`co_names[namei]` onto the stack.
- :py:`LOAD_DEREF(i)`: Loads the cell contained in slot :py:`i` of the cell and free variable storage. Pushes a reference to the object the cell contains on the stack.
