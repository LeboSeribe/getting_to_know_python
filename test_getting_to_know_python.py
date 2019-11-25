from getting_to_know_python import list_all_js_function_names
#testing to see if it returns function names
def test_function():
    assert list_all_js_function_names('script.js') == [' promptUser', 'Array.prototype.memory_card_shuffle ', ' newBoard', ' memoryFlipCard', ' flip2Back']
