# -*- coding: utf-8 -*-
import os
import unittest
import subprocess

# from ..task import num, AxBy, TU154, it10, _AbbA, This_and_that
# answer = " ".join([num, AxBy, TU154, it10, _AbbA, This_and_that])
with open(os.path.join(os.getcwd(), "task.py")) as fout:
    with open(os.path.join(os.getcwd(), "tests", "taskTest.py"), 'w') as f:
        f.write(fout.read())
        f.write('''
print(num,AxBy,TU154,it10,_AbbA,This_and_that)
#         ''')


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def someStreamCreatingProcess(self, stream1, streamdata):
        stream1.write(bytes(str(streamdata)+"\n", encoding='utf-8'))
        stream1.close()
    def CheckTask(self, data):
        subpr1 = subprocess.Popen(["python", os.path.join(os.getcwd(), "tests", "taskTest.py")], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        TestCase.someStreamCreatingProcess(self, subpr1.stdin, data)
        chek = subpr1.wait()
        err = subpr1.stderr.read()
        out1 = subpr1.stdout.read()
        subpr1.kill()
        if err:
            return "Что-то пошло не так"
        else:
            return out1.decode("utf-8").strip()
    def test_print(self):
        self.assertEqual(self.CheckTask(""), "5 mama Fly cool 8 1010", msg="Тест 1")
