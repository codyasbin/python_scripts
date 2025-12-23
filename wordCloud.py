from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Let's use a sample text. You can replace this with any text you like!
text = """Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented, and functional programming. Python is often described as a 'batteries included' language due to its comprehensive standard library. Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0 was released in 2000 and introduced features like list comprehensions, garbage collection system, and augmented assignment. Python 3.0 was released in 2008 and was a major revision of the language that is not entirely backward-compatible. Python 2 code often does not run on Python 3 interpreters without modification. The language is widely used in artificial intelligence, machine learning, web development, data analysis, automation, and more. It has a vast ecosystem of libraries and frameworks.
"""

# Generate a word cloud image
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = set(['a', 'an', 'the', 'is', 'it', 'its', 'of', 'and', 'to', 'in', 'was', 'with', 'by', 'for', 'on', 'from', 'as', 'has', 'its', 'not', 'that', 'but', 'or', 'such', 'this', 'have', 'are', 'which', 'many', 'more', 'also', 'be', 'been', 'at', 'can', 'will', 'if', 'what', 'so', 'had', 'all', 'into', 'out', 'up', 'down', 'only', 'very', 'than', 'after', 'before', 'where', 'when', 'who', 'how', 'about', 'here', 'there', 'he', 'she', 'it', 'we', 'they', 'you', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'our', 'their', 'we', 'us', 'them', 'my', 'your', 'his', 'her', 'our', 'their', 'this', 'that', 'these', 'those', 'any', 'some', 'no', 'few', 'much', 'many', 'most', 'each', 'every', 'other', 'another', 'own', 'same', 'such', 'so', 'too', 'very', 'just', 'now', 'then', 'here', 'there', 'when', 'where', 'why', 'how', 'whether', 'while', 'because', 'although', 'though', 'even', 'once', 'since', 'until', 'unless', 'before', 'after', 'if', 'than', 'then', 'as', 'like', 'through', 'above', 'below', 'between', 'among', 'across', 'behind', 'beside', 'next', 'near', 'over', 'under', 'throughout', 'without', 'within', 'around', 'about', 'along', 'towards', 'onto', 'upon', 'from', 'into', 'with', 'without', 'during', 'during', 'since', 'for', 'through', 'ago', 'until', 'till', 'before', 'after', 'at', 'on', 'in']), # Common English stopwords
                min_font_size = 10).generate(text)

# Display the generated image:
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()