"""
A simple cross-platform Python 3 plotting library.

Usage:
  import simpleplot as plt

  plt.add_line(points)
  plt.add_line(points, label)
    Add a line through the given points to the plot,
      where points is a collection of tuples (x, y).
    The points will be sorted by x-value before plotting.
    The label is optional.

  plt.plot_title("title")
    (optional) Set the title of the plot.
    Default is "Plot".

  plt.show_plot()
    Shows the current plot.
    This blocks execution until the plot window is closed.
    After showing the plot, the plot window is reset.

You can zoom into a region by dragging, and return to the previous view by right-clicking.

Author: Koen Yskout
Date: February 2017

"""

from tkinter import *
from tkinter import font
import math

DEFAULT_TITLE = "Plot"
DEFAULT_X_LABEL = "n"
DEFAULT_Y_LABEL = "T (sec)"

DEFAULT_WINDOW_WIDTH = 800
DEFAULT_WINDOW_HEIGHT = 600

ENABLE_PREDICTION_BUTTON = False

class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color
        self.__vis = None

    def get_bounds(self):
        return Bounds(self.x, self.x, self.y, self.y)

    def __str__(self):
        return "(%.f,%.f)" % (self.x, self.y)

    def draw(self, context, canvas):
        x, y = context.p2s(self.x, self.y)
        self.__vis = canvas.create_oval(x - 1, y - 1, x + 1, y + 1, outline=self.color, fill=self.color)

    def clear(self, context, canvas):
        if self.__vis is not None:
            canvas.delete(self.__vis)
            self.__vis = None


