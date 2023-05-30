# XL-LEXEME
WiC Pretrained Model for Cross-Lingual LEXical sEMantic changE

Install the libaries:
```
pip install -U sentence-transformers
```

Load the model (the model is available in the Hugging Face Model Hub https://huggingface.co/pierluigic/xl-lexeme):
```python
from WordTransformer import WordTransformer

model = WordTransformer('pierluigic/xl-lexeme')
```

Usage:
```python
from InputExample import InputExample

examples = InputExample(texts="the quick fox jumps over the lazy dog", positions=[10,13])
fox_embedding = model.encode(examples) #The embedding of the target word "fox"
```


<b> Citation </b>

```

```
