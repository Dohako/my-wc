# My WC cli tool

## Description
This is a simple cli tool that can be used to count the number of words, lines and characters in a file.

## Usage
```bash
python my_wc.py <file>
```

## Example

### Bytes count
```bash
python my_wc.py test.txt

python my_wc.py -c test.txt
```

### Lines count
```bash
python my_wc.py -l test.txt
```

### Words count
```bash
python my_wc.py -w test.txt
```

### Characters count
```bash
python my_wc.py -m test.txt
```
#### Note
This metric depends on locale and result can differ depending on locale that is set.