class Line:
    def __init__(self, points, color="red", label=None):
        self.points = sorted(points, key=lambda p: (p.x, p.y))
        self.color = color
        self.label = label
        self.bounds = Bounds()
        self.__font = font.Font(family='sans-serif', size=12)
        self.__last_highlight = None
        self.__last_highlight_text = None
        self.show_predictions = False
        for b in self.points:
            self.bounds.extend(b.get_bounds())
        self.__lsq_fit = self.__calculate_fit()

    def __calculate_fit(self):
        mean_prod = 0
        mean_x = 0
        mean_y = 0
        mean_x2 = 0
        n_predict = (7 * len(self.points)) // 10
        for i in range(n_predict):
            p = self.points[i]
            mean_prod += p.x * p.y
            mean_x += p.x
            mean_y += p.y
            mean_x2 += p.x * p.x
        mean_prod /= n_predict
        mean_x /= n_predict
        mean_y /= n_predict
        mean_x2 /= n_predict

        beta = (mean_prod - mean_x * mean_y) / (mean_x2 - mean_x * mean_x)
        alpha = mean_y - beta * mean_x

        return [Point(p.x, alpha + beta * p.x) for p in (self.points[0], self.points[n_predict-1], self.points[-1])]

    def toggle_prediction(self):
        self.show_predictions = not self.show_predictions

    def get_bounds(self):
        return self.bounds

    def draw(self, context, canvas):

        if self.show_predictions:
            lsq_x0 = self.__lsq_fit[0].x
            lsq_y0 = self.__lsq_fit[0].y
            lsq_x1 = self.__lsq_fit[1].x
            lsq_y1 = self.__lsq_fit[1].y
            lsq_x2 = self.__lsq_fit[2].x
            lsq_y2 = self.__lsq_fit[2].y
            canvas.create_line(context.p2s(lsq_x0, lsq_y0), context.p2s(lsq_x1, lsq_y1), fill=self.color, dash=(4, 2))
            canvas.create_line(context.p2s(lsq_x1, lsq_y1), context.p2s(lsq_x2, lsq_y2), fill=self.color, dash=(4, 8))

        prev_point = None
        for point in self.points:
            if prev_point is not None:
                x0, y0 = context.p2s(prev_point.x, prev_point.y)
                x1, y1 = context.p2s(point.x, point.y)
                canvas.create_line(x0, y0, x1, y1, fill=self.color)
            prev_point = point
            point.draw(context, canvas)
        if self.label is not None and prev_point is not None:
            w = self.__font.measure(self.label)
            canvas.create_rectangle(context.p2s_x(prev_point.x)+2, context.p2s_y(prev_point.y)-10,
                               context.p2s_x(prev_point.x)+6+w, context.p2s_y(prev_point.y) + 10,
                               fill=self.color, outline=self.color)

            canvas.create_text(context.p2s_x(prev_point.x)+4, context.p2s_y(prev_point.y), anchor=W, text=self.label,
                               fill="white", font=self.__font)

    def __find_index_by_x(self, x):
        # pre: self.points is sorted by x
        start = 0
        end = len(self.points) - 1

        # INV: points[start].x <= x <= points[end].x
        while start < end:
            mid = (start + end) // 2
            if self.points[mid].x < x:
                start = mid + 1
                if self.points[start].x > x:
                    return mid
            elif self.points[mid].x > x:
                end = mid
            else:
                return mid
        return start

    def update_highlight(self, context, canvas, x, y):
        plot_x = context.s2p_x(x)
        i = self.__find_index_by_x(plot_x)
        if i >= len(self.points) - 1 or plot_x < self.bounds.min_x or plot_x > self.bounds.max_x:
            self.clear_highlight(context, canvas)
            return
        p0 = self.points[i]
        p1 = self.points[i + 1]

        alpha = (plot_x - p0.x) / (p1.x - p0.x)
        x_interp = (1 - alpha) * p0.x + alpha * p1.x
        y_interp = (1 - alpha) * p0.y + alpha * p1.y
        newx, newy = context.p2s(x_interp, y_interp)

        text_str = "%s: %s" % (self.label, _pretty_format(y_interp))
        f = font.Font(family='sans-serif', size=12)
        str_width = f.measure(text_str)

        if self.__last_highlight is not None:
            canvas.coords(self.__last_highlight[0], newx - 4, newy - 4, newx + 4, newy + 4)
            canvas.coords(self.__last_highlight[1], newx + 2, newy - 25, newx + 8 + str_width, newy - 2)
            canvas.coords(self.__last_highlight[2], newx + 5, newy - 5)
            canvas.itemconfig(self.__last_highlight[2], text=text_str, anchor=SW)
        else:
            box = canvas.create_rectangle(x + 2, newy - 25, x + 8 + str_width,
                                          newy - 2,
                                          outline=self.color, fill="white")
            text = canvas.create_text(x + 5, newy - 5,
                                      text=text_str,
                                      fill=self.color, anchor=SW,
                                      font=f)
            dot = canvas.create_oval(x - 4, y - 4, x + 4, y + 4, outline=self.color, fill=self.color)
            self.__last_highlight = [dot, box, text]

    def clear_highlight(self, context, canvas):
        if self.__last_highlight is not None:
            for obj in self.__last_highlight:
                canvas.delete(obj)
            self.__last_highlight = None

    def __str__(self):
        return "Line %s .. %s [%d points]" % (self.points[0], self.points[-1], len(self.points))


class Bounds:
    def __init__(self, min_x=None, max_x=None, min_y=None, max_y=None):
        if min_x and max_x and min_x > max_x:
            min_x, max_x = max_x, min_x
        if min_y and max_y and min_y > max_y:
            min_y, max_y = max_y, min_y
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def set(self, x1, y1, x2, y2):
        self.min_x = min(x1, x2)
        self.max_x = max(x1, x2)
        self.min_y = min(y1, y2)
        self.max_y = max(y1, y2)

    def values(self):
        return self.min_x, self.min_y, self.max_x, self.max_y

    def extend(self, other):
        if other is None:
            return
        self.min_x = Bounds.__compare(self.min_x, other.min_x, min)
        self.min_y = Bounds.__compare(self.min_y, other.min_y, min)
        self.max_x = Bounds.__compare(self.max_x, other.max_x, max)
        self.max_y = Bounds.__compare(self.max_y, other.max_y, max)

    @staticmethod
    def __compare(first, second, function):
        if first is None:
            return second
        if second is None:
            return first
        return function(first, second)

    def width(self):
        if self.max_x is None or self.min_x is None:
            return 0
        return self.max_x - self.min_x

    def height(self):
        if self.max_y is None or self.min_y is None:
            return 0
        return self.max_y - self.min_y

    def is_empty(self):
        return self.min_x == self.max_x and self.min_y == self.max_y

    def __str__(self):
        return "(%.f,%.f)-(%.f,%.f)" % (self.min_x, self.min_y, self.max_x, self.max_y)


