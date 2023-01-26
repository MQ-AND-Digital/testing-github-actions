import HelloWorld

# content of test_sample.py
def func(x):
  return x + 1

def test_answer():
  assert func(3) == 4

def test_answer_2():
  assert func(3) == 5

def test_hello_world(capfd):
  HelloWorld.main()
  out, err = capfd.readouterr()
  assert out == "Hello World!\n"