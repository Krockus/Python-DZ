# ������ ������� ���������� ���������

#������ 1

class triangle:
    max_dist = 1000  # �������� ������ ��������� ����������� �� �������� ������ 1000

    @classmethod
    def check_length(self, sx1, sy1, sx2, sy2):
        return (((sx1 - sx2)**2 + (sy1 - sy2)**2)**0.5) <= 1000

    @classmethod
    def self_checking(self, xt1, yt1, xt2, yt2, xt3, yt3):
        if not self.check_length(xt1, yt1, xt2, yt2):
            return False
        if not self.check_length(xt1, yt1, xt3, yt3):
            return False
        if not self.check_length(xt2, yt2, xt3, yt3):
            return False

        return True

    def __init__(self,x1 = 0,y1 = 0,x2 = 0,y2 = 0,x3 = 0,y3 = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

        if not self.self_checking( x1, y1, x2, y2, x3, y3):
            #raise Exception('������� ������� 1000, �� ���� �������')
            print('������� ������� �������')
            exit(1)

    def get_square(self):
        # � ���������� ��������� � ��� ������ ������������� ������������,
        # ���� 90 �������� � ����� x1 y1

        side_one_length = ((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**0.5
        side_two_length = ((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2) ** 0.5

        return side_one_length * side_two_length / 2

    def get_perimeter(self):
        side_one_length = ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5
        side_two_length = ((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2) ** 0.5
        side_three_length = ((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5

        return side_one_length + side_two_length + side_three_length

    def draw_self(self):
        print('������ ����� ��', self.x1, ':', self.y1, '��', self.x2, ':', self.y2)
        print('������ ����� ��', self.x2, ':', self.y2, '��', self.x3, ':', self.y3)
        print('������ ����� ��', self.x3, ':', self.y3, '��', self.x1, ':', self.y1)

tr = triangle(0,0,10,0,0,10)

print('�������',tr.get_square())
print('��������',tr.get_perimeter())
tr.draw_self()