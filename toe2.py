import matplotlib.pyplot as plt

s1_x = -13.45
s2_x = -13.45
s1_y = 15.78
s2_y = -15.78

plt.plot([s1_x, s2_x], [s1_y, s2_y], 'go')
plt.axis([-20, 20, -20, 20])
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
left, width = .50, .5
bottom, height = .10, .5
right = left + width
top = bottom + height
ax.text(right, 0.5 * (bottom + top), 'Re(S)',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)
ax.text(.60, .90, 'Im(S)',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)
plt.grid()
plt.show()