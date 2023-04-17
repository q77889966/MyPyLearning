import random

xing = ['赵', '张', '王', '郑', '徐']
ming = ['一', '二', '三', '四', '五', '六', '七', '八']


def fake_name():
    xing_g = random.choice(xing)
    ming_g = ''.join(random.sample(ming, random.randint(1, 2)))
    fake_name = xing_g + ming_g
    return fake_name

def generate_scores():
    scores = [round(random.uniform(0, 100), 1) for _ in range(3)]         #下划线取消循环变量
    return scores


scores_dict = {}
for i in range(3):
    fake_names = fake_name()
    scores = generate_scores()
    scores_dict[fake_names] = scores
print(scores_dict)
