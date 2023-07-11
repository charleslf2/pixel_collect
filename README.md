## pixel collect

Pixel collect is a simple google image scrapper for your computer vision tasks

### Installation

#### Quick 

```bash
pip install pixel_collect
```

#### Long

- Step 1

```bash
git clone https://github.com/charleslf2/pixel_collect
```

- Step 2

```bash
cd pixel_collect
```

- Step 3

```bash
py setup.py install
```

### Usage

```python

>>> from pixel_collect import pixel_scrap

>>> pixel_scrap(keyword="cats photos",save_folder="cats",limit=50,logs=True)
```

