# =====================================================
# 📘 PYTHON DATA TYPES - QUICK REVISION NOTES
# =====================================================

# In Python, everything is an object. Data types define
# the kind of values we can store and the operations we
# can perform on them.

# -----------------------------------------------------
# 1. NUMERIC TYPES
# -----------------------------------------------------
# int -> Whole numbers (positive, negative, zero)
# float -> Decimal numbers
# complex -> Numbers with real + imaginary part

x_int = 10                # int
x_float = 3.14            # float
x_complex = 2 + 3j        # complex

print(type(x_int))        # <class 'int'>
print(type(x_float))      # <class 'float'>
print(type(x_complex))    # <class 'complex'>

# -----------------------------------------------------
# 2. SEQUENCE TYPES
# -----------------------------------------------------
# str -> Immutable sequence of characters
# list -> Ordered, mutable collection
# tuple -> Ordered, immutable collection

x_str = "Hello Python"
x_list = [1, 2, 3, "apple", True]
x_tuple = (10, 20, 30)

print(type(x_str))        # <class 'str'>
print(type(x_list))       # <class 'list'>
print(type(x_tuple))      # <class 'tuple'>

# -----------------------------------------------------
# 3. SET TYPES
# -----------------------------------------------------
# set -> Unordered, unique elements, mutable
# frozenset -> Unordered, unique elements, immutable

x_set = {1, 2, 3, 3, 4}   # duplicates removed
x_frozenset = frozenset([10, 20, 20, 30])

print(x_set)              # {1, 2, 3, 4}
print(x_frozenset)        # frozenset({10, 20, 30})

# -----------------------------------------------------
# 4. MAPPING TYPE
# -----------------------------------------------------
# dict -> Key-value pairs (mutable)

x_dict = {
    "name": "Samir",
    "age": 21,
    "is_student": True
}
print(type(x_dict))       # <class 'dict'>

# -----------------------------------------------------
# 5. BOOLEAN TYPE
# -----------------------------------------------------
# bool -> Represents True or False (subclass of int)

x_bool1 = True
x_bool2 = False
print(int(x_bool1))       # 1
print(int(x_bool2))       # 0

# -----------------------------------------------------
# 6. NONE TYPE
# -----------------------------------------------------
# None -> Represents absence of value

x_none = None
print(type(x_none))       # <class 'NoneType'>

# -----------------------------------------------------
# QUICK REFERENCE TABLE
# -----------------------------------------------------
# int       → Whole numbers
# float     → Decimal numbers
# complex   → a + bj numbers
# str       → Immutable text
# list      → Mutable ordered collection
# tuple     → Immutable ordered collection
# set       → Mutable, unique unordered collection
# frozenset → Immutable set
# dict      → Key-value pairs
# bool      → True / False
# NoneType  → Represents "no value"
# -----------------------------------------------------

# ✅ TIP:
# Use type() to check data type of any variable.
# Use isinstance(var, datatype) for type checking.
