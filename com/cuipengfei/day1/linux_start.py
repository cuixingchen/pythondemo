#!/usr/bin/python
import subprocess


# subprocess.Popen()
# class Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
# Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)，举例：
# >>> import subprocess
# >>> child = subprocess.Popen(['ping','-c','4','blog.linuxeye.com'])
# >>> print 'parent process'
# 从运行结果中看到，父进程在开启子进程之后并没有等待child的完成，而是直接运行print。
# 对比等待的情况:
# >>> import subprocess
# >>> child = subprocess.Popen('ping -c4 blog.linuxeye.com',shell=True)
# >>> child.wait()
# >>> print 'parent process'

# ping例


class SubprocessDemo:
    @staticmethod
    def test_ping():
        child = subprocess.Popen(["ping", "-c", "5", "www.google.com"])
        print(child.poll())
        child.wait()
        print("parent process")

    @staticmethod
    def test_dh():
        p = subprocess.Popen("df -h",
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True)
        SubprocessDemo.print_stout(p)
        print("test_dh_end")

    @staticmethod
    def start_mongodb():
        echo = subprocess.Popen(['echo', SubprocessDemo.getpass()], stdout=subprocess.PIPE)
        p = subprocess.Popen("sudo -S /opt/mongodb-linux-x86_64-ubuntu1604-3.4.2/bin/mongod",
                             stdin=echo.stdout,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True)
        SubprocessDemo.print_stout(p)
        print("start_mongodb_end")

    @staticmethod
    def getpass():
        return "123456"

    @staticmethod
    def print_stout(p):
        return_code = p.poll()
        while return_code is None:
            line = p.stdout.readline()
            return_code = p.poll()
            line = line.strip()
            print(line)
        print(return_code)


x = SubprocessDemo()
# x.testPing()
# x.testDh()
x.testStartMongo()
