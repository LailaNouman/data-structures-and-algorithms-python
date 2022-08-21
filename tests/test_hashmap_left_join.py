from hashmap_left_join.hashmap_left_join import HashTable, left_join

hash_table1 = HashTable()
hash_table1.set("diligent", "employed")
hash_table1.set("fond", "enamored")
hash_table1.set("guide", "usher")
hash_table1.set("outfit", "garb")
hash_table1.set("wrath", "anger")
hash_table2 = HashTable()
hash_table2.set("diligent", "idle")
hash_table2.set("fond", "averse")
hash_table2.set("guide", "follow")
hash_table2.set("flow", "jam")
hash_table2.set("wrath", "delight")

def test_left_join():
    actual = left_join(hash_table1, hash_table2)
    expected = [['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'garb', 'NULL'], ['wrath', 'anger', 'delight']]
    assert actual == expected

def test_type_left_join():
    actual = type(left_join(hash_table1, hash_table2))
    expected = type([])
    assert actual == expected