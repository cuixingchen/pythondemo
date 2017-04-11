#!/usr/bin/python
import subprocess
import os
import signal

'''
subprocess.Popen()
class Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)，举例：
>>> import subprocess
>>> child = subprocess.Popen(['ping','-c','4','blog.linuxeye.com'])
>>> print 'parent process'
从运行结果中看到，父进程在开启子进程之后并没有等待child的完成，而是直接运行print。
对比等待的情况:
>>> import subprocess
>>> child = subprocess.Popen('ping -c4 blog.linuxeye.com',shell=True)
>>> child.wait()
>>> print 'parent process'
'''
'ping例'


class SubprocessDemo:
    def testPing(self):
        child = subprocess.Popen(["ping", "-c", "5", "www.google.com"])
        print(child.poll())
        child.wait()
        print("parent process")

    def testDh(self):
        p = subprocess.Popen("df -h",
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True)
        print(p.poll())
        # if p.poll() is None:
        #     p.terminate()
        # p.wait()
        p.communicate()
        print(p.returncode)
        print("end")

x = SubprocessDemo()
# x.testPing()
x.testDh()
