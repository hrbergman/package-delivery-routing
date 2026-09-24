# *********************
# Name: Hannah Bergman
# ID: 001539744
# *********************

# ********************************************************************************************************
# Referenced Webinar 1, "Let's Go Hashing" by Course Instructor, Dr. Cemel Tepe, to create this hash table
# Full citation is included in attached report
# ********************************************************************************************************

# Space complexity is proportional to input size: O(n)
class HashTable(object):
    def __init__(self, size=10):
        self._struct = self.struct_creation(size)

    # The key is hashed using the insert() function, followed by finding the modular value
    # After it uses the modular function to locate a bucket for appending
    # Time complexity is proportional to the size of the bucket, denoted as n, resulting in: O(n)
    def insert(self, key, value):
        hashed_key = hash(key)
        bucket = self.find_bucket(hashed_key)

        mod = self.look_up_key_value_pair(hashed_key, bucket)

        if len(mod) == 0:
            bucket.append([hashed_key, value])
        else:
            mod[1] = value
        return True

    # The function remove() finds a key within the bucket and removes it
    # Time complexity is constant: O(1)
    def remove(self, key):
        bucket = self.find_bucket(key)
        if key in bucket:
            bucket.remove(key)

    # Executing struck_creation() will loop through the hash table and establish buckets for future use
    # Time complexity is linear: O(n)
    def struct_creation(self, size):
        struct = []
        for i in range(size):
            struct.append([])

        return struct

    # The find() function uses a key to perform a hash operation to find its matching bucket
    # It then loops through the bucket to look up the key-value pair
    # Time complexity is proportional to the size of the bucket, denoted as n, resulting in: O(n)
    def look_up(self, key):
        hashed_key = hash(key)
        bucket = self.find_bucket(hashed_key)

        key_value_pair = self.look_up_key_value_pair(hashed_key, bucket)

        if key_value_pair:
            return key_value_pair[1]

        raise Exception("Key-Value pair does not exist")

    # The find_key_value_pair() function loops through the bucket to find the required key-value pair
    # Time complexity is linear: O(n)
    def look_up_key_value_pair(self, key, bucket):
        for keey_value_pair in bucket:
            if keey_value_pair[0] == key:
                return keey_value_pair
        return []

    # The find_bucket() function uses hashed key to find the required bucket
    # Time complexity is constant: O(1)
    def find_bucket(self, key):
        return self._struct[key % len(self._struct)]

