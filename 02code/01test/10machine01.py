from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X = iris["data"]
y = iris["target"]

iris.feature_names, iris.target_names

# 훈련/테스트 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
# random_state(결과 고정) = 42 : 매번 똑같이 섞어서 나누고, (42 -> 항상 같은 방식으로 섞음)
# stratify(비율 유지) = 정답 종류 비율은 똑같이 유지(y(라벨)의 분포를 train/test에 동일하게 유지) 
)

# 모델 생성(k=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 예측
pred = knn.predict(X_test)

print("정확도:", accuracy_score(y_test, pred))
print("혼동행렬:\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, target_names=iris.target_names))
