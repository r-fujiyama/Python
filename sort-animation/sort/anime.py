import matplotlib.pyplot as plt


class SortAnimation:

    def __init__(self, rand_List):
        self.rand_List = rand_List

    def bubblesort(self):
        self.fig = plt.figure()
        self.fig.canvas.manager.window.after(50, self._draw_bubblesort)
        plt.show()

    def _draw_bubblesort(self):
        rects = plt.bar(range(len(self.rand_List)), self.rand_List, 1)
        for i in range(len(self.rand_List)-1):
            for j in range(len(self.rand_List)-1, i, -1):
                if(self.rand_List[j-1] > self.rand_List[j]):
                    t = self.rand_List[j]
                    self.rand_List[j] = self.rand_List[j-1]
                    self.rand_List[j-1] = t
                    self.fig.canvas.draw()
                for rect, h in zip(rects, self.rand_List):
                    rect.set_height(h)
        self.fig.canvas.draw()
