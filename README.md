# XL-LEXEME
WiC Pretrained Model for Cross-Lingual LEXical sEMantic changE
(https://aclanthology.org/2023.acl-short.135.pdf)

Install the library:
```
git clone git@github.com:pierluigic/xl-lexeme.git
cd xl-lexeme
pip3 install .
```

Load the model (the model is available in the Hugging Face Model Hub https://huggingface.co/pierluigic/xl-lexeme):
```python
from WordTransformer import WordTransformer,InputExample

model = WordTransformer('pierluigic/xl-lexeme')

examples = InputExample(texts="the quick fox jumps over the lazy dog", positions=[10,13])
fox_embedding = model.encode(examples) #The embedding of the target word "fox"
```


<b> Citation </b>

```
@inproceedings{cassotti-etal-2023-xl,
    title = "{XL}-{LEXEME}: {W}i{C} Pretrained Model for Cross-Lingual {LEX}ical s{EM}antic chang{E}",
    author = "Cassotti, Pierluigi  and
      Siciliani, Lucia  and
      DeGemmis, Marco  and
      Semeraro, Giovanni  and
      Basile, Pierpaolo",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-short.135",
    pages = "1577--1585"
}
```
