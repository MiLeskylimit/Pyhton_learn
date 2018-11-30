'''
定义一个学生类，用来形容学生
'''
# 定义一个空类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass
# 定义一个对象
mingyue = Student()

# 定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 1.  def 的缩进层级
    # 2.　系统默认由一个self参数
    def doHomework(self):
        print("I do HomeWork")
        
        # 推荐在函数末尾使用return语句
        return
# 实例化
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()

# 定义一个类
class GitHub():
    address = "github.com"
    user = None
    password = "xxxx"

    def LogInGitHub(self):
        print("Open https://github.com")
        return

# 实例化
gitlog = GitHub()
print(gitlog.address)
gitlog.LogInGitHub()


