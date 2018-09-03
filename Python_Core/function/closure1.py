origin = [0, 0]  # 坐标系统原点
legal_x = [0, 50]  # x轴方向的合法坐标
legal_y = [0, 50]  # y轴方向的合法坐标


def create(pos=origin):
    def player(direction, step):
        # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等
        # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step
        pos[0] = new_x
        pos[1] = new_y
        # nonlocal pos
        # pos = [new_x, new_y]    # local variable 'pos' referenced before assignment
        return pos

    return player


player = create()  # 创建棋子player，起点为原点
print(player([1, 0], 10))  # 向x轴正方向移动10步
print(origin)
print(player([0, 1], 20))  # 向y轴正方向移动20步
print(player([-1, 0], 10))  # 向x轴负方向移动10步

origin = [0, 0]  # 坐标系统原点
legal_x = [0, 50]  # x轴方向的合法坐标
legal_y = [0, 50]  # y轴方向的合法坐标


def create2(pos=origin, direction=[0, 0], step=1):
    new_x = pos[0] + direction[0] * step
    new_y = pos[1] + direction[1] * step
    pos[0] = new_x
    pos[1] = new_y
    return pos


player = create2(origin, [0, 1], 10)  # 创建棋子player，起点为原点
print(player)
player = create2(origin, [0, 1], 10)
print(player)
player = create2
print(player(origin, [1, 0], 10))
