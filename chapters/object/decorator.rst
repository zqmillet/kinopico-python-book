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

其中 :py:`LOAD_FAST(var_num)` 和 :py:`LOAD_GLOBAL(namei)` 都很好理解, 分别是加载局部变量, 一个是加载全局变量. 我们注意到, 在\ :numref:`define_a_function_with_closure_dis` 中除了 :py:`LOAD_DEREF(i)` 还有一个特殊的操作 :py:`STORE_DEREF(i)`, 关于这个操作在 Python 的官方文档中也有说明:

- :py:`STORE_DEREF(i)`: Stores TOS into the cell contained in slot i of the cell and free variable storage.

:py:`LOAD_DEREF(i)` 和 :py:`STORE_DEREF(i)`: 这两个操作就是用来实现闭包的. 为什么会存在闭包这个特性呢? 我们都知道, 局部变量的生命周期只存在于这个函数, 如果函数结束了, 那么局部变量的生命周期也结束了. 这个特性如果作用在装饰器上就会出现问题, 比如在\ :numref:`define_a_function_with_closure_code` 中, 函数 :py:`get_function` 中定义了一个函数 :py:`function`, 而在这个 :py:`function` 中, 又引用了局部变量 :py:`a`. 如果这个局部变量 :py:`a` 在函数 :py:`get_function` 结束的时候被销毁了, 那么调用 :py:`function` 的时候就会出现找不到 :py:`a` 的错误. 为了解决这个问题, 所以必须将 :py:`a` 保存起来, 考虑到 :py:`a` 既不是全局变量, 也不能是局部变量, 因此只能将 :py:`a` 这个对象保存在函数 :py:`function` 的的某个空间下, 这个特性就是闭包.

函数 :py:`function` 有一个名为 :py:`__closure__` 的属性, 如\ :numref:`print_closure_code` 所示.

.. _print_closure_code:

.. code_file:: examples/object/decorator/print_closure.py

其运行结果如下所示, 根据运行结果, 我们可以得到几个结论:

- 如果一个函数存在闭包, 那么它的 :py:`__closure__` 是一个 :py:`tuple` 类型, 否则 :py:`__closure__` 的值为 :py:`None`.
- :py:`__closure__` 中元素的类型是 :py:`cell`, 元素个数为闭包变量的数量.
- :py:`__closure__` 中元素的 :py:`cell_contents` 属性为闭包变量的值.

.. python:: examples/object/decorator/print_closure.py

:numref:`print_closure_code` 的反汇编代码如\ :numref:`print_closure_dis` 所示. 注意其中的第 2, 3, 5 行反汇编的内容, 可以看出 Python 分别在第 2 行和第 3 行调用了两次 :py:`STORE_DEREF`, 将 :py:`a` 和 :py:`b` 保存到函数的 :py:`__closure__` 字段中. 在第 5 行调用两次 :py:`LOAD_DEREF` 将 :py:`__closure__` 中的变量加载到内存中进行计算.

.. _print_closure_dis:

.. dis:: examples/object/decorator/print_closure.py
