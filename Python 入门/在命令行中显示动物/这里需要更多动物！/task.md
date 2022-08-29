
# 引子

众所周知，动物园中肯定不止一种动物。如何在众多动物中选择一种并展示呢？

这里我们需要用到 Python 中的一种叫做 **字典** 的数据结构。顾名思义，字典是一个可以通过输入的内容查询对应值的数据结构。

# 字典

## 创建字典

字典的创建非常简单，有两种：使用 `{}` 和 `dict()` 函数。

```python
# 创建一个空的字典
empty_dict1 = {}
# 同时也可以这样
empty_dict2 = dict()
```

当然，如果需要在创建时候就在里面添加一些东西，这两种也都是支持的：

```python
# 创建一个包含一个键值对的字典
dict1 = {'key1': 'value1'}
# 同时也可以这样
dict2 = dict(key1='value1')
```
创建时还需要注意，字典的键必须是唯一的

```python
# 这个字典是错误的，运行时候会报错，同时在 IDE 编辑中你也会看到错误的提示
dict1 = {'key1': 'value1', 'key1': 'value2'}
```

## 字典的查询

一本现实中的字典，核心功能是查询需要查找的字/词。Python 中的字典也一样，它的一个核心功能就是查询。

```python
# 初始化字典
dict1 = {'key1': 'value1', 'key2': 'value2'}
# 查询 key1 的值
print(dict1['key1'])  # 运行此行，将输出：value1
# 你不能查询一个不存在的键
print(dict1['key3'])  # 运行此行，将抛出 KeyError 异常
```

同时，因为字典也是一种"对象"，有一种名为`.get()`的方法，可以让你查询一个不存在的键时，不会抛出异常。

```python
# 初始化字典
dict1 = {'key1': 'value1', 'key2': 'value2'}
# 查询 key1 的值
print(dict1.get('key1'))  # 运行此行，将输出：value1
# 此时你可以安全的查找，即使字典中没有对应的键，也不会报错，相反会返回一个 None
print(dict1.get('key3'))  # 运行此行，将输出：None
# 更有用的是，get() 可以指定默认值
print(dict1.get('key3', 'default'))  # 运行此行，将输出：default
```

## 字典的修改

字典的修改也很简单，只需要把键和值对应起来即可。

```python
# 初始化字典
dict1 = {'key1': 'value1', 'key2': 'value2'}
# 修改 key1 的值
dict1['key1'] = 'value3'
# 查看修改后的字典
print(dict1)  # 运行此行，将输出：{'key1': 'value3', 'key2': 'value2'}

# 也可以用这种方式新增一个键值对
dict1['key3'] = 'value3'
# 查看修改后的字典
print(dict1)  # 运行此行，将输出：{'key1': 'value3', 'key2': 'value2', 'key3': 'value3'}
```

## 删除字典元素

如果你需要删除字典中的元素，可以使用 `del` 函数。

```python
# 初始化字典
dict1 = {'key1': 'value1', 'key2': 'value2'}
# 删除 key1
del dict1['key1']
# 查看删除后的字典
print(dict1)  # 运行此行，将输出：{'key2': 'value2'}
```

## 字典的遍历

有时候，我们会需要查看字典中的全部元素，此时我们需要遍历字典：

```python
# 初始化字典
dict1 = {'key1': 'value1', 'key2': 'value2'}
# 遍历字典
for key in dict1:
    print(key)  # 运行此行，将输出：key1 key2
```

同时，字典还包括了 `.keys()` 和 `.values()` 方法，可以获取字典中的所有键或者所有值。

```python
# 初始化字典
dict1 = {'key1': 'value1', 'key2': 'value2'}
# 获取字典中的所有键
print(dict1.keys())  # 运行此行，将输出：dict_keys(['key1', 'key2'])
# 获取字典中的所有值
print(dict1.values())  # 运行此行，将输出：dict_values(['value1', 'value2'])
```

聪明的你也应该发现了，在很多情况下，直接遍历字典和遍历字典的所有键是等效的。

```python
# 初始化字典
dict1 = {'key1': 'value1', 'key2': 'value2'}
# 遍历字典
for key in dict1:
    print(key)  # 运行此行，将输出：key1 key2
# 遍历字典的所有键
for key in dict1.keys():
    print(key)  # 运行此行，也将输出：key1 key2
```

如果需要让键和对应值一同遍历，一个更好的方法是使用 `.items()` 方法。

```python
# 初始化字典
dict1 = {'key1': 'value1', 'key2': 'value2'}
# 遍历字典
for key, value in dict1.items():
    print(key, value)  # 运行此行，将输出：key1 value1 [此处会换行]key2 value2
```

# 动手实践

那么，我们知道了如何创建字典，如何查看字典中的全部元素，如何修改字典中的元素，如何删除字典中的元素，如何遍历字典，如何获取字典中的所有键和所有值。

现在是时候将动物的图形保存到 **字典** 中了
