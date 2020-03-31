# def person_info(name, age, *, city, job):
#     print(name, age, city, job)
#
#
# person_info('linda', 18, city='beijing', job='test engineering')


def func(a, b, c=0, *args, **kwargs):
    print("a=", a, "b=", b, "c=", c, 'args=', args, 'kwargs=', kwargs)


func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)
func(1, 2, 3, *('a', 'b', 12), **{'name': 'linda', 'age': 18})
