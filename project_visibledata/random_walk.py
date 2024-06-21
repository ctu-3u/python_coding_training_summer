from random import choice


class RandomWalk():

    def __init__(self,num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1,1])
        distance = choice([0,1,2,3,4])
        return direction*distance

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_incre = self.get_step()
            y_incre = self.get_step()
            if x_incre == 0 and y_incre == 0:
                continue
            self.x_values.append(self.x_values[-1] + x_incre)
            self.y_values.append(self.y_values[-1] + y_incre)

    def clear_path(self):
        del self.x_values[1:]
        del self.y_values[1:]