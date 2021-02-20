# crc16-modbus-in-Python
Cyclic Redundance Check hashing algorithm implemented in python 

A bit brief about CRC

A cyclic redundancy check (CRC) is an error-detecting code commonly used in digital networks and storage devices to detect accidental changes to raw data. Blocks of data entering these systems get a short check value attached, based on the remainder of a polynomial division of their contents. On retrieval, the calculation is repeated and, in the event the check values do not match, corrective action can be taken against data corruption

Usage 

```python
>> from crc import crc16_modbus
>> example_str = 'Cyclic redundat check 16 modbus alogirthm in python'
>> crc16_modbus(example_str)
'396E'
```

All the credits to [kalebu](https://github.com/kalebu)