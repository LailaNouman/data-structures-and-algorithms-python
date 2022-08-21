from hash_table.hashtable import HashTable

def test_set_key_value():
    hash1 = HashTable()
    hash1.set('Laila', 22)
    actual = hash1.get('Laila')
    expected = 22
    assert actual == expected

def test_contains_method():
    hash1 = HashTable()
    actual = hash1.contains('l')
    expected = False
    assert actual == expected

def test_return_list_of_keys():
    hash1 = HashTable()
    hash1.set('Laila', 22)
    hash1.set('Nouman', 'Fam')
    hash1.set('Mohammed', 25)
    assert hash1.key() == ['Laila', 'Nouman', 'Mohammed']

def test_handling_collision():
    hash1 = HashTable()
    hash1.set('Laila', 22)
    hash1.set('Nouman', 'Fam')
    assert hash1.get('Nouman') == 'Fam'
    assert hash1.get('Laila') == 22
