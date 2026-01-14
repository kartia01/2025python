from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = """
우울 우울 우울
자존감문제 자존감문제
학업 학업 학업 학업
스트레스 스트레스
불안
진로
자살
가족관계
"""

font_path = "C:/Windows/Fonts/malgun.ttf"  # 윈도우 기준

wc = WordCloud(
    font_path=font_path,
    background_color="white",
    width=800,
    height=600,
    prefer_horizontal=0.6,   # 세로 단어 허용
    colormap="gray"
).generate(text)

plt.figure(figsize=(8, 6))
plt.imshow(wc)
plt.axis("off")
plt.show()
