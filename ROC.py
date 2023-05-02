from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np

# true labels (ground truth) for each class
y_true = np.array([0, 0, 1, 2, 0, 1])

# predicted scores for each class
y_score = np.array([[0.4, 0.3, 0.2],
                    [0.8, 0.02, 0.10],
                    [0.7, 0.05, 0.1],
                    [0.7, 0.13, 0.14],
                    [0.6, 0.07, 0.3],
                    [0.9, 0.01, 0.03]])

# compute ROC curve for each class separately
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(y_score.shape[1]):
    fpr[i], tpr[i], _ = roc_curve(y_true == i, y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# plot ROC curve for each class separately
plt.figure(figsize=(8, 5))
colors = ['blue', 'red', 'green']
for i, color in zip(range(y_score.shape[1]), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([-0.05, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve for multiclass classification (one-vs-rest)')
plt.legend(loc="lower right")
plt.show()
