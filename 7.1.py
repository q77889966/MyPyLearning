import pickle

# 定义一个简单的函数
def add_numbers(a, b):
    return a + b

def save_and_load_function():
    # 将函数对象保存到文件中
    with open('1.txt', 'wb') as f:
        pickle.dump(add_numbers, f)

    # 从文件中读取函数对象并调用它
    with open('1.txt', 'rb') as f:
        function = pickle.load(f)
        result = function(2, 3)
        print(result)

save_and_load_function()