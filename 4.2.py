import random

xing = ['赵', '张', '王', '郑', '徐']

ming = ['一', '二', '三', '四', '五', '六', '七', '八']


def fake_name():
    xing_g = random.choice(xing)

    ming_g = ''.join(random.sample(ming, random.randint(1, 2)))

    fake_name = xing_g + ming_g

    return fake_name


fake_names = []
for i in range(3):
    fake_names.append(fake_name())
print(fake_names)
