# import numpy as np
# age = np.array([65, 9, 41, 3, 17, 58])
# print(age)

# import numpy as np
# age = np.array([[65, 9, 41, 3], [17, 5, 8,11], [25, 32, 1, 96]])
# print(age)

import pandas as pd
age = pd.DataFrame([[65, 9, 41, 3], [17, 5, 8,11], [25, 32, 1, 96]])
age.plot(kind='bar')