def _nice_number(target_range, rounding):
    # Reference: Paul Heckbert, "Nice Numbers for Graph Labels", Graphics Gems, 1990, pp 61-63.
    exponent = math.floor(math.log10(target_range))
    fraction = target_range / 10 ** exponent
    if rounding:
        if fraction < 1.5:
            nice_fraction = 1
        elif fraction < 3:
            nice_fraction = 2
        elif fraction < 7:
            nice_fraction = 5
        else:
            nice_fraction = 10
    else:
        if fraction <= 1:
            nice_fraction = 1
        elif fraction <= 2:
            nice_fraction = 2
        elif fraction <= 5:
            nice_fraction = 5
        else:
            nice_fraction = 10

    return nice_fraction * 10 ** exponent


class AxisX:
    def __init__(self):
        self.__vis = None
        self.__ticks = []
        self.__highlight = None
        self.label = DEFAULT_X_LABEL
        self.__font = font.Font(family='sans-serif', size=12)

    def get_bounds(self):
        return Bounds(0, 0, 0, 0)

    def draw(self, context, canvas):
        if self.__vis is not None:
            canvas.delete(self.__vis)

        xmin = context.plot_extent.min_x
        xmax = context.plot_extent.max_x

        nticks = max(2, context.plot_width() // 75)
        xrange = _nice_number(xmax - xmin, False)
        xunit = _nice_number(xrange / nticks, True)

        xtick = 0
        while xtick <= xmax:
            x = context.p2s_x(xtick)
            y = context.p2s_y(0)
            self.__ticks.append(canvas.create_line(x, y - 3, x, y + 3, fill="black"))
            self.__ticks.append(
                canvas.create_text(x, y + 2, text=_pretty_format(xtick), fill="black", anchor=N, font=self.__font))
            xtick += xunit
        self.__vis = [
            canvas.create_line(context.p2s(xmin, 0), context.p2s(xmax, 0), fill="black"),
            canvas.create_text(context.p2s_x(xmax), context.p2s_y(0) + 20, text=self.label, anchor=NE, font=self.__font)
        ]

    def update_highlight(self, context, canvas, x, y):
        if x < context.margin_left() or x > context.margin_left() + context.plot_width():
            self.clear_highlight(context, canvas)
            return
        text = _pretty_format(context.s2p_x(x))
        str_width = self.__font.measure(text)

        y = context.p2s_y(0)
        if self.__highlight is None:
            box = canvas.create_rectangle(x, y, x + str_width + 6, y + 20, fill="black", outline="black")
            circle = canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline="black")
            text = canvas.create_text(x + 3, y, text=text, fill="white", anchor=NW, font=self.__font)
            self.__highlight = [text, box, circle]
        else:
            canvas.itemconfig(self.__highlight[0], text=text)
            canvas.coords(self.__highlight[0], x + 3, y + 3)
            canvas.coords(self.__highlight[1], x, y, x + str_width + 6, y + 20)
            canvas.coords(self.__highlight[2], x - 4, y - 4, x + 4, y + 4)

    def clear_highlight(self, context, canvas):
        if self.__highlight is not None:
            for obj in self.__highlight:
                canvas.delete(obj)
            self.__highlight = None


