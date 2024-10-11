import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

def plot_wordcloud(data, column):
    all_words = ' '.join(data[column])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Most Common Words in ' + column)
    plt.show()

def sentiment_distribution(df, x):
    plt.figure(figsize=(10,6))
    sns.countplot(x=x, data=df)
    plt.title("Sentiment Distribution")
    plt.show()

def plot_branch_sentiment(data, x_col, hue_col):
    sns.countplot(x=x_col, hue=hue_col, data=data)
    plt.title(f'{x_col.capitalize()}-wise Sentiment Analysis')
    plt.xticks(rotation=85)
    plt.show()