from collections import OrderedDict

# learnt_words = {'insert':'Insert an item in a certain place of a list.',
#     'append':'Add one more item at the end of a list.',
#     'pop':'Pop out and delete the last item of a list.',
#     'remove':'Remove the indicated item from a list.',
#     'del':'Delete something, like an item of a list.',
#     'sort':'Sort the list.',
#     'sorted':'Sort a lisr.',
#     'lower':'The string\'s lower case.',
#     'len':'Return length of a list.',}

learnt_words = OrderedDict()

learnt_words['insert'] = 'Insert an item in a certain place of a list.'
learnt_words['append'] = 'Add one more item at the end of a list.'
learnt_words['pop'] = 'Pop out and delete the last item of a list.'
learnt_words['remove'] = 'Remove the indicated item from a list.'
learnt_words['del'] = 'Delete something, like an item of a list.'

for key, value in learnt_words.items():
    print(key + ": " + value)