class AxisY:
    def __init__(self):
        self.__vis = None
        self.__ticks = []
        self.__highlight = None
        self.label = DEFAULT_Y_LABEL
        self.__font = font.Font(family='sans-serif', size=12)

    def get_bounds(self):
        return Bounds(0, 0, 0, 0)

    def draw(self, context, canvas):
        if self.__vis is not None:
            canvas.delete(self.__vis)

        ymin = context.plot_extent.min_y
        ymax = context.plot_extent.max_y

        nticks = max(2, context.plot_height() // 50)
        yrange = _nice_number(ymax - ymin, False)
        yunit = _nice_number(yrange / nticks, True)

        ytick = 0
        while ytick <= ymax:
            x = context.p2s_x(0)
            y = context.p2s_y(ytick)
            self.__ticks.append(canvas.create_line(x - 3, y, x + 3, y, fill="black"))
            self.__ticks.append(
                canvas.create_text(x - 3, y, text=_pretty_format(ytick), fill="black", anchor=E, font=self.__font))
            ytick += yunit
        self.__vis = [
            canvas.create_line(context.p2s(0, ymin), context.p2s(0, ymax), fill="black"),
            canvas.create_text(context.p2s_x(0) - 5, context.p2s_y(ymax) - 5, text=self.label, anchor=SE, font=self.__font)
        ]

    def update_highlight(self, context, canvas, x, y):
        if y < context.margin_top() or y > context.margin_top() + context.plot_height():
            self.clear_highlight(context, canvas)
            return

        text = _pretty_format(context.s2p_y(y))
        str_width = self.__font.measure(text)

        x = context.p2s_x(0)
        if self.__highlight is None:
            box = canvas.create_rectangle(x - str_width - 6, y, x, y + 20, fill="black", outline="black")
            circle = canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", outline="black")
            text = canvas.create_text(x - 3, y, text=text, fill="white", anchor=NE, font=self.__font)
            self.__highlight = [text, box, circle]
        else:
            canvas.itemconfig(self.__highlight[0], text=text)
            canvas.coords(self.__highlight[0], x - 3, y)
            canvas.coords(self.__highlight[1], x - str_width - 6, y, x, y + 20, )
            canvas.coords(self.__highlight[2], x - 4, y - 4, x + 4, y + 4)

    def clear_highlight(self, context, canvas):
        if self.__highlight is not None:
            for obj in self.__highlight:
                canvas.delete(obj)
            self.__highlight = None


class CrossHair:
    def __init__(self):
        self.__vertical = None
        self.__horizontal = None

    def get_bounds(self):
        return Bounds(0, 0, 0, 0)

    def draw(self, context, canvas):
        pass

    def update_highlight(self, context, canvas, x, y):

        if x < context.margin_left() or x > context.margin_left() + context.plot_width():
            canvas.delete(self.__vertical)
            self.__vertical = None
        elif self.__vertical is None:
            self.__vertical = canvas.create_line(
                x,
                context.margin_top(),
                x,
                context.margin_top() + context.plot_height(), fill="gray")
        else:
            canvas.coords(self.__vertical, x, context.margin_top(), x, context.margin_top() + context.plot_height())

        if y < context.margin_top() or y > context.margin_top() + context.plot_height():
            canvas.delete(self.__horizontal)
            self.__horizontal = None
        elif self.__horizontal is None:
            self.__horizontal = canvas.create_line(
                context.margin_left(), y,
                context.margin_left() + context.plot_width(), y, fill="gray")
        else:
            canvas.coords(self.__horizontal, context.margin_left(), y,
                          context.margin_left() + context.plot_width(), y)

    def clear_highlight(self, context, canvas):
        if self.__vertical is not None:
            canvas.delete(self.__vertical)
            self.__vertical = None
        if self.__horizontal is not None:
            canvas.delete(self.__horizontal)
            self.__horizontal = None


class Context:
    def __init__(self, plot_size, extent, margins):
        self.margins = margins
        self.plot_extent = extent  # units
        self.plot_size = None  # pixels
        self.resize(plot_size)

    def margin_top(self):
        return self.margins[0]

    def margin_right(self):
        return self.margins[1]

    def margin_bottom(self):
        return self.margins[2]

    def margin_left(self):
        return self.margins[3]

    def resize(self, plot_size):
        self.plot_size = (plot_size[0] - self.margin_left() - self.margin_right(),
                          plot_size[1] - self.margin_top() - self.margin_bottom())

    def plot_width(self):
        """Width of the plot area (in pixels)"""
        return self.plot_size[0]

    def plot_height(self):
        """Height of the plot area (in pixels)"""
        return self.plot_size[1]

    def __scale_x(self):
        try:
            return self.plot_width() / self.plot_extent.width()  # pixels / unit
        except ZeroDivisionError:
            return 1

    def __scale_y(self):
        try:
            return self.plot_height() / self.plot_extent.height()
        except ZeroDivisionError:
            return 1

    def p2s(self, x, y):
        return self.p2s_x(x), self.p2s_y(y)

    def p2s_bounds(self, bounds):
        if self.plot_extent.is_empty():
            return self.margin_left(), self.margin_top(), self.margin_left() + self.plot_width(), self.margin_top() + self.plot_height()
        return self.p2s_x(bounds.min_x), self.p2s_y(bounds.min_y), self.p2s_x(bounds.max_x), self.p2s_y(bounds.max_y)

    def p2s_x(self, x):
        return self.margin_left() + (x - self.plot_extent.min_x) * self.__scale_x()

    def p2s_y(self, y):
        return self.margin_top() + self.plot_height() - (y - self.plot_extent.min_y) * self.__scale_y()

    def s2p(self, x, y):
        return self.s2p_x(x), self.s2p_y(y)

    def s2p_x(self, x):
        return (x - self.margin_left()) / self.__scale_x() + self.plot_extent.min_x

    def s2p_y(self, y):
        return - (y - self.margin_top() - self.plot_height()) / self.__scale_y() + self.plot_extent.min_y


class Plot:
    def __init__(self):
        self.__objects = []
        self.__enable_prediction = False

        self.__bounds = Bounds(0, None, 0, 1e-3)
        self.context = Context(plot_size=(DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT),
                               extent=self.__bounds,
                               margins=(30, 50, 50, 80))

        self.__root = Tk()
        self.__canvas = Canvas(self.__root, width=self.context.plot_width(), height=self.context.plot_height())
        self.__canvas.config(background="white")
        self.__canvas.bind("<Configure>", self.__update)
        self.__canvas.bind("<Motion>", self.__on_motion)
        self.__canvas.bind("<B1-Motion>", self.__on_drag)
        self.__canvas.bind("<ButtonRelease-1>", self.__on_drag_end)
        self.__canvas.bind("<Button-2>", self.__unzoom)
        self.__drag_start = None
        self.__zoomhistory = []
        self.__canvas.pack(fill="both", expand=1)

        if ENABLE_PREDICTION_BUTTON:
            self.__show_prediction = Button(self.__root, text="Show/hide linear fit and extrapolation")
            self.__show_prediction.bind("<Button-1>", self.__toggle_predictions)
            self.__show_prediction.pack()

        self.color_index = 0
        self.colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf"]

        self.set_title(DEFAULT_TITLE)
        self.add_crosshair()
        self.add_x_axis()
        self.add_y_axis()

    def __on_drag(self, event=None):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        if self.__drag_start is None:
            rect = canvas.create_rectangle(x, y, x, y, fill="#b0c4de", outline="#b0c4de")
            canvas.tag_lower(rect)
            self.__drag_start = [(x, y), rect]
        else:
            canvas.coords(self.__drag_start[1], *self.__drag_start[0], x, y)

        self.__update_highlight(x, y)

    def __on_drag_end(self, event=None):
        if self.__drag_start is not None:
            canvas = event.widget
            x = canvas.canvasx(event.x)
            y = canvas.canvasy(event.y)
            event.widget.delete(self.__drag_start[1])
            self.__zoom(*self.__drag_start[0], x, y)
            self.__drag_start = None

    def __zoom(self, x1, y1, x2, y2):
        self.__zoomhistory.append(self.context.plot_extent.values())
        self.context.plot_extent.set(*self.context.s2p(x1, y1), *self.context.s2p(x2, y2))
        self.__update()

    def __unzoom(self, event=None):
        if self.__zoomhistory:
            last = self.__zoomhistory.pop()
            self.context.plot_extent.set(*last)
            self.__update()

    def __toggle_predictions(self, event=None):
        for obj in self.__objects:
            if isinstance(obj, Line):
                obj.toggle_prediction()
        self.__update()

    def set_title(self, title):
        if title is None:
            title = DEFAULT_TITLE
        self.__root.title(title)

    def __update(self, event=None):
        self.__clear_highlight()
        self.__canvas.delete(ALL)
        size = (self.__canvas.winfo_width(), self.__canvas.winfo_height())
        self.context.resize(size)
        self.__draw()

    def __on_motion(self, event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        self.__update_highlight(x, y)

    def __clear_highlight(self):
        for obj in self.__objects:
            obj.clear_highlight(self.context, self.__canvas)

    def __update_highlight(self, x, y):
        for obj in self.__objects:
            obj.update_highlight(self.context, self.__canvas, x, y)

    def show(self):
        if self.__bounds.is_empty():
            self.__bounds.extend(Bounds(0, 1, 0, 1))
        self.__draw()
        self.__root.mainloop()

    def __draw(self):
        self.__canvas.create_rectangle(self.context.p2s_bounds(self.__bounds), outline="#eeeeee")

        for obj in self.__objects:
            obj.draw(self.context, self.__canvas)
        self.__root.update_idletasks()

    def next_color(self):
        color = self.colors[self.color_index]
        self.color_index += 1
        if self.color_index >= len(self.colors):
            self.color_index = 0
        return color

    def add_crosshair(self):
        ch = CrossHair()
        self.__add_object(ch)

    def add_x_axis(self):
        axis = AxisX()
        self.__add_object(axis)

    def add_y_axis(self):
        axis = AxisY()
        self.__add_object(axis)

    def add_line(self, points, color=None, label=None):
        if color is None:
            color = self.next_color()
        if label is None:
            nb_lines = sum(isinstance(o, Line) for o in self.__objects)
            label = "Line " + str(nb_lines + 1)
        points = (Point(p[0], p[1], color=color) for p in points)
        line = Line(points, color=color, label=label)
        self.__add_object(line)

    def __add_object(self, object):
        self.__objects.append(object)
        self.__bounds.extend(object.get_bounds())

    def clear(self):
        self.__clear_highlight()
        self.__canvas.delete(ALL)
        self.__objects.clear()


def _pretty_format(number):
    if isinstance(number, int) or round(number) == number:
        return "%d" % number
    elif -1000000 < number < -0.1 or 0.1 < number < 1000000:
        return "%.2f" % number
    else:
        return "%.2e" % number


__current_plot = None


def _current_plot():
    global __current_plot
    if __current_plot is None:
        __current_plot = Plot()
    return __current_plot


def _clear_plot():
    global __current_plot
    __current_plot = Plot()


def plot_title(title):
    _current_plot().set_title(title)


def add_line(points, label=None, color=None):
    _current_plot().add_line(points, color, label)


def show_plot():
    _current_plot().show()
    _clear_plot()


if __name__ == "__main__":
    plot_title("Example plot")

    import random

    add_line([(x, 3 + 3 * math.sin(2 * x * math.pi / 10)) for x in range(20)])
    add_line([(x, 6 + 2 * x + random.normalvariate(0, 2)) for x in range(20)])
    add_line([(x, .2 + .5 * x * x + random.normalvariate(0, x/3)) for x in range(20)])

    add_line([(x, .2 + .5 * x * math.log(x+0.1) + 2*random.normalvariate(0, .5)) for x in range(20)])

    show_plot()
