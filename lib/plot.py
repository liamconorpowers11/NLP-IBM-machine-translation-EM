from matplotlib import pyplot as plt

# class data:pass
# model_data = {1:dict(), 2:dict()}

# model_data[1]["precision"] = [0, 0.202, 0.379, 0.406, 0.41, 0.416]
# model_data[1]["recall"] = [0, 0.209, 0.391, 0.419, 0.423, 0.43]
# model_data[1]["f1-score"] = [0, 0.205, 0.385, 0.413, 0.417, 0.423]

# model_data[2]["precision"] = [0.416, 0.433, 0.438, 0.441, 0.441, 0.443]
# model_data[2]["recall"] = [0.43, 0.447, 0.453, 0.455, 0.455, 0.458]
# model_data[2]["f1-score"] = [0.423, 0.44, 0.445, 0.448, 0.448, 0.45]


# for m in [1,2]:
#     plt.ioff()

#     iterations = range(len(model_data[m]["f1-score"]))

#     plt.figure()
#     plt.ylabel('Accuracy Score')
#     plt.xlabel('Number of Iterations')
#     plt.title('Accuracy Measures vs EM Iterations')

#     colors = ['m-','r-','b-']

#     for i,(aType,scores) in enumerate(model_data[m].items()):
#         plt.plot(iterations, scores, colors[i], label=aType)

#     plt.legend(loc='upper right')
#     plt.show()

models={}
models[1] = [0.000, 0.205, 0.385, 0.413,  0.417, 0.423, 0.425,  0.428, 0.431, 0.431, 0.431]
models[2] = [0.000, 0.205, 0.349, 0.387, 0.408, 0.422, 0.426, 0.432, 0.435, 0.438, 0.439]
plt.ioff()

iterations = range(len(models[1]))

plt.figure()
plt.ylabel('F1 Score')
plt.xlabel('Number of Iterations')
plt.title('F1 Score vs EM Iterations')

colors = ['m-','r-','b-']

for i,(m,scores) in enumerate(models.items()):
    plt.plot(iterations, scores, colors[i], label=f"IBM Model {m}")

plt.legend(loc='lower right')
plt.show()