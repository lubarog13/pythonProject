import matplotlib.pyplot as plt

s1_x = -7.7
s2_x = -7.7
s1_y = 14.32
s2_y = -14.32

plt.plot([s1_x, s2_x], [s1_y, s2_y], 'go')
plt.axis([-10, 10, -20, 20])
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