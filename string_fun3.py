from data import story

print(f"total chars in the story: {len(story)}")
words = story.split()
print(f"total word in the story:{len(words)}")
print(f'total unique words in the story:{len(set(words))}')
print(words)

sentence = story.split('.')
print(f"total sentence in the story: {len(sentence)}")
print(sentence)

line = story.split('\n')
print(f"total line in the story: {len(line)}")
print(line)

poem_list = [
    'Twinkle ,twinkle, little star,',
    'How I wonder what you are',
    'Up above the world so sky,',
    'like a diamond in the sky.',
]

poem = "\n".join(poem_list)
print(poem)