一切皆对象
==========

不知道大家有没有注意到, 在\ :numref:`section_reference` 中, 我说当执行 :py:`a = 1` 时, 是将引用符号 :py:`a` 指向了 :py:`1` 这个对象. 不知道读者是否有过疑问, 在 Python 中, :py:`1` 也是一个对象吗?

是的. 在 Python 中, 一切都是对象. Python 在面向对象方面, 贯彻的非常彻底.

我们可以看一下\ :numref:`members_of_int_code`, 整数 :py:`1` 是有成员方法 :py:`__dir__` 的, 而且成员方法 :py:`__dir__` 的返回值是该对象的所有成员名称.

.. _members_of_int_code:

.. code_file:: examples/object/all_are_objects/members_of_int.py

:numref:`members_of_int_code` 的执行结果如下所示.

.. _members_of_int_output:

.. python:: examples/object/all_are_objects/members_of_int.py

从上面这个例子我们可以看出来, 简单如整数 :py:`int`, 在 Python 中都是对象.

我们知道, 在面向对象编程中, 对象是类 :py:`class` 的实例, 那么, :py:`class` 难道也是对象?

是的!

.. code_file:: examples/object/all_are_objects/class_is_object.py

.. python:: examples/object/all_are_objects/class_is_object.py

有的人会有疑问: 那函数也是对象? 必须的!

.. code_file:: examples/object/all_are_objects/function_is_object.py

.. python:: examples/object/all_are_objects/function_is_object.py

.. admonition:: 深度思考

    可否实现一个对象 :py:`obj`, 使得 :py:`isinstance(obj, object)` 的值是 :py:`False`?
