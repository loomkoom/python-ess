# versie 1

# def any_color_in_combination(colors, given):
#     """ Returns true if at least one color in colors is part of the
#     given combination. False otherwise."""
#
#     index = 0
#
#     while index < len(colors):
#         if colors[index] in given:
#             return True
#         else:
#             index += 1
#     return False

# versie 1
# def create_empty_circles(canvas,number_of_circles, max_number_of_moves):
#
#     """ Return a matrix containing grey ovals that are correctly initialized
#         at their required location."""
#
#     x1,y1 = 10,10
#     x2,y2 = 40,40
#     oval = []
#     ovals = []
#
#     while y2 < max_number_of_moves * 41:
#
#         if x2 in range(0, number_of_circles * 40 + 30):
#             oval.append(canvas.create_oval(x1, y1, x2, y2,fill='grey'))
#             x1 += 40
#             x2 += 40
#
#         if x2  >= number_of_circles * 40 + 30:
#             x1 = 10
#             x2 = 40
#             y1 += 40
#             y2 += 40
#
#     for index in range(0, len(oval)):
#         canvas.itemconfig(oval[index], fill='grey')
#
#     for n in range((len(oval)//number_of_circles)):
#         ovals.append(oval[n * (number_of_circles):(n + 1) * (number_of_circles)])
#
#     return ovals



# versie 1
# def all_colors_in_combination(colors, given):
#     """ Returns true if all the colors in colors are part of the
#     given combination. False otherwise."""
#
#     index = 0
#     count = 0
#
#     while index < len(colors):
#         if colors[index] in given:
#             count += 1
#         else:
#             return False
#         index += 1
#
#     if count == len(colors):
#         return True