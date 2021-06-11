import subprocess
import unittest
import os




# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def someStreamCreatingProcess(self, stream1, streamdata):
        stream1.write(bytes(str(streamdata)+"\n", encoding='utf-8'))
        stream1.close()
    def CheckTask(self, data):
        subpr1 = subprocess.Popen(["python", os.path.join(os.getcwd(), os.pardir, "task.py")], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        TestCase.someStreamCreatingProcess(self, subpr1.stdin, data)
        chek = subpr1.wait()
        err = subpr1.stderr.read()
        out1 = subpr1.stdout.read()
        subpr1.kill()
        if err:
            return err.decode("utf-8")
        else:
            return out1.decode("utf-8").strip()
    def test_print(self):
        self.assertEqual(self.CheckTask("3\n14"), "4", msg="Тест 1")
        self.assertEqual(self.CheckTask("14\n14"), "1", msg="Тест 2")
        self.assertEqual(self.CheckTask("6\n3"), "0", msg="Тест 3")
        self.assertEqual(self.CheckTask("3\n6"), "2", msg="Тест 4")

