from getting_to_know_python import list_all_js_function_names
#testing to see if it returns function names
def test_function():
    assert list_all_js_function_names('script.js') == [{'name': ' promptUser', 'starting line': 7, 'end_line': 13}, {'name': 'Array.prototype.memory_card_shuffle ', 'starting line': 15, 'end_line': 23}, {'name': ' newBoard', 'starting line': 25, 'end_line': 35}, {'name': ' flip2Back', 'starting line': 64, 'end_line': 80}]
