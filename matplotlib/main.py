# Build histogram with 5 bins
import matplotlib.pyplot as plt

plt.hist(life_exp, 5)


# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, 20)

# Show and clean up again
plt.show()
plt.clf()