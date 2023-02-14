# JANcode

## What is this

Library to generate barcode called JANcode.  

![jancode](https://raw.githubusercontent.com/yashikota/jancode/master/example.png)

## Features

- Compatible with standard JANcode and short JANcode
- Calculate checkdigit
- Display numbers below the bar JANcode

## Example

```py
import jancode

jancode.generate(4933032010579, "./img")
```

The first argument is the JANcode, and the second argument is the directory where it will be stored.  
The directory to be saved can be omitted.  
