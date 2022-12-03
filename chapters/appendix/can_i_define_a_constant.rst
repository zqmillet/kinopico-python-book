可以创建一个常量吗?
===================

先说结论, 事实上, 在 Python 当中, 是无法创建一个常量的.

原因是在 Python 中, 无法对赋值运算符进行重载, 因此, 实现不了真正意义上的常量. 当然, 可以使用一些 OOP 的方式变相实现常量.

.. literalinclude:: /examples/appendix/define_a_constant.py

.. bash:: python3 examples/appendix/define_a_constant.py

我们可以看出, 当给 :py:obj:`CONST.PI` 赋值时, 会抛出我们定义好的异常, 从而实现了某种意义上的常量.

如果你使用 mypy 对 Python 代码进行静态检查, 可以通过静态检测的方式, 来杜绝常量被赋值.

.. literalinclude:: /examples/appendix/define_a_final.py

.. bash:: mypy examples/appendix/define_a_final.py
