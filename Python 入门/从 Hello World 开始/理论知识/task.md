现在，让我们开始学习 Python.

在本次课程中，您将学习如何开发您的第一个 Python 程序。尽管这些程序非常简单，但是这会是一个好的开始。

## Hello World 程序

有一个程序员笑话：

> 某程序员退休后决定练习书法，于是重金购买文房四宝。一日，饭后突生雅兴，一番研墨拟纸，并点上上好檀香。定神片刻，泼墨挥毫，郑重地写下一行字： **Hello World！**

我们的第一个示例程序是输出一个 Hello World 的程序。这常常是一个程序员开始学习一门语言的第一个程序。

```python
print("Hello World!")
```

如你所见，这仅需要一行代码。就完成了"Hello World!"的输出。 
这段代码非常简洁，与自然语言（此处指英语）也很接近，这也是 Python 便于上手的原因之一。

## 当我们 print 时，发生了什么？

我们的代码使用了 Python 的一个内置函数 `print()`。 这个函数所做的是输出括号中所传递的字符串，但不包括两端的引号。

**函数** 是一段代码，可为您完成一些有用的工作，例如打印文本。 从某种意义上说，函数是可以在您的程序中重用的子程序。当函数名后跟括号时，表示调用它来获取结果。

在后面我们会详细讨论如何[创建一个函数]()，但在此处，我们主要讨论如何使用函数。

## 字符串

让我们更进一步，上文中我们提到，print() 函数传入的是一个字符串。也就是说`"Hello World!"`是一个字符串。所有的字符串都用英文的双引号（`"`）或单引号（`'`）括起来。
所以，我们认为`"Hello World!"`是一个合格的字符串。

你可以用另一个字符串替换这个字符串，程序将打印新的字符串。如：

```python
print("Python is easy to learn.")
```

正如你所猜到的那样，运行该程序会打印： **Python is easy to learn.**

我们还需要考虑，如果字符串中已经包括了某种引号，那么我们可以将这个字符串括在 **另一种** 类型的引号中，例如：

```python
print("I'm ready to learn Python.")
```

在这种情况下，I'm 中的`'`被正确识别为字符串的一部分，而不是外侧用于包括的引号。

如果你是用错误的方式书写：

```python
print('I'm ready to learn Python.')
```
明显的你会看到编辑器的报错，因为程序并不能理解你的字符串的开始与结束的位置。

## 多行字符串
在 Python 中，可以使用多行字符串来表示多行文本。多行字符串是用三个双引号（`"""`）或三个单引号（`'''`）括起来的文本。

```python
print('''
Hello World!
I'm ready to learn Python.
''')
```

## 中文的输出

Python 的输出是 Unicode 编码的。这意味着，你可以在输出中使用中文。

```python
print("你好，世界！")
```
这将正确运行，并打印：**你好，世界！**.

## f-string

如果你需要在字符串中打印会使用到的变量（变量我们会在后续进行更详细的说明），那么可以使用 `f-string`。

```python
name = "PEScn"
print(f"Hello, {name}!")
```

这将输出：**Hello, PEScn!**

它的构造方式为：`f'字符串'`或`f"字符串"`，其中字符串中以大括号 `{}` 包裹变量，表示在其位置上应为变量的内容。

f-string在功能方面不逊于传统的 **%-formatting** 语句和 **str.format()** 函数，同时性能又优于二者，更能让我们的代码更加简洁，并且更容易理解

#### 拓展阅读：
其他的格式化的方案可以参考 [Python 格式化字符串](https://docs.python.org/zh-cn/3/library/string.html#formatstrings) 。

## 问题

最后，我们来完成一个小练习：

以下哪些代码可以正确运行并打印字符串 `Hello World!`？

A. 
```python
print("Hello World!")
```
B. 
```python
    print('Hello World!')
```
C. 
```python
print('Hello World!')
```
D. 
```python
print(Hello World!)
```
E. 
```python
print('hello world!')
```
