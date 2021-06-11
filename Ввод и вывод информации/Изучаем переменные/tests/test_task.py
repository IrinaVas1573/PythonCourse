import unittest
import subprocess

# from ..task import num, AxBy, TU154, it10, _AbbA, This_and_that
# answer = " ".join([num, AxBy, TU154, it10, _AbbA, This_and_that])
with open('task.py') as fout:
    with open('tests\\taskTest.py', 'w') as f:
        f.write(fout.read())
        f.write('''
print(num,AxBy,TU154,it10,_AbbA,This_and_that)
#         ''')
answer = ""

# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_print(self):
        subpr1 = subprocess.Popen(["python", "tests\\taskTest.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        printOut = subpr1.stdout.read()
        err = subpr1.stderr.read()
        subpr1.kill()
        print(err)
        self.assertEqual(printOut, answer, msg="Сообщение!")
