from Tweening import Tweening
from ETweeningBehaviour import ETweeningBehaviour as ETB
from ETweeningType import ETweeningType as ETT

import matplotlib.pyplot as plt

if __name__ == "__main__":
    initial_value = 0

    goal_value = 1

    number_step = 1000
    
    type_function = ETT.CUBIC
    behaviour = ETB.IN_OUT

    step = (goal_value - initial_value) / number_step

    x_values = []
    y_values = []

    advancement = initial_value
    for i in range(number_step):
        x_values.append(i / number_step)
        y_values.append(Tweening.evaluate(type_function, behaviour, advancement, initial_value, (goal_value - initial_value), 1, None, None))

        advancement += step

    plt.plot(x_values, y_values)
    plt.show()

    
    for j in range(11):
        for k in range(3):
            x_values = []
            y_values = []

            advancement = initial_value
            for i in range(number_step):
                x_values.append(i / number_step)
                y_values.append(Tweening.evaluate(j, k, advancement, initial_value, (goal_value - initial_value), 1, None, None))

                advancement += step

            plt.subplot(11, 3, k + 1 + j * 3)
            plt.plot(x_values, y_values)

    plt.show()